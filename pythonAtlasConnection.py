from pymongo import MongoClient, collection

client = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@<YOUR-CLUSTOR>.jqndj.mongodb.net/<DATABASE>?retryWrites=true&w=majority")

db = client["DATABASE"]
col = db["COLLECTION"]

# Insert one document into collection
col.insert_one({'name': 'TRUMP'})
                
# Insert many documents into collection
col.insert_many({})

# Delete all
col.delete_many({})
