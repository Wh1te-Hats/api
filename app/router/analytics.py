from fastapi import APIRouter

from app.model import Exam, Interest
from app.database import analytics_collection

analytics_router = APIRouter(tags=["Analytics"],prefix="/analytics")

def update_analytics(data:Exam):
    user_id = data.user_id
    type = data.type
    subtype = data.subtype

    # Retrieve existing data or create a new document if not exists
    user_data = analytics_collection.find_one({"user_id": user_id})
    if user_data is None:
        user_data = {
            "user_id": user_id,
            "history": [],
            "total_time_spent": 0
        }

    # Update history with new data
    history_entry = {
        f"{type}": [{
            f"{subtype}": [{
                "data": data.date,
                "total_time": data.total_time,
                "score": data.score,
                "incorrect": data.incorrect,
                "correct": data.correct
            }],
            "avg_score": ""
        }],
        "avg_score": ""
    }

    user_data["history"].append(history_entry)
    user_data["total_time_spent"] += data.total_time

    # Calculate average score for the user
    total_score = 0
    total_entries = 0

    for i ,exam_type in enumerate(user_data["history"]):
        
        for j ,exam_subtype in enumerate(exam_type[f"{type}"]):
            
            for exam_data in exam_subtype[f"{subtype}"]:
                
                total_score += exam_data["score"]
                total_entries += 1
                       
            exam_subtype["avg_score"] = total_score / total_entries
        exam_type["avg_score"] = total_score / total_entries

    if total_entries > 0:
        avg_score = total_score / total_entries
        user_data["avg_score"] = avg_score

    # Update or insert the document in the MongoDB collection
    analytics_collection.update_one(
        {"user_id": user_id},
        {"$set": user_data},
        upsert=True
    )

    return {"message": "sucess"}


@analytics_router.post('/exam')
def exam_analytics(exam_data: Exam):
   return update_analytics(exam_data)




@analytics_router.get('/exam_details/{user_id}')
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

@analytics_router.post('/interest')
def interested_job(data: Interest):
    '''
    - collect the user skills 
    - collect the job skills
    - find the skills required to learn by the user
    - store the interested job, user skills in a list
    '''
    pass