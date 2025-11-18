from .exception import BlankFieldError

def  to_int(value):
    int(value)

def required_fields(row,header):
    for i in header:
        if i not in row:
                raise BlankFieldError(row[header[0]],i)
        else:
            if i == row[header[2]]:
                to_int(row[header[2]])
            return True
             
             