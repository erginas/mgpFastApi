from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FirmaDegerlendirmesi(Base):
    __tablename__ = 'firma_degerlendirmesi'

    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kriter_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    degeri: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    firma_siniflandirmasi: Mapped[Optional['FirmaSiniflandirmasi']] = relationship(back_populates='firma_degerlendirmesi')
    degerlendirme_kriteri: Mapped[Optional['DegerlendirmeKriteri']] = relationship(back_populates='firma_degerlendirmesi')