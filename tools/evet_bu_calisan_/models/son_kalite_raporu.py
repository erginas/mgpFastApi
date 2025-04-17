from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SonKaliteRaporu(Base):
    __tablename__ = 'son_kalite_raporu'

    rapor_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    duzenleyen: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_kontrol: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_kabul: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_sartli_kabul: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_red: Mapped[Optional[Float]] = mapped_column(Float)
    sk_plan_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    baski_sayisi: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='son_kalite_raporu')
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='son_kalite_raporu')
    sk_plani: Mapped[Optional['SkPlani']] = relationship(back_populates='son_kalite_raporu')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='son_kalite_raporu')