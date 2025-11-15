
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
#  UST wants to build a Service Request Processing System

# Main Program Requirements
#  Create at least 4 different request objects (one from each child class).
#  Store all objects in a list.
#  Loop through the list and call:
#  show_basic_details()
#  process_request()
#  The output should clearly show same method name,
#  but different behavior → this proves abstraction + polymorphism.




#importing abstract class
from abc import ABC,abstractmethod

#creating a abstract class 
class ServiceRequest(ABC):
    #initialising a constructor
    def __init__(self,request_id,requested_by,priority):
        self.request_id=request_id
        self.requested_by=requested_by
        self.priority=priority
    
    #defining a abstract method
    @abstractmethod
    def process_request(self):
       pass
    
    #defining a concrete method
    def show_basic_details(self):
        print(f"Request Id: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")
    
#child class

class ITSupportDesk(ServiceRequest):
    #using abstract method
    
    def process_request(self):
        print("Assigning IT Operator")
        print("Checking Laptop")
        print("Issue Resolved")

#child class

class HRDocumentRequest(ServiceRequest):
    #using abstract method
    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")

#child class

class FacilityRequest(ServiceRequest):
    #using abstract method
    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")

#child class

class SoftwareAccessRequest(ServiceRequest):
    #using abstract method
    def process_request(self):
        print("Verifying approval")
        print("Granting software access")

#creating objects for all subclasses
it=ITSupportDesk(101,"Deva","High")
hr=HRDocumentRequest(102,"Asutosh","Medium")
fr=FacilityRequest(103,"Walter White","Low")
sr=SoftwareAccessRequest(104,"Heisenberg","High")

#storing the objects in a list
li=[it,hr,fr,sr]

#looping through the objects and accessig methods

for i in li:
    i.show_basic_details()
    i.process_request()
    print("----------------------------")
        



#Sample output

# Request Id: 101
# Requested By: Deva
# Priority: High
# Assigning IT Operator
# Checking Laptop
# Issue Resolved
# ----------------------------
# Request Id: 102
# Requested By: Asutosh
# Priority: Medium
# Preparing HR document
# Sending via email
# ----------------------------
# Request Id: 103
# Requested By: Walter White
# Priority: Low
# Assigning facility staff
# Checking issue
# Job completed
# ----------------------------
# Request Id: 104
# Requested By: Heisenberg
# Priority: High
# Verifying approval
# Granting software access
# ----------------------------