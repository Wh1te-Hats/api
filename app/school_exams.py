from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

@app.get("/exams/school/cbse")
async def cbse():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/icse")
async def icse():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/state")
async def state():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/cambridge")

async def cambridge():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/ib")
async def ib():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/talent")
async def talents_and_scholarships():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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

    return data

@app.get("/exams/school/ntse")
async def ntse():
    client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/exam")
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
