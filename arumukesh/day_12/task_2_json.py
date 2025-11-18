import json
data ='''
'''
python_onj=json.loads(data)
emp_l=python_onj["employees"]
for emp in emp_l:
    print(f"ID:{emp["id"]},name:{emp["name"]}")



print(python_onj)
print(type(python_onj))



b=json.dumps(python_onj,indent=2)
print(b)
print(type(b))