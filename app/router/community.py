from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database import collection,community_collection

community_router = APIRouter(tags=['Community'],prefix='/community')

def get_community_id(state, career_goal, community_collection):
    community_list = []
    for career in career_goal:
        community = community_collection.find_one({"state": state, "career_goal": career})
        community_list.add(community) if community else community.append(None)
    return community_list

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
        {"$push": {"members": user_id}})

@community_router.post('/add/{user_id}')
def add_user_to_community(user_id:str):
    community = collection.find_one({"id": user_id})
    state=  community.get("state"),
    career_goal = community.get("career_goal")
    id = community.get("id")
 
    community_id_list = get_community_id(state, career_goal, community_collection)

    for index,community_id in enumerate(community_id_list):
        if community_id is not None:
            update_community_members(community_id, id, community_collection)
        else:
            new_community_id = community_collection.count_documents({}) + 1
            new_community = create_community(state, career_goal, new_community_id)
            add_community_to_mongodb(new_community, community_collection)

            # Now get the community_id for the newly created community
            community_id = community_collection.find_one({"state": state, "career_goal": career_goal[index]})
            update_community_members(community_id, id, community_collection)

    return JSONResponse(content={"message": "user is added"}, media_type="application/json")

@community_router.get('/user/{user_id}')
def user_info(user_id:str):
    communities = community_collection.find({"members": user_id})
    
    community_data = []
    for community in communities:
        data = {
            "title": community.get("career_goal"),
            "member": str(len(community.get("members")))
        }
        community_data.append(data)
    
    return JSONResponse(content=community_data, media_type="application/json")

