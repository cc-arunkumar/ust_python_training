# Create an abstract base class called ServiceRequest
# It must contain:
# 1. A constructor with:
# request_id
# requested_by
# priority


from abc import ABC, abstractmethod
class ServiceRequest(ABC):
    def __init__(self, request_id, requested_by, priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
        
# 2. An abstract method:
# process_request()

    
    @abstractmethod
    def process_request(self):
        pass
    
# 3. A normal concrete method:
# show_basic_details()
# Which prints:
# Request ID
# Requested by
# Priority

    
    def show_basic_details(self):
        print("===> Request ID: ", self.request_id)
        print("-----> Requested by: ", self.requested_by)
        print("********> Priority: ", self.priority)
        print("---------> Class Name: ", self.__class__.__name__)
        
# Create 4 child classes thatinherit from
# ServiceRequest :
# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"

class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT Engineer")
        print("Checking Laptop")
        print("Issue Resolved")
        print("------------------------------------------------------------\n")
        
# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"
        
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
        print("------------------------------------------------------------\n")    
        
# 3. FacilityRequest
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"
  
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
        print("------------------------------------------------------------\n")
        
# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"
# Each class must implement its own process_request() .
        


class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        print("------------------------------------------------------------\n")
        
# 1. Create at least 4 different request objects (one from each child class).
# 2. Store all objects in a list.
# 3. Loop through the list and call:
# show_basic_details()
# process_request()
# 4. The output should clearly show same method name,
# but different behavior → this proves abstraction + polymorphism.
            
req1 = ITSupportRequest(101, "Arun", "High")
req2 = HRDocumentRequest(102, "Priya", "Medium")
req3 = FacilityRequest(103, "Varsha", "Low")
req4 = SoftwareAccessRequest(104, "yashu", "High")

requests=[req1, req2, req3, req4]

for req in requests:
    req.show_basic_details()
    req.process_request()
print("*********** Execution complete ************")



# Output:

# ===> Request ID:  101
# -----> Requested by:  Arun
# ********> Priority:  High
# ---------> Class Name:  ITSupportRequest
# Assigning IT Engineer
# Checking Laptop
# Issue Resolved
# ------------------------------------------------------------

# ===> Request ID:  102
# -----> Requested by:  Priya
# ********> Priority:  Medium
# ---------> Class Name:  HRDocumentRequest
# Preparing HR document
# Sending via email
# ------------------------------------------------------------

# ===> Request ID:  103
# -----> Requested by:  Varsha
# ********> Priority:  Low
# ---------> Class Name:  FacilityRequest
# Assigning facility staff
# Checking issue
# Job completed
# ------------------------------------------------------------

# ===> Request ID:  104
# -----> Requested by:  yashu
# ********> Priority:  High
# ---------> Class Name:  SoftwareAccessRequest
# Verifying approval
# Granting software access
# ------------------------------------------------------------

# *********** Execution complete ************
