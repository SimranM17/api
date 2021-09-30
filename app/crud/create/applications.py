from app.models import ApplicationModel, InternshipModel, UserModel
from sqlalchemy.orm.session import Session
from app.schemas import ApplicationSchema


def create_appliation(application_data: ApplicationSchema, db: Session):
    internship_exists = (
        db.query(InternshipModel)
        .all()
        .filter_by(InternshipModel.id == application_data.internship_id)
    )

    user_exists = (
        db.query(UserModel)
        .all()
        .filter_by(UserModel.id == application_data.user_id)
    )

    if internship_exists and user_exists:
        application_instance = ApplicationModel(
            intern_name=application_data.intern_name,
            intern_phone_number=application_data.intern_phone_number,
            application_information=application_data.applicant_information,
            internship_id=application_data.internship_id,
        )
        db.add(application_instance)
        db.commit()
        db.refresh(application_instance)
        return application_instance

    if internship_exists:
        return {"code": "bad-data", "err": "Invalid user id"}
    return {"code": "bad-data", "err": "Invalid internship_id id"}
