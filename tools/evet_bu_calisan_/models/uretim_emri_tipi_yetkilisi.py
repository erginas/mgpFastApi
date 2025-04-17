from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UretimEmriTipiYetkilisi(Base):
    __tablename__ = 'uretim_emri_tipi_yetkilisi'

    uretim_emri_tip_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    uretim_emri_tipi: Mapped[Optional['UretimEmriTipi']] = relationship(back_populates='uretim_emri_tipi_yetkilisi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uretim_emri_tipi_yetkilisi')