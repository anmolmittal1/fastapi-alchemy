from datetime import date

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    email: EmailStr
    birth_date: date

    class Config:
        orm_mode = True
