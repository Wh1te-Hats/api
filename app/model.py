from pydantic import BaseModel

class Aptitude(BaseModel):
    user_id: str
    type: str
    topic: str
    
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
