# TASK: UST Service Request Processing System
from abc import ABC, abstractmethod
class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
    @abstractmethod
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"request_id: {self.request_id}")
        print(f"request_by: {self.requested_by}")
        print(f"priority: {self.priority}")
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        
        
        
a1=ITSupportRequest(101,"HR","High")
b1=HRDocumentRequest(102,"IT","midium")
c1=FacilityRequest(103,"Managment","low")
d1=SoftwareAccessRequest(104,"security","High")

request=[a1,b1,c1,d1]

for requests in request:
    print("....................")
    requests.show_basic_details()
    requests.process_request()
    
# output 
# ....................
# request_id: 101
# request_by: HR
# priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# ....................
# request_id: 102
# request_by: IT
# priority: midium
# Preparing HR document
# Sending via email
# ....................
# request_id: 103
# request_by: Managment
# priority: low
# Assigning facility staff
# Checking issue
# Job completed
# ....................
# request_id: 104
# request_by: security
# priority: High
# Verifying approval
# Granting software access