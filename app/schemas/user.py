from pydantic import BaseModel, field_validator, Field, EmailStr
from datetime import date
from typing import Annotated
from enum import Enum


BirthDate = Annotated[date, Field(ge=date(1900, 1, 1), le=date.today())]

class SexEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"
    

class UserBase(BaseModel):
    surname: str = Field(min_length=2, max_length=100)
    name: str = Field(min_length=2, max_length=100)
    middleName: str | None = None
    sex: SexEnum
    birthday: BirthDate
    email: EmailStr
    password: str = Field(min_length=8)
    
    @field_validator("birthday")
    @classmethod
    def check_age(cls, v: date):
        
        today = date.today()
        age = today.year - v.year - (
            (today.month, today.day) < (v.month, v.day)
        )
        
        if age < 16:
            raise ValueError("You must be at least 16 years old to register.")      
        return v

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    
    class Config:
        from_attributes = True