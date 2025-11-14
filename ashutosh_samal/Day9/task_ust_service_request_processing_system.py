from abc import ABC, abstractmethod
#service request class created
class ServiceRequest(ABC):
    def __init__(self,request_id,requested_by,priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
    
    #abstract method created
    @abstractmethod
    def process_request(self):
        pass
    
    #function to print basic details
    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested by: {self.requested_by}")
        print(f"Priority: {self.priority}")

#class IT support inherited from servive request        
class ITSupportRequest(ServiceRequest):
    def process_request(self):
        print("Assigning IT engineer \nChecking laptop \nIssue resolved")

#class HR Document inherited from servive request        
class HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print("Preparing HR document \nSending via email")

#class facility request inherited from service request
class FacilityRequest(ServiceRequest):
    def process_request(self):
        print("Assigning facility staff \nChecking issue \nJob completed")

#class software accesss inherited from service request        
class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print("Verifying approval \nGranting software access")

#object creation
it1 = ITSupportRequest("IT101","Niel","High")
hr1 = HRDocumentRequest("HR111","Nitin","Medium")
fr1 = FacilityRequest("FR420","Mukesh","Medium")
sa1 = SoftwareAccessRequest("SA250","Deva","High")

#list to store object
list = [it1,hr1,fr1,sa1]

#loop to iterate the list and calling the function
for i in list:
    i.show_basic_details()
    i.process_request()
    print("========================")
    


#Sample Execution
# Request ID: IT101
# Requested by: Niel
# Priority: High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# ========================
# Request ID: HR111
# Requested by: Nitin
# Priority: Medium
# Preparing HR document
# Sending via email
# ========================
# Request ID: FR420
# Requested by: Mukesh
# Priority: Medium
# Assigning facility staff
# Checking issue
# Job completed
# ========================
# Request ID: SA250
# Requested by: Deva
# Priority: High
# Verifying approval
# Granting software access
# ========================