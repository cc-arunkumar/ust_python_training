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
# Your Requirements
# �� Create an abstract base class called ServiceRequest
# It must contain:
# 1. A constructor with:
# request_id
# requested_by
# priority
# Abstraction Task 1
# 2. An abstract method:
# process_request()
# Every child class must override this method.
# 3. A normal concrete method:
# show_basic_details()
# Which prints:
# Request ID
# Requested by
# Priority

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
        print("Request ID: ",self.request_id)
        print("Requested by: ",self.requested_by)
        print("Priority: ",self.priority)

#Create 4 child classes thatinherit from
# ServiceRequest :
# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved
class ITSupportRequest(ServiceRequest):
    
    def __init__(self,request_id,requested_by,priority):
        super().__init__(request_id,requested_by,priority)
    
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")
        print()
#2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"

class HRDocumentRequest(ServiceRequest):
    
    def __init__(self,request_id,requested_by,priority):
        super().__init__(request_id,requested_by,priority)
    
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")
        print()
        
# #3. FacilityRequest
# Abstraction Task 2
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"    
class FacilityRequest(ServiceRequest):
    
    def __init__(self,request_id,requested_by,priority):
        super().__init__(request_id,requested_by,priority)
    
    def process_request(self):
        print("Assigning facility staff")
        print("Checking Issue")
        print("Job completed")
        print()
        
# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"
# Each class must implement its own process_request() .   
class SoftwareAcceccRequest(ServiceRequest):
    
    def __init__(self,request_id,requested_by,priority):
        super().__init__(request_id,requested_by,priority)
    
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")
        print()
    
#IT support request object
it1=ITSupportRequest(101,"shyam","High")
it1.show_basic_details()
it1.process_request()

#HR document request object
hr1=HRDocumentRequest(102,"anjan","Low")
hr1.show_basic_details()
hr1.process_request()

#Facility Request object
fr1=FacilityRequest(103,"Arun","Medium")
fr1.show_basic_details()
fr1.process_request()

#Software Access Request object
sar1=SoftwareAcceccRequest(104,"felix","Low")
sar1.show_basic_details()
sar1.process_request()

#Sample output
# Request ID:  101
# Requested by:  shyam
# Priority:  High
# Assigning IT engineer
# Checking laptop
# Issue resolved

# Request ID:  102
# Requested by:  anjan
# Priority:  Low
# Preparing HR document
# Sending via email

# Request ID:  103
# Requested by:  Arun
# Priority:  Medium
# Assigning facility staff
# Checking Issue
# Job completed

# Request ID:  104
# Requested by:  felix
# Priority:  Low
# Verifying approval
# Granting software access