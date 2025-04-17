from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FirmaSiniflandirmasi(Base):
    __tablename__ = 'firma_siniflandirmasi'

    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sinifi: Mapped[Optional[String]] = mapped_column(String)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='firma_siniflandirmasi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='firma_siniflandirmasi')