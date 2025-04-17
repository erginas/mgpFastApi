from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ResimOlcusu(Base):
    __tablename__ = 'resim_olcusu'

    resim_olcu_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    olcum_turu: Mapped[Optional[String]] = mapped_column(String)
    ust_limit: Mapped[Optional[Float]] = mapped_column(Float)
    alt_limit: Mapped[Optional[Float]] = mapped_column(Float)
    esas_olcu: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    teknik_resim_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    teknik_resim_kapsam_id: Mapped[Optional[String]] = mapped_column(String)
    kritik_fl: Mapped[Optional[String]] = mapped_column(String)
    malzemeye_ozgu_fl: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    teknik_resim: Mapped[Optional['TeknikResim']] = relationship(back_populates='resim_olcusu')
    teknik_resim_kapsami: Mapped[Optional['TeknikResimKapsami']] = relationship(back_populates='resim_olcusu')