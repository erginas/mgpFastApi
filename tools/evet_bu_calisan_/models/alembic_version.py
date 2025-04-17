from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AlembicVersion(Base):
    __tablename__ = 'alembic_version'

    version_num: Mapped[Optional[String]] = mapped_column(String, nullable=False)