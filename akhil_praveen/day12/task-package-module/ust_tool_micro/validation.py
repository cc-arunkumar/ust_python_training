from .exception import BlankFieldError

def  to_int(value):
    int(value)

def required_fields(row,header):
    required = [ "order_id" , "item_id" , "quantity" ]
    for i in required:
        if i not in row:
            raise BlankFieldError(row[header[0]],i)
        else:
            if i == header[header[2]]:
                to_int(row[header[2]])
            return True
             
             