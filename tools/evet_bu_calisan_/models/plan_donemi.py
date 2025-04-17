from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PlanDonemi(Base):
    __tablename__ = 'plan_donemi'

    donem_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    durum: Mapped[Optional[String]] = mapped_column(String)
    surum: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='plan_donemi')