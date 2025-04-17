from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyLogRecord(Base):
    __tablename__ = 'my_log_record'

    log_record_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    create_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    create_session: Mapped[Optional[String]] = mapped_column(String)
    delete_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    delete_session: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    my_log_session: Mapped[Optional['MyLogSession']] = relationship(back_populates='my_log_record')
    my_log_session_1: Mapped[Optional['MyLogSession']] = relationship(back_populates='my_log_record')