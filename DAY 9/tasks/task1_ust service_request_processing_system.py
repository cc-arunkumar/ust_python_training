from abc import ABC, abstractmethod

# Abstract Base Class for all service requests
class ServiceRequest(ABC):

    def __init__(self, request_id, requested_by, priority):
        self.rrequest_id = request_id          # Unique request ID
        self.requested_by = requested_by       # Employee who requested the service
        self.priority = priority               # Priority level (High/Medium/Low)

    @abstractmethod
    def process_request(self):
        """Abstract method — must be implemented by all subclasses"""
        pass
    
    # Common method to display request details
    def show_basic_details(self):
        print(f"Request ID : {self.rrequest_id}")
        print(f"Requested By : {self.requested_by}")
        print(f"Priority : {self.priority}")



# Handles IT-related support issues
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")



# Handles HR-related document requests
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document")
        print("Sending via email")



# Handles physical facility-related issues
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")



# Handles software access and permission requests
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval")
        print("Granting software access")



# Creating objects for different service requests
r1 = ITSupportRequest(1, "Gowtham", "High")
r2 = HRDocumentRequest(2, "Mani", "High")
r3 = FacilityRequest(3, "Dinesh", "Medium")
r4 = SoftwareAccessRequest(4, "Gowtham", "Low")

# Storing objects in a list
requested_service = [r1, r2, r3, r4]

# Iterating and processing each request
for req in requested_service:
    req.show_basic_details()
    req.process_request()
    print("------------")


"""
SAMPLE OUTPUT

Request ID :1
Requested by :Gowthm
Priority: High
Processing IT Support Request :
Assigning IT engineer
Checking laptop
Issue resolved
------------
Request ID :2
Requested by :Mani
Priority: High
Processing HR Document Request :
Preparing HR document
Sending via email
------------
Request ID :3
Requested by :Dinesh
Priority: Medium
Processing Facility Request :
Assigning facility staff
Checking issue
Job completed
------------
Request ID :4
Requested by :Gowthm
Priority: Low
Software Access Request :
Verifying approval
Granting software access
------------

"""