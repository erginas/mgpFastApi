from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UretimTalepDetay(Base):
    __tablename__ = 'uretim_talep_detay'

    fis_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yapilacak_islem: Mapped[Optional[String]] = mapped_column(String)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    miktar_talep: Mapped[Optional[Float]] = mapped_column(Float)
    tarih_talep: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    miktar_is_emri: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    oncelik: Mapped[Optional[String]] = mapped_column(String)
    miktar_iptal: Mapped[Optional[Float]] = mapped_column(Float)
    istenen_lot_no: Mapped[Optional[String]] = mapped_column(String)
    istenen_malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    bekleme_sebebi: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    siparis_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    iade_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='uretim_talep_detay')
    uretim_talebi: Mapped[Optional['UretimTalebi']] = relationship(back_populates='uretim_talep_detay')
    malzeme_1: Mapped[Optional['Malzeme']] = relationship(back_populates='uretim_talep_detay')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uretim_talep_detay')