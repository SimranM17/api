from .users import User
from enum import Enum
from pydantic import BaseModel
from typing import Iterable, Optional
from datetime import date


class part_time_or_full_time(str, Enum):
    part_time = "part_time"
    full_time = "full_time"


class Internship(BaseModel):
    id: int
    position_title: str
    company_name: str
    part_time_or_full_time: part_time_or_full_time
    location: str
    skills: Iterable[str]
    number_of_openings: int
    description: str
    expires_on: date
    application_ids: Optional[Iterable[int]]


class Application(BaseModel):
    id: int
    intern_name: str
    intern_phone_number: int
    intern_user_object = User
    internship = Internship
