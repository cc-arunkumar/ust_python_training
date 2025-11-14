from abc import ABC, abstractmethod
class ServiceRequest(ABC):
    
    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
        
    @abstractmethod
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")

class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT Engineer...")
        print("Checking laptop...")
        print("Issue resolved!\n")

class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document...")
        print("Sending via email...\n")


class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff...")
        print("Checking issue...")
        print("Job completed!\n")


class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval...")
        print("Granting software access...\n")
        

it1=ITSupportRequest("101","Harsh","High")
hr1=HRDocumentRequest("102","Rohit","Medium")
fac1=FacilityRequest("103","Prithvi","Low")
sw1=SoftwareAccessRequest("104","Taniya","High")

sr=[it1,hr1,fac1,sw1]

for s in sr:
    s.show_basic_details()
    s.process_request()



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