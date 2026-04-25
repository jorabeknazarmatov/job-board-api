from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from datetime import date


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String(200), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    middleName: Mapped[str] = mapped_column(String(200))
    sex: Mapped[str] = mapped_column(String(50), nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    @property
    def age(self) -> int:
        today = date.today()
        
        age = today.year - self.birthday - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )
        
        return age