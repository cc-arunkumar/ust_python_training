# Abstraction Task
# TASK: UST Service Request Processing System

#requirments
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
# # Which prints:
# # Request ID
# # Requested by

# Create 4 child classes that inherit from
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

# Abstract Base Class
class ServiceRequest(ABC):
    def __init__(self, request_id, requested_by, priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority

    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")


# Child Classes

class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT Engineer...")
        print("Checking laptop...")
        print("Issue resolved!\n")


class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document...")
        print("Sending via email...\n")


class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff...")
        print("Checking issue...")
        print("Job completed!\n")


class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval...")
        print("Granting software access...\n")


# Main Program 
req1 = ITSupportRequest(101, "Bhargavi", "High")
req2 = HRDocumentRequest(102, "Meena", "Medium")
req3 = FacilityRequest(103, "chinnu", "Low")
req4 = SoftwareAccessRequest(104, "Shero", "High")

#requests into the list
requests = [req1, req2, req3, req4]

for req in requests:
    req.show_basic_details()
    req.process_request()


#output
# Request ID: 101
# Requested By: Bhargavi        
# Priority: High
# Processing IT Support Request:
# Assigning IT Engineer...      
# Checking laptop...
# Issue resolved!

# Request ID: 102
# Requested By: Meena
# Priority: Medium
# Processing HR Document Request:
# Preparing HR document...
# Sending via email...

# Request ID: 103
# Requested By: chinnu
# Priority: Low
# Processing Facility Request:
# Assigning facility staff...
# Checking issue...
# Job completed!

# Request ID: 104
# Requested By: Shero
# Priority: High
# Processing Software Access Request:
# Verifying approval...
# Granting software access...