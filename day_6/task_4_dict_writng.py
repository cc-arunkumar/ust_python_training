import csv
employees=[{"id":102,"name":"arumukesh","dept":"IT","salary":45500},
           {"id":102,"name":"arumukesh","dept":"IT","salary":45500},
           {"id":102,"name":"arumukesh","dept":"IT","salary":45500},
           {"id":102,"name":"arumukesh","dept":"IT","salary":45500}]
with open("employee_dict_data.csv","w",newline='') as file:
    header=["id","name","dept","salary"]
    writer=csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    # writing data to the csv file 
    writer.writerows(employees)