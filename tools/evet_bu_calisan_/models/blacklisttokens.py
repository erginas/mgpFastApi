from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Blacklisttokens(Base):
    __tablename__ = 'blacklisttokens'

    id: Mapped[Optional[String]] = mapped_column(String)
    expire: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime)
