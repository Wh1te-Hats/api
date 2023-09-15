from fastapi import FastAPI, Request
from app.model import UserRegister, UserLogin, Job,Aptitude
from fastapi import HTTPException
from pymongo import MongoClient
import secrets


from app.intent_classifier import search
from app.service.job import job_seek
from app.service.pdf import pdf_search
from app.service.video import scrape_video

from app.aptitude.generalApt.logicalReasoning import logical_aptitude

app = FastAPI()

MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
AUTHENTICATION_DATABASE_NAME = "Authentication"
AUTHENTICATION_COLLECTION_NAME = "User"


client = MongoClient(MONGO_URI)  
db = client[AUTHENTICATION_DATABASE_NAME]  
collection = db[AUTHENTICATION_COLLECTION_NAME]

@app.post("/register")
async def register_user(user: UserRegister):
    # Check if the username already exists
    if collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    # Insert the user into the MongoDB collection and generate a random ID
    user_dict = user.dict()
    user_dict["user_id"] = secrets.token_hex(16)
    collection.insert_one(user_dict)
    return {"message": "User registered successfully", "user_id": user_dict["user_id"]}

@app.post("/login")
async def login_user(user: UserLogin):
    stored_user = collection.find_one({"username": user.username})
    
    if stored_user is None or stored_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": stored_user["_id"]}

@app.post("/chat")
async def chatbot(request: Request):
    data = await request.json()
    response = search(data)
    return response

@app.post("/job")
async def job(data: Job):
    job_res = job_seek([data.role,data.location,data.type])
    return {"message": job_res}

@app.post("/document")
async def document(data: str):
    pdf_res = pdf_search(data)
    return {"message": pdf_res,"flow": "EMPTY","num":-1}
    
@app.post('/video')
async def document(data: str):
    vid_res = scrape_video(data)
    return {"message": vid_res,"flow": "EMPTY","num":-1}

@app.post('/aptitude')
async def general_aptitude(data: Aptitude):
    if (data.type).lower() == 'general':

        if (data.topic).lower() == 'logical reasoning':
            response = logical_aptitude()

        
            
    return response
