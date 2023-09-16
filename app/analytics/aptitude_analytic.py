from pymongo import MongoClient
from datetime import datetime

def analytics(response,topic,data):
    MONGO_URI = "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test"
    client = MongoClient(MONGO_URI)  
    db = client["test"]  
    collection = db[data.user_id]

    data = {

            "topic": data.topic,
            "timestamp": datetime.utcnow(),
            "question": [],
            "score": ""
        }
    

    for ques,expl in zip(response["question"],response["explaination"]):
        data["question"].append({
            "question_number": ques["question_number"],
            "question_text_html": ques["question_text_html"],
            "options_html": ques["options_html"],
            "correct_option": expl["correct_option"],
            "explaination": expl["explaination"],
            "attempted_answer": "",
            "score": ""
        })



    collection.insert_one(data)