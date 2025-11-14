# Abstraction Task

# TASK: UST Service Request Processing
# System
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

from abc import ABC ,abstractmethod
class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority

    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print(f"Request ID:{self.request_id}")
        print(f"Requested By:{self.requested_by}")
        print(f"Priority:{self.priority}")

# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"

class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request")
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue Resolved")
        print("----------------------------------------")

# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"

class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
        print("----------------------------------------")

# 3. FacilityRequest
# Abstraction Task 2
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"

class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
        print("----------------------------------------")

# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"

class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        print("----------------------------------------")

a1=ITSupportRequest(101,"Arjun","Medium")
a2=HRDocumentRequest(102,"Rahul","High")
a3=FacilityRequest(103,"sohail","Low")
a4=SoftwareAccessRequest(104,"charan","High")

req_list=[a1,a2,a3,a4]

for i in req_list:
    i.show_basic_details()
    i.process_request()

#Sample Output
# Request ID:101
# Requested By:Arjun
# Priority:Medium
# Processing IT Support Request
# Assigning IT engineer
# Checking laptop
# Issue Resolved
# ----------------------------------------
# Request ID:102
# Requested By:Rahul
# Priority:High
# Preparing HR document
# Sending via email
# ----------------------------------------
# Request ID:103
# Requested By:sohail
# Priority:Low
# Assigning facility staff
# Checking issue
# Job completed
# ----------------------------------------
# Request ID:104
# Requested By:charan
# Priority:High
# Verifying approval
# Granting software access
# ----------------------------------------
