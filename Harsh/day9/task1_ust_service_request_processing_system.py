from abc import ABC, abstractmethod

# Abstract base class for all service requests
class ServiceRequest(ABC):
    
    def __init__(self, request_id, requested_by, priority):
        # Common attributes for all service requests
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
        
    @abstractmethod
    def process_request(self):
        # Abstract method: must be implemented by subclasses
        pass
    
    def show_basic_details(self):
        # Common method to display basic request details
        print(f"Request ID: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")


# Subclass for IT support requests
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT Engineer...")
        print("Checking laptop...")
        print("Issue resolved!\n")


# Subclass for HR document requests
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document...")
        print("Sending via email...\n")


# Subclass for facility-related requests
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff...")
        print("Checking issue...")
        print("Job completed!\n")


# Subclass for software access requests
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval...")
        print("Granting software access...\n")
        

# ------------------- Testing -------------------

# Create different types of service requests
it1 = ITSupportRequest("101", "Harsh", "High")
hr1 = HRDocumentRequest("102", "Rohit", "Medium")
fac1 = FacilityRequest("103", "Prithvi", "Low")
sw1 = SoftwareAccessRequest("104", "Taniya", "High")

# Store them in a list
sr = [it1, hr1, fac1, sw1]

# Loop through and process each request
for s in sr:
    s.show_basic_details()   # Show common details
    s.process_request()      # Call subclass-specific implementation
    
    

# Request ID: 101
# Requested By: Harsh
# Priority: High
# Processing IT Support Request:
# Assigning IT Engineer...
# Checking laptop...
# Issue resolved!

# Request ID: 102
# Requested By: Rohit
# Priority: Medium
# Processing HR Document Request:
# Preparing HR document...
# Sending via email...

# Request ID: 103
# Requested By: Prithvi
# Priority: Low
# Processing Facility Request:
# Assigning facility staff...
# Checking issue...
# Job completed!

# Request ID: 104
# Requested By: Taniya
# Priority: High
# Processing Software Access Request:
# Verifying approval...
# Granting software access...