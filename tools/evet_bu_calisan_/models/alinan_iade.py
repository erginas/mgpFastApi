from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AlinanIade(Base):
    __tablename__ = 'alinan_iade'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    iade_fis_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    irsaliye: Mapped[Optional[String]] = mapped_column(String)
    fatura: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iade_nedeni: Mapped[Optional[String]] = mapped_column(String)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='alinan_iade')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='alinan_iade')
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(back_populates='alinan_iade')