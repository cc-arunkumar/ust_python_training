def division(a,b):
    try:
        print(f"multiplication:{a*b}")
        print(f"subtract:{a-b}")
        print(f"add :{a+b}")
        print(f"divison:{a/b}")
    except ZeroDivisionError as zde:
        print(f"Division operation has error {zde}")
    except Exception as e:
        print("Exxception is {e}")
   
      
division(2,0)
#sample execution
# multiplication:0
# subtract:2
# add :2
# Division operation has error division by zero