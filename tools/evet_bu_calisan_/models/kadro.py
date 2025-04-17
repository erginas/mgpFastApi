from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Kadro(Base):
    __tablename__ = 'kadro'

    kadro_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    bagimli_kadro: Mapped[Optional[Float]] = mapped_column(Float)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    kapatan: Mapped[Optional[Float]] = mapped_column(Float)
    acilma_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kapanma_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    acik_kadro: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(back_populates='kadro')
    kadro: Mapped[Optional['Kadro']] = relationship(back_populates='kadro')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='kadro')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='kadro')