def add_new_field(data):
    for emp in data:
        if emp["age"]<25:
            emp["category"]="Fresher"
        else:
            emp["category"]="Experienced"
    return data