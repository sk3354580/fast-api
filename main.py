from xml.etree.ElementTree import PI
from fastapi import FastAPI, File, UploadFile, Depends
import  cloudinary
import models
from models import pics
from schemas import Picss
from database import Base,engine,SessionLocal
import cloudinary.uploader
from sqlalchemy.orm import sessionmaker, Session
Base.metadata.create_all(bind=engine)
app = FastAPI()


# this is for getting file name
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    result = cloudinary.uploader.upload(file.file)
    url = result.get("url")
    filename = file.filename

    con = {
        "filename":filename,
        "url":url
    }
    return con


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   
@app.get("/testing_api/")
def read_users(db:Session = Depends(get_db)):
     users = db.query(pics).all()
     return users


def create_place(db: Session, place: Picss):
    db_place = pics(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place

@app.post('/places/', response_model=Picss)
def create_places_view(place: Picss, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place