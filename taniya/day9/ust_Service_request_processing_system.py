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


# Import ABC (Abstract Base Class) and abstractmethod to define abstract classes
from abc import ABC, abstractmethod

# Define an abstract base class ServiceRequest
class ServiceRequest(ABC):
    # Constructor to initialize request details
    def __init__(self, request_id, requested_by, priority):
        self.request_id = request_id      # Unique request ID
        self.requested_by = requested_by  # Employee who raised the request
        self.priority = priority          # Priority level (High/Medium/Low)

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def process_request(self):
        pass

    # Method to show basic request details
    def show_basic_details(self):
        print(f"Request ID : {self.request_id}")
        print(f"Request By : {self.requested_by}")
        print(f"Priroty : {self.priority}")


# Define ITSupportRequest class inheriting from ServiceRequest
class ITSupportRequest(ServiceRequest):
    # Implement process_request method
    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")


# Define HRDocumentRequest class inheriting from ServiceRequest
class HRDocumentRequest(ServiceRequest):
    # Implement process_request method
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")


# Define FacilityRequest class inheriting from ServiceRequest
class FacilityRequest(ServiceRequest):
    # Implement process_request method
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")


# Define SoftwareAccessRequest class inheriting from ServiceRequest
class SoftwareAccessRequest(ServiceRequest):
    # Implement process_request method
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")


# -------------------------------
# Object Creation
# -------------------------------

# Create IT support request
emp1 = ITSupportRequest(101, "Taniya", "High")

# Create HR document request
emp2 = HRDocumentRequest(102, "Prithvi", "Medium")

# Create Facility request
emp3 = FacilityRequest(103, "Rohit", "High")

# Create Software access request
emp4 = SoftwareAccessRequest(104, "Harsh", "Medium")


# -------------------------------
# Processing Requests
# -------------------------------

# Store all requests in a list
show = [emp1, emp2, emp3, emp4]

# Loop through each request and display details + process it
for showing in show:
    showing.show_basic_details()
    showing.process_request()


# -------------------------------
# Expected Output
# -------------------------------
# Request ID : 101
# Request By : Taniya
# Priroty : High
# Assigning IT engineer
# Checking laptop
# Issue resolved
#
# Request ID : 102
# Request By : Prithvi
# Priroty : Medium
# Preparing HR document
# Sending via email
#
# Request ID : 103
# Request By : Rohit
# Priroty : High
# Assigning facility staff
# Checking issue
# Job completed
#
# Request ID : 104
# Request By : Harsh
# Priroty : Medium
# Verifying approval
# Granting software access