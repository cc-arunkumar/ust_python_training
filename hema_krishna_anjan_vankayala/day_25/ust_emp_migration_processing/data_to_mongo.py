from db_connection import get_connection_mongo

def insert_all_data_mongo(data):
    try:
        collection = get_connection_mongo()
        data = collection.insert_many(data)
        return 'Inserted to Mongo Successfully!'
    except Exception as e:
        return f'Error: {e}'
    