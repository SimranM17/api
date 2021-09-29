from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class part_time_or_full_time(str, Enum):
    part_time = "part_time"
    full_time = "full_time"


class Application_schema(BaseModel):
    id: int

    intern_name: str
    intern_phone_number: int
    intern_email: int

    internship_id: int
    user_id: int

    applicant_information: str

    class Config:
        orm_mode = True


class User_schema(BaseModel):
    id: int
    name: str
    email: str
    picture: str

    applications: Optional[List[Application_schema]]

    class Config:
        orm_mode = True


class Internships_schema(BaseModel):
    id: Optional[int]

    position_title: str
    company_name: str
    description: str

    part_time_or_full_time: part_time_or_full_time
    location: str
    skills: List[str]

    number_of_openings: int
    expires_on: date

    application_id: int
    applications: Optional[List[Application_schema]]

    class Config:
        orm_mode = True
