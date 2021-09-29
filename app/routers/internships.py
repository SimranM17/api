from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from app.crud.read.internships import get_users
from app.database import SessionLocal, engine
from app.models import Base


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


internships_router = APIRouter(
    prefix="/internship",
    tags=["internship"],
    responses={404: {"description": "Not found"}},
)


@internships_router.get("/", response_model=dict)
async def read_internships(db: Session = Depends(get_db)):
    return get_users(db)
