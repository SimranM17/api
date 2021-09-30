from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class PartTimeOrFullTime(str, Enum):
    part_time = "part_time"
    full_time = "full_time"


class ApplicationSchema(BaseModel):
    id: int

    intern_name: str
    intern_phone_number: int
    intern_email: int

    internship_id: int
    user_id: int

    applicant_information: str

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    picture: str

    applications: List[ApplicationSchema] or None

    class Config:
        orm_mode = True


class InternshipSchema(BaseModel):
    id: Optional[int]

    position_title: str
    company_name: str
    description: str

    part_time_or_full_time: PartTimeOrFullTime
    location: str
    skills: List[str]

    number_of_openings: int
    expires_on: date

    application_id: int
    applications: List[ApplicationSchema] or None

    class Config:
        orm_mode = True
