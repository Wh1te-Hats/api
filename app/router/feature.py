from fastapi import APIRouter
import json

from app.intent_classifier import search
from app.service.job import job_seek
from app.service.pdf import pdf_search
from app.service.video import scrape_video
from app.prediction.career import growth_rate
from app.database import rd
from app.service.course import course

from app.model import Job,Career,ChatBot

feature_router = APIRouter(tags=["features"])

@feature_router.post("/chat")
async def chatbot(data: ChatBot):
    response = search(data.dict())
    return response

@feature_router.post("/job")
async def job(data: Job):
    cache_key = f"{data.role}:{data.location}:{data.type}"
    cache = rd.get(cache_key)
    if cache:
        print("HIT")
        return json.loads(cache)
    else:
        job_res = job_seek([data.role,data.location,data.type])
        rd.set(cache_key,json.dumps(job_res))
        rd.expire(cache_key,3600)
    return job_res

@feature_router.post("/career")
async def career(data: Career):
    career_list = growth_rate(data.skill)
    return career_list

@feature_router.post("/document")
async def document(data: str):
    pdf_res = pdf_search(data)
    return {"result": pdf_res}
    
@feature_router.post('/video')
async def document(data: str):
    vid_res = scrape_video(data)
    return {"result": vid_res}

@feature_router.post('/course')
async def course_data(data:str):
    cache_key = f"{data}"
    cache = rd.get(cache_key)
    if cache:
        print("HIT")
        return json.loads(cache)
    else:
        course_result = course(data)
        rd.set(cache_key,json.dumps(course_result))
        rd.expire(cache_key,3600)
        return {"result": course_result}