from fastapi import APIRouter
from pymongo import MongoClient

from app.database import MONGO_URI

stream_router = APIRouter(tags=["stream"])

@stream_router.get("/stream/{stream}")
async def stream(stream:str):
    client = MongoClient(MONGO_URI)
    if stream == 'arts':  
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

    elif stream == 'commerce':
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
            
    elif stream == 'pcb':
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

    elif stream == 'pcm':
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
            
    elif stream == 'pcmb':
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



@stream_router.get("/college/{college_type}")
async def college(college_type:str):
    client = MongoClient(MONGO_URI)
    if college_type == 'engineering':  
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

    elif college_type == 'architecture':
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

    elif college_type == 'bcom':
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
    
    elif college_type == 'mass_media':
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

    elif college_type == 'law':
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

    elif college_type == 'mba':
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
    elif college_type == 'mbbs':
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

    elif college_type == 'science':
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
