from fastapi import APIRouter
from app.database import MongoClient

school_exam_router = APIRouter(tags=["exam"])

@school_exam_router.get("/exams/school/{school_type}")
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
                    
                    "Title":exam_data.get("Title", ""),"Title":exam_data.get("Title", ""),
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
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
                    "Title":exam_data.get("Title", ""),
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                }
                )

    elif school_type == 'cambridge':
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
                    
                    "Title":exam_data.get("Title", ""),"Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                }
                )

    elif school_type == 'ib':
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
                    "Title":exam_data.get("Title", ""),
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                }
                )

    elif school_type == 'state':
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
                    
                    "Title":exam_data.get("Title", ""),"Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
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
                    
                    "Title":exam_data.get("Title", ""),"Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
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
                    
                    "Title":exam_data.get("Title", ""),"Exam Name": exam_name,
                    "Description": exam_data.get("Description", ""),
                    "Subjects Covered": exam_data.get("Subjects Covered", ""),
                    "Eligibility Criteria": exam_data.get("Eligibility", ""),
                    "Pass Criteria": exam_data.get("Pass Criteria", ""),
                    "Link to Website": exam_data.get("Link", ""),
                    "Registration fee": exam_data.get("Reg_fee", ""),
                    "Logo": exam_data.get("Logo", ""),
                    "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                }
                )

    return data

