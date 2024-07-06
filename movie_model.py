import datetime
from pydantic import BaseModel, Field
from genre import GenreEnum
from language import LanguageEnum


class MovieBaseModel(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='Movie Name')
    genre: GenreEnum
    release_date: datetime.date
    rating: float = Field(lt=10, gt=1, description='Rating')
    language: LanguageEnum
