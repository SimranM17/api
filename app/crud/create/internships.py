from app.models import Internship
from sqlalchemy.orm.session import Session
from app.schemas import Internships_schema


def create_internship(internship_data: Internships_schema, db: Session):
    internship_instance = Internship(
        position_title=internship_data.position_title,
        company_name=internship_data.company_name,
        part_time_or_full_time=internship_data.part_time_or_full_time,
        location=internship_data.location,
        skills=internship_data.skills,
        number_of_openings=internship_data.number_of_openings,
        description=internship_data.description,
        expires_on=internship_data.expires_on,
        applications=internship_data.applications,
    )
    db.add(internship_instance)
    db.commit()
    return internship_instance
