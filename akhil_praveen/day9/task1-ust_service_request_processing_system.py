from abc import ABC,abstractmethod

#class with abstract method
class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by  = requested_by
        self.priority = priority
    @abstractmethod
    def process_request(self):
        pass
    
    def show_basic_details(self):
        print(f"Request id : ",self.request_id)
        print(f"Requested by : ",self.requested_by)
        print(f"Priority : ",self.priority)
        
# inherting abstract class
class ITSupportRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)
    
    def process_request(self):
        print("Processing ITSupportRequest")
        print("Assigning IT engineer")
        print("Checking laptop")
        print("Issue resolved")
        print("")
        

# inherting abstract class
class HRDocumentRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)
    
    def process_request(self):
        print("Processing HRDocumentRequest")
        print("Preparing HR document")
        print("Sending via email")
        print("")


# inherting abstract class
class FacilityRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)
    
    def process_request(self):
        print("Processing FacilityRequest")
        print("Assigning facility staff")
        print("Checking issue")
        print("Job completed")
        print("")


# inherting abstract class
class SoftwareAccessRequest(ServiceRequest):
    def __init__(self, request_id, requested_by, priority):
        super().__init__(request_id, requested_by, priority)
    
    def process_request(self):
        print("Processing SoftwareAccessRequest")
        print("Verifying approval")
        print("Granting software access")
        print("")
        
it1 = ITSupportRequest(101,"Akhil","High")

hr1 = HRDocumentRequest(102,"Arjun","Medium")

fr1 = FacilityRequest(103,"Felix","Low")

sar1 = SoftwareAccessRequest(104,"Arun","Medium")

service_req = [it1,hr1,fr1,sar1]

for i in service_req:
    i.show_basic_details()
    i.process_request()



# Output
# Request id :  101
# Requested by :  Akhil
# Priority :  High
# Processing ITSupportRequest
# Assigning IT engineer
# Checking laptop
# Issue resolved

# Request id :  102
# Requested by :  Arjun
# Priority :  Medium
# Processing HRDocumentRequest
# Preparing HR document
# Sending via email

# Request id :  103
# Requested by :  Felix
# Priority :  Low
# Processing FacilityRequest
# Assigning facility staff
# Checking issue
# Job completed

# Request id :  104
# Requested by :  Arun
# Priority :  Medium
# Processing SoftwareAccessRequest
# Verifying approval
# Granting software access