from pydantic import BaseModel
from typing import Optional, Iterable


class User(BaseModel):
    id: int
    name: str
    email: str
    picture: str
    applications: Optional[Iterable[int]] = []
