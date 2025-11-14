from abc import ABC, abstractmethod

class ServiceRequest(ABC):

    def __init__(self,request_id,requested_by,priority):
        self.rrequest_id=request_id
        self.requested_by=requested_by
        self.priority=priority

    @abstractmethod
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"Request ID :{self.rrequest_id}")
        print(f"Requested by :{self.requested_by}")
        print(f"Priority: {self.priority}")
    

class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request :")
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")

class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request :")
        print("Preparing HR document")
        print("Sending via email")
    
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Processing Facility Request :")
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")

class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Software Access Request :")
        print("Verifying approval")
        print("Granting software access")

# Creating objects

r1=ITSupportRequest(1,"Gowthm","High")
r2=HRDocumentRequest(2,"Mani","High")
r3=FacilityRequest(3,"Dinesh","Medium")
r4=SoftwareAccessRequest(4,"Gowthm","Low")

# storing all the objects in list
requested_service=[r1,r2,r3,r4]

#iterAtion in list for objects
for i in requested_service:
    i.show_basic_details()
    i.process_request()
    print("------------")
