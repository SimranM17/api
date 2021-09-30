from app.models import InternshipModel
from sqlalchemy.orm.session import Session


def get_users(db: Session):
    return db.query(InternshipModel)
