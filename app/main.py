from fastapi import FastAPI, Request
from app.model import UserRegister, UserLogin, Job, General, Course,Career 
from fastapi import HTTPException
from pymongo import MongoClient
import secrets


from app.intent_classifier import search
from app.service.job import job_seek
from app.service.pdf import pdf_search
from app.service.video import scrape_video
from app.prediction.career import growth_rate

from app.aptitude.generalApt.logicalReasoning import logical_aptitude
from app.aptitude.generalApt.verbalAbilityApt import aptitude as verbal_ability_aptitude
from app.aptitude.generalApt.verbalReasoningApt import aptitude as verbal_reasoning_aptitude
from app.aptitude.generalApt.arithmeticApt import aptitude as arithmetic_aptitude
from app.aptitude.generalApt.generalKnowledgeApt import aptitude as general_knowledge_aptitude
from app.aptitude.generalApt.verbalReasoningApt import aptitude as non_verbal_reasoning_aptitude

from app.aptitude.courseBased.engineering.chemical import aptitude as chemical_aptitude
from app.aptitude.courseBased.engineering.civil import aptitude as civil_aptitude
from app.aptitude.courseBased.engineering.cse import aptitude as cse_aptitude
from app.aptitude.courseBased.engineering.ece import aptitude as ece_aptitude
from app.aptitude.courseBased.engineering.eee import aptitude as eee_aptitude
from app.aptitude.courseBased.engineering.mechanical import aptitude as mechanical_aptitude

from app.aptitude.courseBased.medical.bioChemical import aptitude as bio_chem_aptitude
from app.aptitude.courseBased.medical.biotech import aptitude as bio_tech_aptitude
from app.aptitude.courseBased.medical.microBiology import aptitude as micro_bio_aptitude

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
    return {"result": job_res}

@app.post("/career")
async def career(data: Career):
    career_list = growth_rate(data.skill)
    return {"result":career_list}

@app.post("/document")
async def document(data: str):
    pdf_res = pdf_search(data)
    return {"result": pdf_res}
    
@app.post('/video')
async def document(data: str):
    vid_res = scrape_video(data)
    return {"result": vid_res}

@app.post('/aptitude/general')
async def general_aptitude(data: General):

    if (data.topic).lower() == 'logical reasoning':
        response = logical_aptitude()
    if (data.topic).lower() == 'verbal ability':
        response = verbal_ability_aptitude()
    if (data.topic).lower() == 'verbal reasoning':
        response = verbal_reasoning_aptitude()
    if (data.topic).lower() == 'arithmetic':
        response = arithmetic_aptitude()
    if (data.topic).lower() == 'general knowledge':
        response = general_knowledge_aptitude()
    if (data.topic).lower() == 'non verbal reasoning':
        response = non_verbal_reasoning_aptitude()

@app.post('/aptitude/course/engineering')
async def course_aptitude(data: Course):
    if (data.subject).lower() == 'chemical':
        response = chemical_aptitude()
    if (data.subject).lower() == 'civil':
        response = civil_aptitude()
    if (data.subject).lower() == 'cse':
        response = cse_aptitude()
    if (data.subject).lower() == 'ece':
        response = ece_aptitude()
    if (data.subject).lower() == 'eee':
        response = eee_aptitude()
    if (data.subject).lower() == 'mechanical':
        response = mechanical_aptitude()

@app.post('/aptitude/course/medical')
async def medical_aptitude(data: Course):
    if (data.subject).lower() == 'bio_chem':
        response = bio_chem_aptitude()
    if (data.subject).lower() == 'bio_tech':
        response = bio_tech_aptitude()
    if (data.subject).lower() == 'micro_bio':
        response = micro_bio_aptitude()

    return response
