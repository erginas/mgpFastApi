from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IsEmriOperasyonDurusu(Base):
    __tablename__ = 'is_emri_operasyon_durusu'

    islem_sirasi: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    durus_detay_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    frekans: Mapped[Optional[Float]] = mapped_column(Float)
    toplam_sure: Mapped[Optional[Float]] = mapped_column(Float)
    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)