from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from models import Job,ResourceRequest
from pymongo import ReturnDocument

client = AsyncIOMotorClient(
    "mongodb+srv://303391_db_user:5IhrghdRaiXTR22b@cluster0.i0ih74y.mongodb.net/talent_management?retryWrites=true&w=majority&appName=Cluster0"
)
db = client.talent_management

BANDS = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3']

async def get_jobs(location: Optional[str], current_user):
    """
    Role-based job access:
    - Admin: all jobs
    - Employee (TP): jobs in band ±1, matching skills, optional location
    - Employee (non-TP): all jobs
    - WFM: jobs where wfm_id == current_user.id
    - HM: jobs where hm_id == current_user.id
    """
    role = current_user["role"]  # "Admin", "Employee", "WFM", "HM"

    if role == "Admin":
        cursor = db.jobs.find({})
        return await cursor.to_list(length=100)

    elif role in ["TP", "Non TP"]:
        emp = await db.employees.find_one({"employee_id": current_user["employee_id"]})
        if emp and role == "TP":
            curr_band = emp["Band"]
            curr_skills = emp.get("Detailed Skill Set (List of top skills on profile)", [])

            indx = BANDS.index(curr_band)
            above_band = BANDS[indx+1] if indx < len(BANDS)-1 else BANDS[indx]
            below_band = BANDS[indx-1] if indx > 0 else BANDS[indx]
            print(above_band,curr_band,below_band)
            print(curr_skills)
            query = {
                "job_grade": {"$in": [curr_band, above_band, below_band]},
                "required_skills": {"$in": curr_skills}
            }
            if location:
                query["city"] = location

            cursor = db.jobs.find(query)
            docs = await cursor.to_list(length=100)
            for d in docs:
                d["_id"] = str(d["_id"])
            return docs
        else:
            cursor = db.jobs.find({})
            docs = await cursor.to_list(length=100)
            for d in docs:
                d["_id"] = str(d["_id"])
            return docs

    elif role == "WFM":
        query = {"wfm_id": current_user["employee_id"]}
        cursor = db.resource_request.find(query)
        docs = await cursor.to_list(length=100)
        for d in docs:
            d["_id"] = str(d["_id"])
        return docs

    elif role == "HM":
        query = {"HM ID": current_user["employee_id"]}
        cursor = db.resource_request.find(query)
        docs = await cursor.to_list(length=100)
        for d in docs:
            d["_id"] = str(d["_id"])
        return docs



async def create_job_and_resource_request(job_data: ResourceRequest, current_user):
    """
    Only Admins and HMs can create jobs and insert ResourceRequest into both tables.
    """
    if current_user.role != "HM":
        raise PermissionError("You do not have permission to create jobs.")
    
    # Start a MongoDB session for the transaction
    async with db.client.start_session() as session:
        try:
            # Step 1: Insert ResourceRequest
            resource_request_data = job_data.__dict__()  # Convert the ResourceRequest to a dict
            # Insert the resource request into the ResourceRequest table
            result = await db.resource_request.insert_one(resource_request_data, session=session)

            # Step 2: Create Job data based on ResourceRequest
            job_data_for_job_table = {
                "rr_id": str(result.inserted_id),  # Link the Job to ResourceRequest via rr_id
                "title": job_data.project_name,
                "location": job_data.city,
                "required_skills": job_data.mandatory_skills + job_data.optional_skills,
                "description": job_data.job_description,
                "start_date": job_data.project_start_date,
                "end_date": job_data.project_end_date,
                "wfm_id": job_data.wfm_id,
                "hm_id": job_data.hm_id,
                "status": "Open",
                "account_name": job_data.account_name,
                "project_id": job_data.project_id,
                "created_at": job_data.raised_on,
            }

            # Step 3: Insert the Job data into the Job table
            new_job = Job(**job_data_for_job_table)
            await db.jobs.insert_one(new_job.__dict__(), session=session)

            # Commit the transaction
            session.commit_transaction()

            return str(result.inserted_id)  # Return ResourceRequest ID as confirmation

        except Exception as e:
            # Abort the transaction if there is any error
            session.abort_transaction()
            raise Exception(f"Error occurred: {e}")



async def update_job_and_resource_request(job_id: str, update_data: ResourceRequest, current_user):
    """
    Only Admins and HMs can update jobs.
    - HMs can only update jobs they own (hm_id == current_user.id).
    """
    if current_user.role == "HM":
        async with db.client.start_session() as session:
            try:
                # Step 1: Update ResourceRequest (find by job_id to get rr_id)
                job = await db.jobs.find_one({"_id": ObjectId(job_id), "hm_id": current_user.id})
                if not job:
                    raise PermissionError("Job not found or you're not authorized to update this job.")

                rr_id = job["rr_id"]  # Get the linked resource request ID

                # Update ResourceRequest in resource_request table
                update_resource_request_data = update_data.__dict__(exclude_unset=True)
                update_result = await db.resource_request.update_one(
                    {"_id": ObjectId(rr_id)},
                    {"$set": update_resource_request_data},
                    session=session
                )
                
                # Check if ResourceRequest was found and updated
                if update_result.matched_count == 0:
                    raise Exception("ResourceRequest not found for the job.")

                # Step 2: Update Job data in jobs table
                update_job_data = {
                    "title": update_data.project_name,
                    "location": update_data.city,
                    "required_skills": update_data.mandatory_skills + update_data.optional_skills,
                    "description": update_data.job_description,
                    "start_date": update_data.project_start_date,
                    "end_date": update_data.project_end_date,
                    "wfm_id": update_data.wfm_id,
                    "hm_id": update_data.hm_id,
                    "status": update_data.rr_status,  # If you want to set status based on the RR status
                    "account_name": update_data.account_name,
                    "project_id": update_data.project_id,
                    "last_updated_on": update_data.last_updated_on,
                }

                # Update the Job record in the jobs table
                await db.jobs.update_one(
                    {"_id": ObjectId(job_id), "hm_id": current_user.id},
                    {"$set": update_job_data},
                    session=session
                )

                # Commit the transaction
                session.commit_transaction()

                return True  # Successful update

            except Exception as e:
                # Abort the transaction if there is any error
                session.abort_transaction()
                raise Exception(f"Error occurred: {e}")
    else:
        raise PermissionError("You do not have permission to update jobs.")
