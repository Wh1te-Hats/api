from fastapi import APIRouter

from app.model import Exam, Interest

analytics_router = APIRouter(tags=["Analytics"],prefix="/analytics")

analytics_router.post('/exam')
def exam_analytics(exam_data: Exam):
    '''
    Store in MongoDB 
    - total time of the exam in type ,subtype and overall
    - total score of the exam in type ,subtype and overall
    - total incorrect of the exam in type ,subtype and overall
    - total correct of the exam in type ,subtype and overall
    - sort the data passed in the forntend in a list of json object
    - total exam taken in type ,subtype and overall
    '''
    pass


analytics_router.get('/exam_details/{user_id}')
def exam_details(user_id:str):
    '''
    Give dashboard analytics
    Display
    - Total Time Taken of Exam Overall
    - Total Exam Taken Overall
    Graph (General, Course, Career)
    - Show Avg percentage of all the subtype in the particular apititude type
    '''
    pass

analytics_router.post('/interest')
def interested_job(data: Interest):
    '''
    - collect the user skills 
    - collect the job skills
    - find the skills required to learn by the user
    - store the interested job, user skills in a list
    '''
    pass