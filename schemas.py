from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str
    age: int
    country: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True