from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    message: str
    category: str


class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class FeedbackCreate(BaseModel):
    user_id: int
    message: str

class ActivityCreate(BaseModel):
    user_id: int
    module_name: str