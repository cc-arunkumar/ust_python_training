#Task: UST Service Request Processing System
from abc import ABC, abstractmethod
class ServiceRequest(ABC):
    def __init__(self,request_id,request_by,priority):
        self.request_id=request_id
        self.request_by=request_by
        self.priority=priority
    @abstractmethod
    def process_request(self):
        pass
    def show_basic_details(self):
        print("Request ID: ",self.request_id)
        print("Request by: ",self.request_by)
        print("Priority: ",self.priority)
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

isr=ITSupportRequest(10,"Sovan","high")
hdr=HRDocumentRequest(2,"Rajeev","mid")
fr=FacilityRequest(3,"Shivam","high")
sar=SoftwareAccessRequest(4,"Rishi","low")



l=[isr,hdr,fr,sar]
for li in l:
    li.show_basic_details()
    li.process_request()
    
#Sample Execution
# Request ID:  10
# Request by:  Sovan   
# Priority:  high      
# Assigning IT engineer
# Checking laptop      
# Issue resolved
# Request ID:  2
# Request by:  Rajeev
# Priority:  mid
# Preparing HR document
# Sending via email
# Request ID:  3
# Request by:  Shivam
# Priority:  high
# Assigning facility staff
# Checking issue
# Job completed
# Request ID:  4
# Request by:  Rishi
# Priority:  low
# Verifying approval
# Granting software access
    