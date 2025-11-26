import csv
import re
def vendor_master_validation(row,header):
    
    valid_cities = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Surat", "Ahmedabad", "Pune", "Kanpur",
    "Jaipur", "Navi Mumbai", "Lucknow", "Nagpur", "Indore", "Kallakurichi", "Patna", "Bhopal", "Ludhiana", "Tirunelveli",
    "Agra", "Vadodara", "Rajkot", "Najafgarh", "Jamshedpur", "Gorakhpur", "Nashik", "Pimpri", "Kalyan", "Thane",
    "Meerut", "Nowrangapur", "Faridabad", "Ghaziabad", "Dhanbad", "Dombivli", "Varanasi", "Vijayawada", "Ranchi", "Amritsar",
    "Allahabad", "Visakhapatnam", "Jabalpur", "Howrah", "Aurangabad", "Shivaji Nagar", "Solapur", "Srinagar", "Guwahati", "Chandigarh",
    "Coimbatore", "Jodhpur", "Madurai", "Gwalior", "Mysore", "Rohini", "Hubli", "Narela", "Jalandhar", "Trivandrum",
    "Salem", "Tiruchi", "Kota", "Bhubaneswar", "Aligarh", "Bareilly", "Moradabad", "Bhiwandi", "Raipur", "Gorakhpur",
    "Bhilai", "Borivali", "Kochi", "Amravati", "Sangli", "Cuttack", "Bikaner", "Bokaro Steel City", "Warangal", "Bhavnagar",
    "Nanded", "Raurkela", "Guntur", "Dehra Dun", "Bhayandar", "Durgapur", "Ajmer", "Ulhasnagar", "Kolhapur", "Siliguri",
    "Bilimora", "Karol Bagh", "Asansol", "Jamnagar", "Saharanpur", "Gulbarga", "Bhatpara", "Jammu", "Kurnool", "Ujjain"]
    try:
        if re.match(row[header[1]],r'^[A-Za-z]+(?: [A-Za-z]+)*$'):
            return False
        # if not row[header[2]].isalpha():
        #     return False
        # if len(str(row[header[3]]))!=10:
        #     return False
        # if len(str(row[header[4]]))!=16:
        #     return False
        # if len(str(row[header[5]]))!=10:
        #     return False
        # if "@" not in row[header[6]] or not row[header[6]].endswith(".com"):
        #     return False
        # if len(str(row[header[7]]))>200:
        #     return False
        # if row[header[8]] not in valid_cities:
        #     return False
        # if row[header[9]] not in["Active","Inactive"]:
            return False
        return True
    except Exception :
        return False
    
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/vendor_master.csv","r") as file01:
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/vendor_master_final.csv","w") as file02:
        vendor_file = csv.DictReader(file01)
        header = vendor_file.fieldnames
        final_file = csv.DictWriter(file02,fieldnames=header)
        final_file.writeheader()
        for row in vendor_file:
            condition = vendor_master_validation(row,header)
            print(condition)
            if not condition:
                final_file.writerow(row)