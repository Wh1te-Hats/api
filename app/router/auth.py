from fastapi import APIRouter, Request
from app.model import UserRegister, UserLogin
from app.database import collection
from fastapi import HTTPException
import secrets

auth_router = APIRouter(tags=["authentication"])

@auth_router.post("/register")
async def register_user(user: UserRegister):
    # Check if the username already exists
    if collection.find_one({"username": user.name}):
        raise HTTPException(status_code=400, detail="Username already taken")
    # Insert the user into the MongoDB collection and generate a random ID
    user_dict = user.dict()
    print(user_dict)
    print(collection.insert_one(user_dict))
    print("User registered successfully")
    return {"message": "User registered successfully", "id": user_dict["id"]}

@auth_router.post("/login")
async def login_user(user: UserLogin):
    stored_user = collection.find_one({"username": user.username})
    
    if stored_user is None or stored_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": stored_user["_id"]}

@auth_router.get("/info/{user_id}")
async def get_info(user_id):
    stored_user = collection.find_one({"id": user_id})
    print(stored_user)
    return
