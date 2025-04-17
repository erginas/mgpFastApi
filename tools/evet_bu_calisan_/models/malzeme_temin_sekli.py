from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeTeminSekli(Base):
    __tablename__ = 'malzeme_temin_sekli'

    temin_sekil_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    oncelik: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    temin_sekli: Mapped[Optional['TeminSekli']] = relationship(back_populates='malzeme_temin_sekli')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='malzeme_temin_sekli')