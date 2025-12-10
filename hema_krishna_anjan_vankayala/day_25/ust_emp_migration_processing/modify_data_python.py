
def modify_data(row):
    if row['age']>25:
        row['category'] = "Experienced"
    else:
        row['category'] = "Fresher"
    
    return row