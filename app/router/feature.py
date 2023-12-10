from fastapi import APIRouter

from app.intent_classifier import search
from app.service.job import job_seek
from app.service.pdf import pdf_search
from app.service.video import scrape_video
from app.prediction.career import growth_rate

from app.model import Job,Career,ChatBot

feature_router = APIRouter(tags=["features"])

@feature_router.post("/chat")
async def chatbot(data: ChatBot):
    response = search(data.dict())
    return response

@feature_router.post("/job")
async def job(data: Job):
    job_res = job_seek([data.role,data.location,data.type])
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