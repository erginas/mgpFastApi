from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HammaddeSertifikasi(Base):
    __tablename__ = 'hammadde_sertifikasi'

    sertifika_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    goruntu: Mapped[Optional[String]] = mapped_column(String)
    malzeme_bilgisi: Mapped[Optional[String]] = mapped_column(String)
    tipi: Mapped[Optional[String]] = mapped_column(String)
    id: Mapped[Optional[Integer]] = mapped_column(Integer)
    file_backup: Mapped[Optional[Integer]] = mapped_column(Integer)
    dosya_yolu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)