import csv
path="C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day12/data/orders.csv"
def read_csv(path):
    rows = []
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return None 
    return rows


def write_csv(path,orders,headers):
    with open(path,mode="w")as file:
        csv_writter=csv.DictWriter(file,fieldnames=headers)
        csv_writter.writeheader()
        for row in orders:
            csv_writter.writerow(row)
    
