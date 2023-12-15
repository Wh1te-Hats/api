from fastapi import APIRouter
from app.database import MongoClient

govt_exam_router = APIRouter(tags=["exam"])

@govt_exam_router.get("/exams/govt/{exam_type}")
async def exam(exam_type:str):
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
    
    if exam_type == 'insurance':
        db = client["exam"]
        collection = db["insurance"]
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
                }
                )

    elif exam_type == 'defence':
        db = client["exam"]
        collection = db["defence"]
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

    elif exam_type == 'apscb':
        db = client["exam"]
        collection = db["apscb"]
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

    elif exam_type == 'bcb':
        db = client["exam"]
        collection = db["bcb"]
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

    elif exam_type == 'ibps':
        db = client["exam"]
        collection = db["ibps"]
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

    elif exam_type == 'nainital_banking_exam':
        db = client["exam"]
        collection = db["nainital_b"]
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

    elif exam_type == 'rbi':
        db = client["exam"]
        collection = db["rbi"]
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
    elif exam_type == 'sbi':
        db = client["exam"]
        collection = db["sbi"]
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
    elif exam_type == 'sib':
        db = client["exam"]
        collection = db["sib"]
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

