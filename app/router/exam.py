from fastapi import APIRouter
from app.database import MongoClient

exam_router = APIRouter(tags=["exam"])


@exam_router.get("/exams/school/{school_type}")
async def exam(school_type:str):
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
    
    if school_type == 'cbse':
        db = client["exam"]
        collection = db["cbse"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'icse':
        db = client["exam"]
        collection = db["icse"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'state':
        db = client["exam"]
        collection = db["state"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'cambridge':
        db = client["exam"]
        collection = db["cambridge"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'ib':
        db = client["exam"]
        collection = db["ib"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'talent':
        db = client["exam"]
        collection = db["talent"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    elif school_type == 'ntse':
        db = client["exam"]
        collection = db["ntse"]
        # Fetch the document from MongoDB
        document = collection.find_one()

        # Initialize a list to store the exam data
        data = []

        # Iterate over the objects within the document
        for exam_name, exam_data in document.items():
            # Skip the "_id" field which is not an exam object
            if exam_name != "_id":
                data.append(
                {
                    "Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility Criteria", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                }
                )

    return data

