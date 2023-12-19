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
    community_id: list
    career_goal: list

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

class Exam(BaseModel):
    user_id: str
    total_time: int
    date: str
    score: int
    incorrect: int
    correct: int
    type: str
    subtype: str

class Interest(BaseModel):
    user_id:str
    career_goal:str

class CommunityUser(BaseModel):
    name:str
    city:str
    state:str
    school_or_college:str
    career_goal: list

class CourseExam(BaseModel):
    grade:str
    subject: str
    chapter: str