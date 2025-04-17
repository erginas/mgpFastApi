from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KaliteKontrolKaydi(Base):
    __tablename__ = 'kalite_kontrol_kaydi'

    kalite_kontrol_kayit_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    resim_olcu_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    olculen_deger: Mapped[Optional[Float]] = mapped_column(Float)
    olcum_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    gozlem: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    sonuc: Mapped[Optional[String]] = mapped_column(String)
    ornek_no: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    resim_olcusu: Mapped[Optional['ResimOlcusu']] = relationship(back_populates='kalite_kontrol_kaydi')
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='kalite_kontrol_kaydi')