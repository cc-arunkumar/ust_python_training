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
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
    @abstractmethod
    def process_request(self):
        pass
   
    def show_basic_details(self):
        print(f"request_id: {self.request_id}")
        print(f"request_by: {self.requested_by}")
        print(f"priority: {self.priority}")
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
       
       
       
a1=ITSupportRequest(123,"HR","High")
b1=HRDocumentRequest(420,"IT","low")
c1=FacilityRequest(320,"Managment","low")
d1=SoftwareAccessRequest(455,"security","medium")
 
request=[a1,b1,c1,d1]
 
for requests in request:
    print("....................")
    requests.show_basic_details()
    requests.process_request()

# sample output
# request_id: 123
# request_by: HR
# priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# ....................
# request_id: 420
# request_by: IT
# priority: midium
# Preparing HR document
# Sending via email
# ....................
# request_id: 320
# request_by: Managment
# priority: low
# Assigning facility staff
# Checking issue
# Job completed
# ....................
# request_id: 455
# request_by: security
# priority: High
# Verifying approval
# Granting software access
# PS C:\Users\303462\Downloads\Day9> & C:/Users/303462/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Users/303462/Downloads/Day9/abstraction_task.py
# ....................
# request_id: 123
# request_by: HR
# priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# ....................
# request_id: 420
# request_by: IT
# priority: low
# Preparing HR document
# Sending via email
# ....................
# request_id: 320
# request_by: Managment
# priority: low
# Assigning facility staff
# Checking issue
# Job completed
# ....................
# request_id: 455
# request_by: security
# priority: medium
# Verifying approval
# Granting software access