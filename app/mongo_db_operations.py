import pymongo

USR = "iNeuron_TEST" # User created by us

# Auto Generated Password or Password set by You
# Update according to your set password for autogenerated password
PWD = "YoUr__PassWord" 

DB_NAME = "iNeuron_AI" # Specifiy a Database Name

# Connection URL
CONNECTION_URL = f"mongodb+srv://{USR}:{PWD}@cluster0.ksto3.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

# Establish a connection with mongoDB
client = pymongo.MongoClient(CONNECTION_URL)

# Create a DB
dataBase = client[DB_NAME]

# Create a Collection Name
COLLECTION_NAME = "iNeuron_Products"
collection = dataBase[COLLECTION_NAME]

# Create a List of Records
list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},
    
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},
    
    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

# insert above records in the collection
rec = collection.insert_many(list_of_records)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")
