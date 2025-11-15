#TASK: UST Service Request Processing System
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
    
    def show_basic_details(self):
        print("\nRequest ID:",self.request_id)
        print("Requested By:",self.requested_by)
        print("Priority:",self.priority)
        
    @abstractmethod
    def process_request(self):
        pass #Abstract Method

class ITSupportRequest(ServiceRequest):
    #Override the Abstract Method of Parent Class
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

it_req = ITSupportRequest(101,"Neha",'High')
hr_req = HRDocumentRequest(102,"Ram",'Low')
facility_req = FacilityRequest(103,'Priya','Medium')
software_req = SoftwareAccessRequest(104,'Rakesh','High')

#list of Requests
req_list = [it_req,hr_req,facility_req,software_req]

for req in req_list:
    req.show_basic_details()
    req.process_request()
    

#Sample Output 
# Request ID: 101
# Requested By: Neha
# Priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved

# Request ID: 102
# Requested By: Ram
# Priority: Low
# Preparing HR document
# Sending via email

# Request ID: 103
# Requested By: Priya
# Priority: Medium
# Assigning facility staff
# Checking issue
# Job completed

# Request ID: 104
# Requested By: Rakesh
# Priority: High
# Verifying approval
# Granting software access
    
