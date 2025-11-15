# TASK: UST Service Request Processing
# System
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


from abc import ABC,abstractmethod
class  ServiceRequest():
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
    
    
    def process_request(self):
        pass
    
    
    def show_basic_details(self):
        print(f"Requestid = {self.request_id}")
        print(f"Requestedby = {self.requested_by}")
        print(f"Priority = {self.priority}")
        
        
class  ITSupportRequest(ServiceRequest):
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
            
            
it=ITSupportRequest(101,"Arun","High")
hr=HRDocumentRequest(102,"priya","medium")
facility=FacilityRequest(103,"klaus","Low")
software=SoftwareAccessRequest(104,"jeni","High")

List1=[it,hr,facility,software]

for i in List1:
    i.show_basic_details()
    i.process_request()

# sample output      
# Requestid = 101
# Requestedby = Arun
# Priority = High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# Requestid = 102
# Requestedby = priya
# Priority = medium
# Preparing HR document
# Sending via email
# Requestid = 103
# Requestedby = klaus
# Priority = Low
# Assigning facility staff
# Checking issue
# Job completed
# Requestid = 104
# Requestedby = jeni
# Priority = High
# Verifying approval
# Granting software access