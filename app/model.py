from pydantic import BaseModel
from typing import Optional

class General(BaseModel):
    user_id: str
    topic: str

class Course(BaseModel):
    user_id: str
    subject: str
    
class UserRegister(BaseModel):
    id:str
    name: str
    city: str
    state: str
    grade: str
    gender:str
    board: str

class ChatBot(BaseModel):
    message: str
    flow: Optional[str] = "EMPTY"
    num: Optional[int] = -1

class UserLogin(BaseModel):
    username: str
    password: str

class Job(BaseModel):
    role: str
    location: str
    type: str

class Career(BaseModel):
    skill: list
