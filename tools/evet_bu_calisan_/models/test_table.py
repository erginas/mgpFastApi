from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'test_table'

    yil: Mapped[Optional[Float]] = mapped_column(Float)
    sira: Mapped[Optional[Float]] = mapped_column(Float)
    deger: Mapped[Optional[String]] = mapped_column(String)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    log_record_id: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)