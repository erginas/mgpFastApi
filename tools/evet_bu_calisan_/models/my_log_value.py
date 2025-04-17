from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyLogValue(Base):
    __tablename__ = 'my_log_value'

    log_value_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    log_field: Mapped[Optional[String]] = mapped_column(String)
    log_value: Mapped[Optional[String]] = mapped_column(String)
    log_session_id: Mapped[Optional[String]] = mapped_column(String)
    log_key_id: Mapped[Optional[String]] = mapped_column(String)
    chg_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    my_log_session: Mapped[Optional['MyLogSession']] = relationship(back_populates='my_log_value')
    my_log_record: Mapped[Optional['MyLogRecord']] = relationship(back_populates='my_log_value')