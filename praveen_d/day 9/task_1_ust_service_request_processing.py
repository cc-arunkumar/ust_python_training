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



# Create an abstract base class called ServiceRequest
# It must contain:
# 1. A constructor with:
# request_id
# requested_by
# priority
from abc import ABC,abstractmethod

class Service_Request(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority

# 2. An abstract method:
# process_request()
# Every child class must override this method.
    def process_request(self):
        pass

# 3. A normal concrete method:
# show_basic_details()
# Which prints:
# Request ID
# Requested by
# Priority
    def show_basic_details(self):
        print(f"The request ID:{self.request_id}")
        print(f"Requested by:{self.requested_by}")
        print(f"Priority:{self.priority}")

# Create 4 child classes thatinherit from
# ServiceRequest :
# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"
class It_Request(Service_Request):
    #  Service_Request.__init__(self,request_id,requested_by,priority)
     def process_request(self):
                print("Assigning IT engineer")
                print("Checking laptop")
                print("Issue resolved")

# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"
class HRDocumentRequest(Service_Request):
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")

# 3. FacilityRequest
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"
class FacilityRequest(Service_Request):
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")

# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"
# Each class must implement its own process_request() .
class SoftwareAccessRequest(Service_Request):
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")

# Main Program Requirements
# 1. Create at least 4 different request objects (one from each child class).
# 2. Store all objects in a list.
# 3. Loop through the list and call:
# show_basic_details()
# process_request()
# 4. The output should clearly show same method name,
# but different behavior → this proves abstraction + polymorphism.
gendrel_service=It_Request(102,"kamal",5)
hr_request=HRDocumentRequest(104,"Arun",7)
finance_service=FacilityRequest(105,"Uma",8)
software_acess_request=SoftwareAccessRequest(106,"Ak",10)

request_list=[Service_Request(101,"Ravi",2),gendrel_service,hr_request,finance_service,software_acess_request]

for emp in request_list:
    emp.show_basic_details()
    emp.process_request()
    print("--------------------------------------------------")


# Sample output:
# The request ID:101
# Requested by:Ravi
# Priority:2
# --------------------------------------------------
# The request ID:102
# Requested by:kamal
# Priority:5
# Assigning IT engineer
# Checking laptop
# Issue resolved
# --------------------------------------------------
# The request ID:104
# Requested by:Arun
# Priority:7
# Preparing HR document
# Sending via email
# --------------------------------------------------
# The request ID:105
# Requested by:Uma
# Priority:8
# Assigning facility staff
# Checking issue
# Job completed
# --------------------------------------------------
# The request ID:106
# Requested by:Ak
# Priority:10
# Verifying approval
# Granting software access
# --------------------------------------------------