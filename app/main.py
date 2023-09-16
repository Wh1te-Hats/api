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
from app.analytics.aptitude_analytic import analytics
from app.helper import read_json

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
    return career_list

@app.post("/document")
async def document(data: str):
    pdf_res = pdf_search(data)
    return {"result": pdf_res}
    
@app.post('/video')
async def document(data: str):
    vid_res = scrape_video(data)
    return {"result": vid_res}


@app.get("/stream/arts")
async def arts():
    client = MongoClient(MONGO_URI)  
    db = client["stream"]  
    collection = db["arts"]
    results = collection.find()
    data = []
    for document in results:
        data.append(
            {    
            "course name": document["course name"],
            "course description": document["course description"],
            "course duration": document["course duration"],
            "career opportunities": document["career opportunities"],
            "eligibility requirements": document["eligibility requirements"],
            "course curriculum": document["course curriculum"],
            "course structure": document["course structure"]
            }
        )
    
    return data

@app.get("/stream/commerce")
async def commerce():
    client = MongoClient(MONGO_URI)  
    db = client["stream"]  
    collection = db["commerce"]
    results = collection.find()
    data = []
    for document in results:
        data.append(
            {    
            "course name": document["course name"],
            "course description": document["course description"],
            "course duration": document["course duration"],
            "career opportunities": document["career opportunities"],
            "eligibility requirements": document["eligibility requirements"],
            "course curriculum": document["course curriculum"],
            "course structure": document["course structure"]
            }
        )
    
    return data

@app.get("/stream/pcb")
async def pcb():
    client = MongoClient(MONGO_URI)  
    db = client["stream"]  
    collection = db["pcb"]
    results = collection.find()
    data = []
    for document in results:
        data.append(
            {    
            "course name": document["course name"],
            "course description": document["course description"],
            "course duration": document["course duration"],
            "career opportunities": document["career opportunities"],
            "eligibility requirements": document["eligibility requirements"],
            "course curriculum": document["course curriculum"],
            "course structure": document["course structure"]
            }
        )
    
    return data

@app.get("/stream/pcm")
async def pcm():
    client = MongoClient(MONGO_URI)  
    db = client["stream"]  
    collection = db["pcm"]
    results = collection.find()
    data = []
    for document in results:
        data.append(
            {    
            "course name": document["course name"],
            "course description": document["course description"],
            "course duration": document["course duration"],
            "career opportunities": document["career opportunities"],
            "eligibility requirements": document["eligibility requirements"],
            "course curriculum": document["course curriculum"],
            "course structure": document["course structure"]
            }
        )
    
    return data

@app.get("/stream/pcmb")
async def pcmb():
    client = MongoClient(MONGO_URI)  
    db = client["stream"]  
    collection = db["pcmb"]
    results = collection.find()
    data = []
    for document in results:
        data.append(
            {    
            "course name": document["course name"],
            "course description": document["course description"],
            "course duration": document["course duration"],
            "career opportunities": document["career opportunities"],
            "eligibility requirements": document["eligibility requirements"],
            "course curriculum": document["course curriculum"],
            "course structure": document["course structure"]
            }
        )
    
    return data

@app.get("/college/engineering")
async def engineering():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["engineering colleges"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("college_nirf", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("average_package", "")
    }
)
    
    return data

@app.get("/college/architecture")
async def engineering():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["Architecture"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/bcom")
async def engineering():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["BCom"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/mass_media")
async def law():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["mass_media"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/law")
async def law():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["law"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/mba")
async def mba():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["mba"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_icon", ""),
        "fees": document.get("fees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/mbbs")
async def mbbs():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["mbbs"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_img", ""),
        "fees": document.get("FirstYearFees", ""),
        "duration": document.get("duration", ""),
        "exam": document.get("exam", ""),
        "eligibility": document.get("eligibility", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get("/college/science")
async def mbbs():
    client = MongoClient(MONGO_URI)  
    db = client["pragati"]  
    collection = db["science"]
    results = collection.find()
    data = []
    for document in results[:10]:
        
        data.append(
    {
        "college_name": document.get("college_name", ""),
        "college_icon": document.get("college_img", ""),
        "fees": document.get("fees1", ""),
        "duration": document.get("duration1", ""),
        "exam": document.get("exams1", ""),
        "eligibility": document.get("eligibility1", ""),
        "college_nirf": document.get("rank", ""),
        "highest_package": document.get("highest_package", ""),
        "average_package": document.get("salary", "")
    }
)
    
    return data

@app.get('/college')
def college_data():
    return read_json()


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


    # analytics(response,topic,data)

    return response["question"]

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
    return response

@app.post('/aptitude/course/medical')
async def medical_aptitude(data: Course):
    if (data.subject).lower() == 'bio_chem':
        response = bio_chem_aptitude()
    if (data.subject).lower() == 'bio_tech':
        response = bio_tech_aptitude()
    if (data.subject).lower() == 'micro_bio':
        response = micro_bio_aptitude()

    return response
