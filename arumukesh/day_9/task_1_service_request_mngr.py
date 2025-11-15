from abc import ABC,abstractmethod
#importing Abstract base Class 
class ServiceRequest(ABC):
    
    def __init__(self,request_id,request_by,priority):
        self.request_id=request_id
        self.request_by=request_by
        self.priority=priority
    def show_basic_details(self):
        print(f"""request_id={self.request_id}
request_by={self.request_by}
priority={self.priority}""")
    @abstractmethod
    def process_request(self):
        pass
# creating child classes that overrrides the process request method
class  ITSupportRequest(ServiceRequest):
    def process_request(self):
        print('''Assigning IT engineer
Checking laptop
Issue resolved''')

class  FacilityRequest(ServiceRequest):
    def process_request(self):
        print('''Assigning facility staff
Checking issue
Job completed
''')
        
class  HRDocumentRequest(ServiceRequest):
    def process_request(self):
        print('''"Preparing HR document
"Sending via email....
''')


class SoftwareAccessRequest(ServiceRequest):
    def process_request(self):
        print('''""Verifying approval
Granting software access
''')
        
# emp1=ITSupportRequest("101","Arun","High")
# emp1.show_basic_details()
# emp1.process_request()
# emp2=ITSupportRequest("101","Arun","High")
# emp2.show_basic_details()
# emp2.process_request()

emp_req=[ITSupportRequest("101","Arun","High"),HRDocumentRequest("101","Arun","High"),SoftwareAccessRequest("103","ajay","low")]
for emp in emp_req:
    try:
        emp.show_basic_details()
        emp.process_request()
    except TypeError:
        print("enter type of request")


# =======Output========
# request_id=101
# request_by=Arun
# priority=High
# Assigning IT engineer
# Checking laptop
# Issue resolved
# request_id=101
# request_by=Arun
# priority=High
# "Preparing HR document
# "Sending via email....