# task_1_ ust_service_request_processing_system

# UST handles thousands of internal service requests every day:
# Laptop issues
# Software access requests
# Network problems
# Password resets
# HR document requests
# Facility issues
# UST wants to build a Service Request Processing System where:
# Every type of request MUST implement a method:
# process_request()
# But the way each request is processed is different, so UST wants a general rule
# (abstract class) and each department must follow it.

from abc import ABC,abstractmethod

class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority

        @abstractmethod
        def process_request(self):
            pass

    def show_basic_details(self):
        print("Request ID:",self.request_id)
        print("Requested_By:",self.requested_by)
        print("Priority:",self.priority)


# Create 4 child classes thatinherit from ServiceRequest :

# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"

class ItSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT Engineer...")
        print("Checking Laptop...")
        print("Issue Resolve!")
        print("-------------------------------------------------")

# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"

class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR Document")
        print("Sending via Email")
        print("--------------------------------------------------")

# 3. FacilityRequest
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"

class Facilityrequest(ServiceRequest):
    def process_request(self):
        print("Processing facility Request:")
        print("Assingning Facility Staff")
        print("Checking Issue")
        print("Job Completed")
        print("---------------------------------------------------")

# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"

class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying Approval")
        print("Granting Software Access")
        print("---------------------------------------------------")

# 1. Create at least 4 different request objects (one from each child class).
# 2. Store all objects in a list.
# 3. Loop through the list and call:
# show_basic_details()
# process_request()
# 4. The output should clearly show same method name,
# but different behavior → this proves abstraction + polymorphism.


r1 = ItSupportRequest(101,"Sai Vamsi","High")
r2 = HRDocumentRequest(102,"Tharun","Medium")
r3 = Facilityrequest(103,"Vijay","High")
r4 = SoftwareAccessRequest(104,"Vikram","High")

request = [r1,r2,r3,r4]

for r in request:
    r.show_basic_details()
    r.process_request()
    print()

# ------------------------------------------------------------------------------------------------------

# Sample Output

# Request ID: 101
# Requested_By: Sai Vamsi
# Priority: High
# Processing IT Support Request:
# Assigning IT Engineer...
# Checking Laptop...
# Issue Resolve!
# -------------------------------------------------

# Request ID: 102
# Requested_By: Tharun
# Priority: Medium
# Processing HR Document Request:
# Preparing HR Document
# Sending via Email
# --------------------------------------------------

# Request ID: 103
# Requested_By: Vijay
# Priority: High
# Processing facility Request:
# Assingning Facility Staff
# Checking Issue
# Job Completed
# ---------------------------------------------------

# Request ID: 104
# Requested_By: Vikram
# Priority: High
# Processing Software Access Request:
# Verifying Approval
# Granting Software Access
# ---------------------------------------------------


