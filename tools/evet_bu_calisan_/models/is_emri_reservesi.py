from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IsEmriReservesi(Base):
    __tablename__ = 'is_emri_reservesi'

    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    yil: Mapped[Optional[Float]] = mapped_column(Float)
    fis_no: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_reserve: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ue_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='is_emri_reservesi')
    uretim_talep_detay: Mapped[Optional['UretimTalepDetay']] = relationship(back_populates='is_emri_reservesi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='is_emri_reservesi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='is_emri_reservesi')