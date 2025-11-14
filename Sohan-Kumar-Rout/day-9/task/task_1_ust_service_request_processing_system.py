#Task : UST Service Request Processing System

#Code

from abc import ABC, abstractmethod

class ServiceRequest(ABC):
    
    
    def __init__(self,request_id,requested_by,priority):
        self.request_id =request_id
        self.requested_by=requested_by
        self.priority= priority
        
    @abstractmethod   
    def process_request(self):
        pass
    def basic_details(self):
        print(f"Requested_id : {self.request_id}")
        print(f"Requested_By : {self.requested_by}")
        print(f"Priority : {self.priority}")
        
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT Engineer")
        print("Checking Laptop")
        print("Issue Resolved")
        
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document")
        print("Sending Via Email")
        
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning Facility staff")
        print("Checking issue")
        print("Job Completed")
    
class SoftwareAccessRequest(ServiceRequest):
    print("Verifying approval")
    print("Granting software access")



req1=ITSupportRequest(10001,"Sohan","High")

request=[req1]

for req in request:
    req1.basic_details()
    req1.process_request()

#Output
# Verifying approval
# Granting software access
# Requested_id : 10001
# Requested_By : Sohan
# Priority : High
# Assigning IT Engineer
# Checking Laptop
# Issue Resolved
        
    