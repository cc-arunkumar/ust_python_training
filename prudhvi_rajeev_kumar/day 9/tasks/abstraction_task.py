# #Question :

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
# Expected Output(sample)
# Request ID: 101
# Requested By: Arun
# Priority: High
# Processing IT Support Request:
# Assigning IT Engineer...
# Checking laptop...
# Abstraction Task 3
# Issue resolved!
# Request ID: 102
# Requested By: Priya
# Priority: Medium
# Processing HR Document Request:
# Preparing document...
# Email sent.
# ...
# Abstraction Task 4

#Adding abstraction to handle different types of service requests
from abc import ABC, abstractmethod

class Service_request(ABC):
    def __init__(self, request_id, requested_by, priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
#The abstract method to be implemented by all subclasses
    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")

# Subclass for IT Support Request
class It_support_request(Service_request):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT engineer...")
        print("Checking laptop...")
        print("Issue resolved!")

# Subclass for HR Document Request
class Hr_document_request(Service_request):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document...")
        print("Sending via email.")

# Subclass for Facility Request
class Faqulty_request(Service_request):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff...")
        print("Checking issue...")
        print("Job completed!")

# Subclass for Software Access Request
class Software_access_request(Service_request):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval...")
        print("Granting software access.")
        
# Creating instances of each service request type
service_list = [
    It_support_request(101, "Rajeev", "High"),
    Hr_document_request(102, "Prudhvi", "Medium"),
    Faqulty_request(103, "Kumar", "Low"),
    Software_access_request(104, "Sneha", "High")
]
# Processing each service request
for request in service_list:
    request.show_basic_details()
    request.process_request()
    print("--------------------------------------")

#Sample Output:
# Request ID: 101
# Requested By: Rajeev
# Priority: High
# Processing IT Support Request:
# Assigning IT engineer...
# Checking laptop...
# Issue resolved!
# --------------------------------------
# Request ID: 102
# Requested By: Prudhvi
# Priority: Medium
# Processing HR Document Request:
# Preparing HR document...
# Sending via email.
# --------------------------------------
# Request ID: 103
# Requested By: Kumar
# Priority: Low
# Processing Facility Request:
# Assigning facility staff...
# Checking issue...
# Job completed!
# --------------------------------------
# Request ID: 104
# Requested By: Sneha
# Priority: High
# Processing Software Access Request:
# Verifying approval...
# Granting software access.
# --------------------------------------