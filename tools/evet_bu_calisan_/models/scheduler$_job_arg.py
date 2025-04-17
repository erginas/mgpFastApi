from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Scheduler$JobArg(Base):
    __tablename__ = 'scheduler$_job_arg'

    job_name: Mapped[Optional[String]] = mapped_column(String)
    arg_name: Mapped[Optional[String]] = mapped_column(String)
    arg_position: Mapped[Optional[Integer]] = mapped_column(Integer)
    value: Mapped[Optional[String]] = mapped_column(String)
    flags: Mapped[Optional[Integer]] = mapped_column(Integer)
    enabled: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)