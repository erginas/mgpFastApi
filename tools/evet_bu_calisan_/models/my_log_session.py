from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyLogSession(Base):
    __tablename__ = 'my_log_session'

    log_session_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    application_user: Mapped[Optional[String]] = mapped_column(String)
    start_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    connect_info: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)