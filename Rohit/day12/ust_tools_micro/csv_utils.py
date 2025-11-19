import csv

def write_csv(path:str, data:list[dict[str,str]],headers: list[str])->None:
    
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        if not data:
            return 

        # fieldnames = data[0].keys()
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writerows(data)

def read_csv(path:str)->list[dict[str,str]]:
    # """Reads a CSV file and returns a list of dictionaries representing each row.

    # Args:
    #     path (str): The file path to the CSV file.
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        write_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\inventory.csv",data,headers=['item_id','available_stock'])
        return data

read_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\order.csv")

