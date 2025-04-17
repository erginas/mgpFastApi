from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ToplantiIlgilisi(Base):
    __tablename__ = 'toplanti_ilgilisi'

    toplanti_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    toplanti_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    katilim_fl: Mapped[Optional[String]] = mapped_column(String)
    firma: Mapped[Optional[String]] = mapped_column(String)
    katilimci: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    toplanti: Mapped[Optional['Toplanti']] = relationship(back_populates='toplanti_ilgilisi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='toplanti_ilgilisi')
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(back_populates='toplanti_ilgilisi')