from fastapi import APIRouter
from app.database import MongoClient, rd

import json

counselor_data_router = APIRouter(tags=["counselor"])

@counselor_data_router.get("/counselor/{name}")
async def counselor(name:str):
    cache = rd.get(name)
    if cache: 
        return json.loads(cache)
    else:
        client = MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/counselor")

        if name == 'counselor':
            db = client["counselor"]
            collection = db["counselor"]
            # Fetch the document from MongoDB
            document = collection.find_one()

            # Initialize a list to store the counselor data
            data = []

            # Iterate over the objects within the document
            for counselor_name, counselor_data in document.items():
                # Skip the "_id" field which is not an counselor object
                if counselor_name != "_id":
                    data.append(
                    {

                        "Name":counselor_data.get("name", ""),
                        "Qualification": counselor_data.get("qualifications", ""),
                        "Email": counselor_data.get("experience", ""),
                        "Experience": counselor_data.get("email", ""),
                        "ImgProfile": counselor_data.get("imgProfile", ""),
                    }
                    )

        
        rd.set(name,json.dumps(data))
        rd.expire(name,3600) 
        return data

