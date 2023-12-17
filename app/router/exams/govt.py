from fastapi import APIRouter
from app.database import MongoClient, rd,client

import json

govt_exam_router = APIRouter(tags=["exam"])

@govt_exam_router.get("/exams/govt/{exam_type}")
async def exam(exam_type:str):
    cache = rd.get(exam_type)
    if cache: 
        return json.loads(cache)
    else:

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
                        "Subjects Covered": [],
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
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
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
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
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

                        "Title":exam_data.get("Title", ""),
                        "Description": exam_data.get("Description", ""),
                        "Subjects Covered": [],
                        "Eligibility Criteria": exam_data.get("Eligibility", ""),
                        "Pass Criteria": exam_data.get("Pass Criteria", ""),
                        "Link to Website": exam_data.get("Link", ""),
                        "Registration fee": exam_data.get("Reg_fee", ""),
                        "Logo": exam_data.get("Logo", ""),
                        "Previous year Question papers": exam_data.get("Prev_year_papers", ""),
                    }
                    )
        for i, exam_data in enumerate(data):
            data[i] = {key: value if value is not None else "" for key, value in exam_data.items()}
        rd.set(exam_type,json.dumps(data))
        rd.expire(exam_type,3600) 
        return data

