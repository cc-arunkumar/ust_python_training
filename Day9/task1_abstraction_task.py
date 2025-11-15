# Abstraction Task
# TASK: UST Service Request Processing
# System

from abc import ABC, abstractmethod

#Abstract class
class ServiceRequest(ABC):
    def __init__(self, req_id,req_by,priority):
        self.req_id =req_id
        self.req_by = req_by
        self.priority = priority

    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print(f"\nRequest ID: {self.req_id}")
        print(f"Requested By: {self.req_by}")
        print(f"Priority: {self.priority}")


# child - 1 ITSupportRequest
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")

class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("\nPreparing HR document")
        print("Sending via email")

class  FacilityRequest(ServiceRequest):
    def process_request(self):
        print("\nAssigning facility staff")
        print("Checking issue")
        print("Job completed")

class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("\nVerifying approval")
        print("Granting software access")


it_sup_req = ITSupportRequest("E101", "Madhan", "High")
hr_req = HRDocumentRequest("E102", "Sudhan", "Low")
network_issue_req = FacilityRequest("E103", "Gowtham", "Medium")
hr_doc_req = SoftwareAccessRequest("E104", "Dev", "High")

obj_list = [it_sup_req,hr_req,network_issue_req,hr_doc_req]

for req in obj_list:
    req.show_basic_details()
    req.process_request()

# sample output:
# Request ID: E101
# Requested By: Madhan
# Priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved

# Request ID: E102
# Requested By: Sudhan
# Priority: Low

# Preparing HR document
# Sending via email

# Request ID: E103
# Requested By: Gowtham
# Priority: Medium

# Assigning facility staff
# Checking issue
# Job completed

# Request ID: E104
# Requested By: Dev
# Priority: High

# Verifying approval
# Granting software access






