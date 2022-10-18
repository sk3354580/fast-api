from pydantic import BaseModel

class Picss(BaseModel):
    name_of_image: str
    url_of_image: str

    class Config:
        orm_mode = True