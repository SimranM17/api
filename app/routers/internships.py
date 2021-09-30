import app.crud.create as create
from app.schemas import InternshipSchema
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
import app.crud.read as read
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


@internships_router.get("/read-all")
async def read_internships(db: Session = Depends(get_db)):
    return read.internships(db)


@internships_router.post("/new-internship", response_model=dict)
async def new_internship(
    internship: InternshipSchema,
    db: Session = Depends(get_db),
):
    try:
        # Internships_schema.validate(internship)
        create.internship(internship_data=internship, db=db)
        return {
            "message": "created-internship",
            "internship": internship,
            "status_code": 200,
        }
    except Exception as err:
        return {
            "message": "Bad Data",
            "internship": f"Bad data. The Error is: {err}\
            and the data you sent is {internship}",
            "status_code": 400,
        }
