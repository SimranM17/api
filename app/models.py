from sqlalchemy.sql.schema import ForeignKey
from app.database import Base
from sqlalchemy import Column, Integer, String, Date, ARRAY
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    picture = Column(String)

    applications_id = Column(Integer, ForeignKey("applications.id"))
    applications = relationship("Application", back_populates="intern_user_object")


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    intern_name = Column(String, index=True)
    intern_phone_number = Column(Integer)

    intern_user_object = relationship("User", back_populates="applications")
    internship = relationship(
        "Internships", uselist=False, back_populates="applications"
    )

    applicant_information = Column(String)


class Internships(Base):
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

    application_id = Column(Integer, ForeignKey("applications.id"))
    applications = relationship("Application", back_populates="internship")


class Api_keys(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(Integer, index=True)
