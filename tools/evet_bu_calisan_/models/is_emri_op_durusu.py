from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IsEmriOpDurusu(Base):
    __tablename__ = 'is_emri_op_durusu'

    baslama_z: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    islem_sirasi: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    durus_detay_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    bitis_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    durus_tipi: Mapped[Optional['DurusTipi']] = relationship(back_populates='is_emri_op_durusu')
    is_emri_operasyonu: Mapped[Optional['IsEmriOperasyonu']] = relationship(back_populates='is_emri_op_durusu')