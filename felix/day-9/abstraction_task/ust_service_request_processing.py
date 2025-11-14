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


from abc import ABC,abstractmethod

# Creating parent class ServeceRequest
class ServiceRequest:
    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
        
    # Creating the abstract method
    @abstractmethod  
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested by: {self.requested_by}")
        print(f"Priority: {self.priority}")
        
# class ITSupportRequest is the child class of ServiceRequest
class ITSupportRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")
        
# class HRDocumentRequest is the child class of ServiceRequest
class HRDocumentRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
        
# class FacilityRequest is the child class of ServiceRequest
class FacilityRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
        
# class SoftwareAccessRequest is the child class of ServiceRequest
class SoftwareAccessRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        ServiceRequest.__init__(self,request_id, requested_by, priority)
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        
# Creating objects for all child classes
req1 = ITSupportRequest(101,"Felix","High")
req2 = HRDocumentRequest(102,"Arun","Medium")
req3 = FacilityRequest(103,"Arjun","High")
req4 = SoftwareAccessRequest(104,"Akhil","Low")

# inserting all objects into a list
list = [req1,req2,req3,req4]

# looping through each objects and callig tow methods
for obj in list:
    obj.show_basic_details()
    obj.process_request()
    print("-----------------------")


# output

# Request ID: 101
# Requested by: Felix
# Priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# -----------------------
# Request ID: 102
# Requested by: Arun
# Priority: Medium
# Preparing HR document
# Sending via email
# -----------------------
# Request ID: 103
# Requested by: Arjun
# Priority: High
# Assigning facility staff
# Checking issue
# Job completed
# -----------------------
# Request ID: 104
# Requested by: Akhil
# Priority: Low
# Verifying approval
# Granting software access
# -----------------------


        
        
    