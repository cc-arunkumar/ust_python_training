# �� Create an abstract base class called ServiceRequest
# It must contain:
# 1. A constructor with:
# request_id
# requested_by
# priority
# Abstraction Task 1
# 2. An abstract method:
# process_request()
# Every child class must override this method.
# 3. A normal concrete method:
# show_basic_details()
# Which prints:
# Request ID
# Requested by
# Priority
# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"
# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"
# 3. FacilityRequest
# Abstraction Task 2
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"
# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"
# Each class must implement its own process_request() .
from  abc import ABC,abstractmethod 

class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
        
    @abstractmethod
    def process_request():
        pass
    
    def show_basic_details(self):
        print(f"RequestID:{self.request_id}")
        print(f"Requested by: {self.requested_by}")
        print(f"Priority : {self.priority}")


class ITSupportRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print(f"Assigning IT engineer")
        print(f"Checking laptop")
        print(f"Issue resolved")

class HRDocumentRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print(f"Preparing HR document")
        print(f"Sending via email")

class FacilityRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print(f"Assigning facility staff")
        print(f"Checking issue")
        print(f"Job completed")
        
class SoftwareAccessRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        

itsupport=ITSupportRequest("7689","Manager",1)
hrrequest=HRDocumentRequest("7690","HR",2)
facilityrequest=FacilityRequest("7691","CEO",4)
softwarerequest =SoftwareAccessRequest("7692","Director",3)
list1=[itsupport,hrrequest,facilityrequest,softwarerequest]
for item in list1:
    item.process_request()
    item.show_basic_details()
    print("=========================")



    
# sample execution 
# Assigning IT engineer
# Checking laptop
# Issue resolved
# RequestID:7689
# Requested by: Manager
# Priority : 1
# =========================
# Preparing HR document
# Sending via email
# RequestID:7690
# Requested by: HR
# Priority : 2
# =========================
# Assigning facility staff
# Checking issue
# Job completed
# RequestID:7691
# Requested by: CEO
# Priority : 4
# =========================
# Verifying approval
# Granting software access
# RequestID:7692
# Requested by: Director
# Priority : 3
# =========================