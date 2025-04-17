from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AstipTipsanDepo(Base):
    __tablename__ = 'astip_tipsan_depo'

    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    malzeme_adi: Mapped[Optional[String]] = mapped_column(String)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    siparis_yil: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_ay: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_no: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    sip_no: Mapped[Optional[String]] = mapped_column(String)
    ce_bilgisi: Mapped[Optional[String]] = mapped_column(String)
    son_kullanma_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    irs_fat: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
