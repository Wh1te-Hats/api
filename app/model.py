from pydantic import BaseModel

class General(BaseModel):
    user_id: str
    topic: str

class Course(BaseModel):
    user_id: str
    subject: str
    
class UserRegister(BaseModel):
    username: str
    password: str
    grade: int
    board: str

class UserLogin(BaseModel):
    username: str
    password: str

class Job(BaseModel):
    role: str
    location: str
    type: str

class Career(BaseModel):
    skill: list
