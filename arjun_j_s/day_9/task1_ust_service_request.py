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

class ServiceRequest(ABC):

    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority

    @abstractmethod
    def process_request(self,request_id,requested_by,priority):
        pass

    def show_basic_details(self):
        print(f"Request ID : {self.request_id}")
        print(f"Requested By : {self.requested_by}")
        print(f"Priority : {self.priority}")


class ITSupportRequest(ServiceRequest):

    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)

    def process_request(self):
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")

class HRDocumentRequest(ServiceRequest):

    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)

    def process_request(self):
        print("Preparing HR document")
        print("Sending via email")

class FacilityRequest(ServiceRequest):

    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)

    def process_request(self):
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")

class SoftwareAccessRequest(ServiceRequest):

    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)

    def process_request(self):
        print("Verifying approval")
        print("Granting software access")

t1 = ITSupportRequest(101,"Arjun",1)
t2 = HRDocumentRequest(102,"Rahul",2)
t3 = FacilityRequest(103,"Ravi",1)
t4 = SoftwareAccessRequest(104,"Manu",4)

L=[t1,t2,t3,t4]
for i in L:
    i.show_basic_details()
    i.process_request()

# #Output
# Request ID : 101
# Requested By : Arjun
# Priority : 1
# Assigning IT engineer
# Checking laptop
# Issue resolved
# Request ID : 102
# Requested By : Rahul
# Priority : 2
# Preparing HR document
# Sending via email
# Request ID : 103
# Requested By : Ravi
# Priority : 1
# Assigning facility staff
# Checking issue
# Job completed
# Request ID : 104
# Requested By : Manu
# Priority : 4
# Verifying approval
# Granting software access


    


    