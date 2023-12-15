from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
AUTHENTICATION_DATABASE_NAME = "Authentication"
AUTHENTICATION_COLLECTION_NAME = "User"


client = MongoClient(MONGO_URI)  
db = client[AUTHENTICATION_DATABASE_NAME]  
collection = db[AUTHENTICATION_COLLECTION_NAME]

import redis

rd = redis.Redis(
  host='apn1-assuring-buffalo-35049.upstash.io',
  port=35049,
  password='b9101fb51c8947d481968bf2d17d6e45'
)