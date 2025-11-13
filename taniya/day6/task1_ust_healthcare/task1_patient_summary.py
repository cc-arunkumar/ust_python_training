import csv
with open("ust_health_care_visits_cleaned.csv","r") as file:
    reader1=csv.DictReader(file)
    # fieldnames=reader.fieldnames
    with open("patient_summary.csv","w",newline='') as file02:
        # assigning header files for the new list
        fieldnames=["patient_id","name","visit_times","total_billed_amount","has_pending_payments"]
        writer1=csv.DictWriter(file02,fieldnames=fieldnames)
        writer1.writeheader()
        # creating empty dictionary to store the summary values
        patient_data={}
        # next(file)

        for row in reader1:
            p_id=row["patient_id"]
            name=row["name"]
            billed_str=row.get("billed_amount","")
            p_stat=row["payment_status"]
            # converting string to float val 
            billed = float(billed_str) if billed_str else 0.0
            try:
                billed = float(billed_str) if billed_str else 0.0
            except ValueError:
                print(f"⚠️ Invalid billed_amount for {p_id}: {billed_str}")
                billed = 0.0       
                # creating new dictionary for new p_id                
            if p_id not in patient_data:
                patient_data[p_id]={
                    "name":name,
                    "visit_times":0,
                    "total_billed_amount":0.00,
                    "has_pending_payments":"No"
                }
            # modifying the values on every new p_id addition
            patient_data[p_id]["visit_times"]+=1
            patient_data[p_id]["total_billed_amount"]+=billed
            if p_stat !="Paid":
                patient_data[p_id]["has_pending_payments"]="Yes"
        # writing dictionar data to summary.csv file
        for p_id,data in patient_data.items():
            writer1.writerow({
                "patient_id":p_id,
                "name":data["name"],
                "visit_times":data["visit_times"],
                "total_billed_amount": f"{data['total_billed_amount']:.2f}",
                "has_pending_payments":data["has_pending_payments"]})