from fastapi import FastAPI

from app.router.auth import auth_router
from app.router.feature import feature_router
from app.router.stream import stream_router
from app.router.aptitude import aptitude_router
from app.router.exams.school import school_exam_router
from app.router.analytics import analytics_router
from app.router.exams.govt import govt_exam_router
from app.router.exams.eng import engineering_exam_router
from app.router.community import community_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(feature_router)
app.include_router(stream_router)
app.include_router(aptitude_router)
app.include_router(school_exam_router)
app.include_router(analytics_router)
app.include_router(govt_exam_router)
app.include_router(engineering_exam_router)
app.include_router(community_router)

# @app.get('/college')
# def college_data():
#     return read_json()







