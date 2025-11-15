# Task
# Abstraction Task
#  TASK: UST Service Request Processing 
# System 
# UST handles thousands of internal service requests every day:
#  Laptop issues
#  Software access requests
#  Network problems
#  Password resets
#  HR document requests
#  Facility issues
#  UST wants to build a Service Request Processing System where:
#  Every type of request MUST implement a method:
#  process_request()
#  But the way each request is processed is different, so UST wants a general rule 
# (abstract class) and each department must follow it.
#  Your Requirements
#  👉
#  Create an abstract base class called 
# It must contain:
#   A constructor with:
#  request_id
#  requested_by
#  priority
#  ServiceRequest
#  1
#  Abstraction Task
#  An abstract method:
#  process_request()
#  Every child class must override this method.
#   A normal concrete method:
#  show_basic_details()
#  Which prints:
#  Request ID
#  Requested by
#  Priority
#  Create 4 child classes that inherit from 
# ServiceRequest :
#  1. ITSupportRequest
#  Print steps like:
#  "Assigning IT engineer"
#  "Checking laptop"
#  "Issue resolved"
#  2. HRDocumentRequest
#  Print:
#  "Preparing HR document"
#  "Sending via email"
#  3. FacilityRequest
#  2
#  Abstraction Task
# Print:
#  "Assigning facility staff"
#  "Checking issue"
#  "Job completed"
#  4. SoftwareAccessRequest
#  Print:
#  "Verifying approval"
#  "Granting software access"
#  Each class must implement its own 
# process_request() .
#  Main Program Requirements
#   Create at least 4 different request objects (one from each child class).
#   Store all objects in a list.
#   Loop through the list and call:
#  show_basic_details()
#  process_request()
#   The output should clearly show same method name,
#  but different behavior → this proves abstraction + polymorphism.
#  Expected Output (sample)
#  Request ID 101
#  Requested By: Arun
#  Priority: High
#  Processing IT Support Request:
#  Assigning IT Engineer...
#  Checking laptop...
#  3
#  Abstraction Task
# Issue resolved!
#  Request ID 102
#  Requested By: Priya
#  Priority: Medium
#  Processing HR Document Request:
#  Preparing document...
#  Email sent.
#  ...
#  4
#  Abstraction Task


from abc import ABC,abstractmethod

class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
        
    @abstractmethod
    def process_request(self):
        pass
    def show_basic_details(self):
        print(f"Request ID : {self.request_id}")
        print(f"Request By : {self.requested_by}")
        print(f"Priroty : {self.priority}")
        
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        
emp1=ITSupportRequest(101,"Taniya","High")
emp2=HRDocumentRequest(102,"Prithvi","Medium")
emp3=FacilityRequest(103,"Rohit","High")
emp4=SoftwareAccessRequest(104,"Harsh","Medium")

show =[emp1,emp2,emp3,emp4]
for showing in show:
    showing.show_basic_details()
    showing.process_request()
    
# Output
# Request ID : 101
# Request By : Taniya
# Priroty : High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# Request ID : 102
# Request By : Prithvi
# Priroty : Medium
# Preparing HR document
# Sending via email
# Request ID : 103
# Request By : Rohit
# Priroty : High
# Assigning facility staff
# Checking issue
# Job completed
# Request ID : 104
# Request By : Harsh
# Priroty : Medium
# Verifying approval
# Granting software access
        
        
            
        