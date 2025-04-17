from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SatinAlmaTalebi(Base):
    __tablename__ = 'satin_alma_talebi'

    satinalma_talep_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    yil: Mapped[Optional[Float]] = mapped_column(Float)
    parti_no: Mapped[Optional[Float]] = mapped_column(Float)
    malzeme_adi: Mapped[Optional[String]] = mapped_column(String)
    marka: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Float]] = mapped_column(Float)
    giris_cikis: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    termin_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    onay_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fatura_irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    belge_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    birim_fiyat: Mapped[Optional[Float]] = mapped_column(Float)
    farkli_karsilama: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='satin_alma_talebi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='satin_alma_talebi')