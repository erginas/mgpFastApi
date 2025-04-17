from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Vardiya(Base):
    __tablename__ = 'vardiya'

    vardiya_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    baslama_zamani: Mapped[Optional[String]] = mapped_column(String)
    bitis_zamani: Mapped[Optional[String]] = mapped_column(String)
    mola_1_baslama: Mapped[Optional[String]] = mapped_column(String)
    mola_1_bitis: Mapped[Optional[String]] = mapped_column(String)
    mola_2_baslama: Mapped[Optional[String]] = mapped_column(String)
    mola_2_bitis: Mapped[Optional[String]] = mapped_column(String)
    mola_3_baslama: Mapped[Optional[String]] = mapped_column(String)
    mola_3_bitis: Mapped[Optional[String]] = mapped_column(String)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)