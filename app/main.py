from fastapi import FastAPI

from app.router.auth import auth_router
from app.router.feature import feature_router
from app.router.stream import stream_router
from app.router.aptitude import aptitude_router
from app.router.exam import exam_router

from app.analytics.aptitude_analytic import analytics

app = FastAPI()

app.include_router(auth_router)
app.include_router(feature_router)
app.include_router(stream_router)
app.include_router(aptitude_router)
app.include_router(exam_router)

# @app.get('/college')
# def college_data():
#     return read_json()






