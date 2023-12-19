from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
AUTHENTICATION_DATABASE_NAME = "Authentication"
AUTHENTICATION_COLLECTION_NAME = "User"
COMMUNITY_DATABASE_NAME = "Community"
COMMUNITY_COLLECTION_NAME = "communities"
COMMUNITY_USER_DATABASE_NAME = "Community"
COMMUNITY_USER_COLLECTION_NAME = "user"
ANALYTICS_DATABAME_NAME = "Analytics"
ANALYTICS_COLLECTION_NAME = "User"


client = MongoClient(MONGO_URI)  
db = client[AUTHENTICATION_DATABASE_NAME]  
collection = db[AUTHENTICATION_COLLECTION_NAME]

db_community = client[COMMUNITY_DATABASE_NAME]
community_collection = db_community[COMMUNITY_COLLECTION_NAME]

db_authentication = client[COMMUNITY_USER_DATABASE_NAME]
user_collection = db_authentication[COMMUNITY_USER_COLLECTION_NAME]

db_analytics = client[ANALYTICS_DATABAME_NAME]
analytics_collection = db_analytics[ANALYTICS_COLLECTION_NAME]

import redis

rd = redis.Redis(
  host='apn1-assuring-buffalo-35049.upstash.io',
  port=35049,
  password='b9101fb51c8947d481968bf2d17d6e45'
)