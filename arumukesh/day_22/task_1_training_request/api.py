from fastapi import FastAPI,HTTPException,routing,APIRouter,status,Depends
from model import TrackingRequest,Status,LoginRequest,Token,User
from datetime import datetime,timedelta
from auth import create_access_token,DEMO_USERNAME,DEMO_PASSWORD,ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM,get_current_user
from db_connection import get_connection

router=APIRouter(prefix="/request")

@router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticates a user and generates a JWT access token.

    Args:
        data (LoginRequest): Contains the username and password entered by the user.

    Returns:
        Token: Contains the generated JWT and token type.

    Raises:
        HTTPException: If the credentials do not match the stored demo credentials.
    """

    # Validate username and password against stored credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Set expiration time for JWT token
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    # Create the JWT access token
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


@router.post("/")
def create_request(req:TrackingRequest,current_user:User=Depends(get_current_user)):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        last_updated=datetime.now()
        path=(req.employee_id,req.employee_name,
              req.training_title,req.training_description,
              req.requested_date,req.status.value,
        req.manager_id,last_updated)
        cursor.execute("""insert into training_request(employee_id,employee_name,
                    training_title,training_description,
                    requested_date,status,
                    manager_id,last_updated) values (%s,%s,%s,
                    %s,%s,%s,%s,%s);""",path)
        conn.commit()
        return {"message":"Request added!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while inserting: {str(e)}")

@router.get("/")
def get_all_req():
    try :
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""select * from training_request;""")
        rows=cursor.fetchall()
        return {"detail fetched":rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while retriwving: {str(e)}")


@router.get("/{id}") 
def get_by_id(id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from training_request where id=%s ",(id,))
        row=cursor.fetchone()
        return{"details fetched ":row}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while retrieving: {str(e)}")
    
@router.put("/{id}") 
def update_req(id,req:TrackingRequest):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        path=(req.employee_id,req.employee_name,
        req.training_title,
        req.training_description,req.requested_date,req.status,
        req.manager_id,id)
        cursor.execute("""update training_request set employee_id=%s,employee_name=%s,
                    training_title=%s,training_description=%s,
                    requested_date=%s,status=%s,
                    manager_id=%s,last_updated=NOW() where id=%s""",path)
        conn.commit()
        return{"message":"Request updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while updating: {str(e)}")
    
@router.patch("/{id}")
def update_status(id:int,status:Status):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("update training_request set status=%s where id =%s;",(status,id))
        conn.commit()
        return {"message":"status Updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while updating: {str(e)}")
    
@router.delete("/{id}")
def delete_req(id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""delete from training_request where id=%s""",(id,))
        conn.commit()
        return {"message":"request deleted "}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while deleting: {str(e)}")
    
 