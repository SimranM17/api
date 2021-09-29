from app.models import Internships
from sqlalchemy.orm.session import Session


def get_users(db: Session):
    return db.query(Internships)
