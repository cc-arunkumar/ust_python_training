# Abstraction 

from abc import ABC, abstractmethod

class ServiceRequest(ABC):
    def __init__(self, request_id, requested_by, priority):
        # Initialize common attributes for all service requests
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority

    @abstractmethod
    def process_request(self):
        # Abstract method - must be implemented by subclasses
        pass
    
    def show_basic_details(self):
        # Display basic details of the request
        print(f"Request_ID: {self.request_id}")
        print(f"Requested_By: {self.requested_by}")
        print(f"Priority: {self.priority}")
        # Show the class name (which subclass is being used)
        print("\"Class Name\":", self.__class__.__name__)


# Subclass for IT support requests
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        # Implementation of abstract method for IT support
        print("Processing IT Support Request:")
        print("Assigning IT engineer")
        print("Checking laptop.....")
        print("Issue resolved")
        print("*******************************\n")


# Subclass for HR document requests
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        # Implementation of abstract method for HR documents
        print("Processing HR document request:")
        print("Preparing HR document.....")
        print("Sending via email")
        print("*******************************\n")


# Subclass for facility-related requests
class FacilityRequest(ServiceRequest):
    def process_request(self):
        # Implementation of abstract method for facility issues
        print("Processing facility request:")
        print("Assigning facility staff.....")
        print("Checking issue.....")
        print("Job completed")
        print("*******************************\n")

# Subclass for software access requests
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        # Implementation of abstract method for software access
        print("Software access request:")
        print("Verifying approval.....")
        print("Granting software access")
        print("*******************************")

# Create a list of different service requests
request = [
    ITSupportRequest(101, "Gopi", "High"),
    HRDocumentRequest(102, "Shiv", "Medium"),
    FacilityRequest(103, "Yashu", "Low"),
    SoftwareAccessRequest(104, "Lara", "High")
]

# Loop through each request and process it
for req in request:
    req.show_basic_details()   # Show common details
    req.process_request()      # Call subclass-specific implementation


#o/p:
# Request_ID: 101
# Requested_By: Gopi
# Priority: High
# "Class Name": ITSupportRequest 
# Processing IT Support Request: 
# Assigning IT engineer
# Checking laptop.....
# Issue resolved
# *******************************

# Request_ID: 102
# Requested_By: Shiv
# Priority: Medium
# "Class Name": HRDocumentRequest
# Processing HR document request:
# Preparing HR document.....
# Sending via email
# *******************************

# Request_ID: 103
# Requested_By: Yashu
# Priority: Low
# "Class Name": FacilityRequest
# Processing facility request:
# Assigning facility staff.....
# Checking issue.....
# Job completed
# *******************************

# Request_ID: 104
# Requested_By: Lara
# Priority: High
# "Class Name": SoftwareAccessRequest
# Software access request:
# Verifying approval.....
# Granting software access
# *******************************