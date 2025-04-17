from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OrganizasyonBirimi(Base):
    __tablename__ = 'organizasyon_birimi'

    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    bagimli_birim: Mapped[Optional[Integer]] = mapped_column(Integer)
    kisa_kod: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    cesidi: Mapped[Optional[String]] = mapped_column(String)
    gizli: Mapped[Optional[Float]] = mapped_column(Float)
    aktif: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(back_populates='organizasyon_birimi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='organizasyon_birimi')