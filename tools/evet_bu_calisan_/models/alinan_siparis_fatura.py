from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlinanSiparisFatura(Base):
    __tablename__ = 'alinan_siparis_fatura'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    yil: Mapped[Optional[Integer]] = mapped_column(Integer)
    ay: Mapped[Optional[Integer]] = mapped_column(Integer)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    fatura_no: Mapped[Optional[String]] = mapped_column(String)
    tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    hareket_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    irsaliye_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    irsaliye_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    irsaliye_giren: Mapped[Optional[Integer]] = mapped_column(Integer)
    fatura_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fatura_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fatura_giren: Mapped[Optional[Integer]] = mapped_column(Integer)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    baski_sayisi: Mapped[Optional[Integer]] = mapped_column(Integer)
    kimlik_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    gumruk_bedeli: Mapped[Optional[Integer]] = mapped_column(Integer)
    tasima_bedeli: Mapped[Optional[Integer]] = mapped_column(Integer)
    diger_bedel: Mapped[Optional[Integer]] = mapped_column(Integer)
    beyanname_no: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    birim_no: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='alinan_siparis_fatura')
