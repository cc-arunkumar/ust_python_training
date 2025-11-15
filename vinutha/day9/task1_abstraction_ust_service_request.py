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

# Create an abstract base class called ServiceRequest
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
# Create 4 child classes thatinherit from

# ServiceRequest :

# 1. ITSupportRequest
# Print steps like:
# "Assigning IT engineer"
# "Checking laptop"
# "Issue resolved"
# 2. HRDocumentRequest
# Print:
# "Preparing HR document"
# "Sending via email"
# 3. FacilityRequest
# Abstraction Task 2
# Print:
# "Assigning facility staff"
# "Checking issue"
# "Job completed"
# 4. SoftwareAccessRequest
# Print:
# "Verifying approval"
# "Granting software access"
# Each class must implement its own process_request() .

# Main Program Requirements
# 1. Create at least 4 different request objects (one from each child class).
# 2. Store all objects in a list.
# 3. Loop through the list and call:
# show_basic_details()
# process_request()
# 4. The output should clearly show same method name,
# but different behavior → this proves abstraction + polymorphism.

from abc import ABC, abstractmethod
class ServiceRequest(ABC):
    def __init__(self,request_id,request_by,priority):
        self.request_id=request_id
        self.request_by=request_by
        self.priority=priority
        
    @abstractmethod
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"Request ID : {self.request_id}")
        print(f"Request by : {self.request_by}")
        print(f"priority : {self.priority}")
        
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

class SoftwareAccessRequired(ServiceRequest):
    def process_request(self):
        print("Verifying Approvals")
        print("Granting Software access")
        
req1=ITSupportRequest("R001","Vinnu","High")
req2=HRDocumentRequest("R002","siri","Low")
req3=FacilityRequest("R003","hima","Medium")
req4=SoftwareAccessRequired("R004","Varsha","High")

request=[req1,req2,req3,req4]

for req in request:
    print("\n*** basic Details of employee***")
    req.show_basic_details()
    print("\n***Processing Request***")
    req.process_request()
    

#sample output
# *** basic Details of employee***
# Request ID : R001 
# Request by : Vinnu
# priority : High   

# ***Processing Request***
# Assigning IT engineer
# Checking laptop
# Issue resolved

# *** basic Details of employee***
# Request ID : R002
# Request by : siri
# priority : Low

# ***Processing Request***
# Preparing HR document
# Sending via email

# *** basic Details of employee***
# Request ID : R003
# Request by : hima
# priority : Medium

# ***Processing Request***
# Assigning facility staff
# Checking issue
# Job completed

# *** basic Details of employee***
# Request ID : R004
# Request by : Varsha
# priority : High

# ***Processing Request***
# Verifying Approvals
# Granting Software access