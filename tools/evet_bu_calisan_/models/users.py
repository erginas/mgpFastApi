from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    email: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    full_name: Mapped[Optional[String]] = mapped_column(String)
    password: Mapped[Optional[String]] = mapped_column(String)
    is_active: Mapped[Optional[String]] = mapped_column(String)
    created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    updated_at: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    articles: Mapped[Optional[Integer]] = mapped_column(Integer)
    title: Mapped[Optional[String]] = mapped_column(String)
    profile_path: Mapped[Optional[String]] = mapped_column(String)