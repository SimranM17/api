from sqlalchemy.sql.schema import ForeignKey
from app.database import Base
from sqlalchemy import Column, Integer, String, Date, ARRAY
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    picture = Column(String)

    applications = relationship("ApplicationModel")


class ApplicationModel(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    intern_name = Column(String, index=True)
    intern_phone_number = Column(Integer)

    applicant_information = Column(String)

    internship_id = Column(Integer, ForeignKey("internships.id"))

    user_id = Column(Integer, ForeignKey("users.id"))


class InternshipModel(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String, index=True)
    position_title = Column(String, index=True)
    description = Column(String)

    part_time_or_full_time = Column(String, index=True)
    location = Column(String, index=True)
    skills = Column(ARRAY(String), index=True)

    number_of_openings = Column(Integer)
    expires_on = Column(Date, index=True)

    applications = relationship("ApplicationModel")


class ApiKeysModel(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(Integer, index=True)
