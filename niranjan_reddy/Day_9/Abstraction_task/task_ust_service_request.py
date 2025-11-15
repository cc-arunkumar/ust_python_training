# Abstraction Task


#  TASK: UST Service Request Processing System 


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
#  But the way each request is processed is different, so UST wants a general rule (abstract class) and each department must follow it.

# Create an abstract base class called ServiceRequest
# It must contain:
#  A constructor with:
#  request_id
#  requested_by
#  priority

# An abstract method:
#  process_request()
#  Every child class must override this method.

#  A normal concrete method:
#  show_basic_details()

#  Which prints:
#  Request ID
#  Requested by
#  Priority

from abc import ABC,abstractmethod

class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by, priority):
        self.request_id=request_id
        self.request_by=requested_by
        self.priority=priority
    
    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print("Request ID:",self.request_id)
        print("Requested By:",self.request_by)
        print("Priority:",self.priority)
    
# Create 4 child classes that inherit from ServiceRequest :

#  1. ITSupportRequest
#  Print steps like:
#  "Assigning IT engineer"
#  "Checking laptop"
#  "Issue resolved"

class ITSupportRequest(ServiceRequest):

    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved!")

        
#  2. HRDocumentRequest
#  Print:
#  "Preparing HR document"
#  "Sending via email"

class HRDocumentRequest(ServiceRequest):

    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")



#  3. FacilityRequest
# Print:
#  "Assigning facility staff"
#  "Checking issue"
#  "Job completed"

class FacilityRequest(ServiceRequest):
    
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")


#  4. SoftwareAccessRequest
#  Print:
#  "Verifying approval"
#  "Granting software access"
#  Each class must implement its own 
# process_request() .

class SoftwareAccessRequest(ServiceRequest):
    
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")



#  Main Program Requirements
#  Create at least 4 different request objects (one from each child class).
#  Store all objects in a list.
#  Loop through the list and call:
#  show_basic_details()
#  process_request()
#  The output should clearly show same method name,
#  but different behavior → this proves abstraction + polymorphism


service1 = ITSupportRequest(101, "Arun", "High")
service2 = HRDocumentRequest(102, "Niranjan", "Medium")
service3 = FacilityRequest(103, "Sai", "Low")
service4 = SoftwareAccessRequest(104, "Abhi", "High")

services=[service1,service2,service3,service4]

for  service in services:
    service.show_basic_details()
    service.process_request()
    print("----------------")

# Sample output

# Request ID: 101
# Requested By: Arun
# Priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved!
# ----------------
# Request ID: 102
# Requested By: Niranjan
# Priority: Medium
# Preparing HR document
# Sending via email
# ----------------
# Request ID: 103
# Requested By: Sai
# Priority: Low
# Assigning facility staff
# Checking issue
# Job completed
# ----------------
# Request ID: 104
# Requested By: Abhi
# Priority: High
# Verifying approval
# Granting software access
# ----------------