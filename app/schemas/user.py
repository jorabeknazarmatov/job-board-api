from pydantic import BaseModel, field_validator
from datetime import date


class UserBase(BaseModel):
    surname: str
    name: str
    middleName: str
    sex: str
    birthday: date
    email: str
    
    @field_validator("birthday")
    @classmethod
    def check_age(cls, v: date):
        if v.year < 1900:
            raise ValueError("Tug'ilgan yil juda kichik")
        return v

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int