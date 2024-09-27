from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

class Author(BaseModel):
    id: int

    name:str
    phone: str
    class Config:
        orm_mode = True

class Post(BaseModel):
    id: int

    title:str
    description:str
    image_url:str

    class Config:
        orm_mode = True