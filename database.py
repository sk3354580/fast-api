from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import cloudinary

cloudinary.config(
    cloud_name= "drd46pgae",
    api_key= "728384414442461",
    api_secret ="Tx9Z-zX84WZcXsm2p3FlYmt2o-A"
)

engine=create_engine("postgresql://postgres:shiv1915@localhost/images",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)

Base.metadata.create_all(engine)