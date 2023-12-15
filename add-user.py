from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
COMMUNITY_DATABASE_NAME = "Community"
COMMUNITY_COLLECTION_NAME = "communities"
AUTHENTICATION_DATABASE_NAME = "Community"
AUTHENTICATION_COLLECTION_NAME = "user"

def get_community_id(state, career_goal, community_collection):
    community = community_collection.find_one({"state": state, "career_goal": career_goal})
    return community["community_id"] if community else None

def create_community(state, career_goal, community_id):
    community = {
        "community_id": community_id,
        "state": state,
        "career_goal": career_goal,
        "members": []
    }
    return community

def add_community_to_mongodb(community, community_collection):
    community_collection.insert_one(community)

def update_community_members(community_id, user_id, community_collection):
    community_collection.update_one(
        {"community_id": community_id},
        {"$push": {"members": user_id}}
    )

def add_user_to_mongodb(user, user_collection, community_collection):
    state = user["state"]
    career_goal = user["career_goal"]

    # Get community_id based on state and career goal
    community_id = get_community_id(state, career_goal, community_collection)

    if community_id is not None:
        new_user = {
            "name": user["name"],
            "city": user["city"],
            "state": state,
            "school/college": user["school/college"],
            "career_goal": career_goal,
            "community_id": community_id
        }

        # Add the new user to the User collection
        result = user_collection.insert_one(new_user)

        # Update the members list in the corresponding community
        update_community_members(community_id, result.inserted_id, community_collection)
    else:
        # If no matching community is found, create a new one
        new_community_id = community_collection.count_documents({}) + 1
        new_community = create_community(state, career_goal, new_community_id)
        add_community_to_mongodb(new_community, community_collection)

        # Now get the community_id for the newly created community
        community_id = get_community_id(state, career_goal, community_collection)

        # Add the new user to the User collection with the appropriate community_id
        new_user = {
            "name": user["name"],
            "city": user["city"],
            "state": state,
            "school/college": user["school/college"],
            "career_goal": career_goal,
            "community_id": community_id
        }
        result = user_collection.insert_one(new_user)

        # Update the members list in the corresponding community
        update_community_members(community_id, result.inserted_id, community_collection)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db_community = client[COMMUNITY_DATABASE_NAME]
community_collection = db_community[COMMUNITY_COLLECTION_NAME]

db_authentication = client[AUTHENTICATION_DATABASE_NAME]
user_collection = db_authentication[AUTHENTICATION_COLLECTION_NAME]

# Example new user data
new_user_data = {
    "name": "Harshil",
    "city": "New York",
    "state": "NY",
    "school/college": "harvard",
    "career_goal": "Engineer",
}

# Add the new user to the User collection with the appropriate community_id
add_user_to_mongodb(new_user_data, user_collection, community_collection)
