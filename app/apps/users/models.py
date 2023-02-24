from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from libs.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(128), unique=True)
    birth_date: Mapped[date] = mapped_column()
