from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlinanSiparisFaturaDetay(Base):
    __tablename__ = 'alinan_siparis_fatura_detay'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    als_fatura_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    hareket_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    uretim_bildirim_no: Mapped[Optional[String]] = mapped_column(String)
    verme_bildirim_no: Mapped[Optional[String]] = mapped_column(String)
    adet: Mapped[Optional[Integer]] = mapped_column(Integer)
    iptal_eden: Mapped[Optional[String]] = mapped_column(String)
    iptal_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_aciklama: Mapped[Optional[String]] = mapped_column(String)
    muadil_malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    muadil_fiyat: Mapped[Optional[Integer]] = mapped_column(Integer)
    muadil_iskonto: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis_fatura: Mapped[Optional['AlinanSiparisFatura']] = relationship(
        back_populates='alinan_siparis_fatura_detay')
