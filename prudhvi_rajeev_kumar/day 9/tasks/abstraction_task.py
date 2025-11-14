
from abc import ABC, abstractmethod

class Service_request(ABC):
    def __init__(self, request_id, requested_by, priority):
        self.request_id = request_id
        self.requested_by = requested_by
        self.priority = priority
#what is an exception : 

    @abstractmethod
    def process_request(self):
        pass

    def show_basic_details(self):
        print(f"Request ID: {self.request_id}")
        print(f"Requested By: {self.requested_by}")
        print(f"Priority: {self.priority}")


class It_support_request(Service_request):
    def process_request(self):
        print("Processing IT Support Request:")
        print("Assigning IT engineer...")
        print("Checking laptop...")
        print("Issue resolved!")


class Hr_document_request(Service_request):
    def process_request(self):
        print("Processing HR Document Request:")
        print("Preparing HR document...")
        print("Sending via email.")


class Faqulty_request(Service_request):
    def process_request(self):
        print("Processing Facility Request:")
        print("Assigning facility staff...")
        print("Checking issue...")
        print("Job completed!")


class Software_access_request(Service_request):
    def process_request(self):
        print("Processing Software Access Request:")
        print("Verifying approval...")
        print("Granting software access.")

service_list = [
    It_support_request(101, "Rajeev", "High"),
    Hr_document_request(102, "Prudhvi", "Medium"),
    Faqulty_request(103, "Kumar", "Low"),
    Software_access_request(104, "Sneha", "High")
]

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