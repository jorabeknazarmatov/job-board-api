from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Annotated


correct_date = Annotated[date, Field(ge=date.today())]

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None
    type: str | None = None