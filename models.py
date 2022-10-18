from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class pics(Base):
    __tablename__='pics_url'
    id=Column(Integer,primary_key=True)
    name_of_image=Column(String(255),nullable=False)
    url_of_image=Column(Text)
    class Config:
        orm_mode = True
