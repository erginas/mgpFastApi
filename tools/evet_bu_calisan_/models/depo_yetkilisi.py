from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DepoYetkilisi(Base):
    __tablename__ = 'depo_yetkilisi'

    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    depo: Mapped[Optional['Depo']] = relationship(back_populates='depo_yetkilisi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='depo_yetkilisi')