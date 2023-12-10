from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
AUTHENTICATION_DATABASE_NAME = "Authentication"
AUTHENTICATION_COLLECTION_NAME = "User"


client = MongoClient(MONGO_URI)  
db = client[AUTHENTICATION_DATABASE_NAME]  
collection = db[AUTHENTICATION_COLLECTION_NAME]