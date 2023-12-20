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
            "total_time_spent": 0,
            "total_test_taken": 0
        }
    
    # Update history with new data
        history_entry = {
            "type" : type,
            "history": [
                {
                    "subtype": subtype,
                    "score": data.score,
                    "total_test_taken": 1
                },
            ],
            "score": data.score,
            "total_test_taken": 1
        }

        user_data["history"].append(history_entry)
    else:
        # {'user_id': 'string', 'history': [{'course': [{'subtj': [{'data': 'string', 'total_time': 0, 'score': 16, 'incorrect': 4, 'correct': 16}], 'avg_score': ''}], 'avg_score': ''}], 'total_time_spent': 0, 'total_test_taken': 0}
        exam_details = user_data.get('history')
        for i in exam_details:
            print(i)
            if i["type"] == data.type:
                i["score"] += data.score
                i["total_test_taken"] += 1
                for j in i["history"]:
                    print(j)
                    if j["subtype"] == data.subtype:
                        j["score"] += data.score
                        j["total_test_taken"] += 1
                        
                i["history"].append({
                    "subtype" : data.subtype,
                    "score": data.score,
                    "total_test_taken": 1
                })
                break

        exam_details.append({
            "type": data.type,
            "history": [],
            "score": data.score,
            "total_test_taken": 1
        })
        # subtype_list = []
        # type_list = {}
        # type_list[f"{data.type}"] = {}
        # type_list[f"{data.type}"][f"{data.subtype}"] = []
        # subtype_list.append(
        #     {
        #         "data": data.date,
        #         "total_time": data.total_time,
        #         "score": data.score,
        #         "incorrect": data.incorrect,
        #         "correct": data.correct
        #     }
        # )
        # type_list[f'{data.type}'][f'{data.subtype}'].append(subtype_list)
        # user_data["history"].append(type_list)
        

    user_data["total_time_spent"] += data.total_time
    user_data["total_test_taken"] += 1

    print(user_data)

    # Update or insert the document in the MongoDB collection
    analytics_collection.update_one(
        {"user_id": user_id},
        {"$set": user_data},
        upsert=True
    )

    return "sucess"


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
    user_data = analytics_collection.find_one({"user_id": user_id})
    total_time_spent = user_data.get("total_time_spent")
    total_test_taken = user_data.get("total_test_taken")
    
    details = user_data.get("history")
    course_score = 0
    course_chapter_score = []
    general_score = 0
    general_chapter_score = []
    career_score = 0
    career_chapter_score = []
    course_subtype = []
    career_subtype = []
    general_subtype = []
    general_chapter = []
    course_chapter = []
    carrer_chapter = []


    for details in user_data.get("history"):
        if details["type"] == 'course':
            course_score = details["score"]
            for j in details["history"]:
                course_subtype.append(j["subtype"])
                course_chapter.append(j["score"])
            course_chapter_score.append({
                    "subtype": course_subtype,
                    "score": course_chapter
                }) 
            # career_list = 
        elif details["type"] == 'general':
            general_score = details["score"]
            for j in details["history"]:
                general_subtype.append(j["subtype"])
                general_chapter.append(j["score"])
            general_chapter_score.append({
                    "subtype": general_subtype,
                    "score": general_chapter
                }) 
        elif details["type"] == 'career':
            career_score = details["score"]
            for j in details["history"]:
                career_subtype.append(j["subtype"])
                carrer_chapter.append(j["score"])
            career_chapter_score.append({
                    "subtype": career_subtype,
                    "score": carrer_chapter
                }) 

    
    
    data = {
            "total_time_spent": total_time_spent,
            "total_test_taken": total_time_spent,
            "course_score": course_score,
            "general_score": general_score,
            "career_score": career_score,
            "course_chapter_score": course_chapter_score,
            "general_chapter_score": general_chapter_score,
            "career_chapter_score": career_chapter_score
        }
    return data
    

@analytics_router.post('/interest')
def interested_job(data: Interest):
    '''
    - collect the user skills 
    - collect the job skills
    - find the skills required to learn by the user
    - store the interested job, user skills in a list
    '''
    pass