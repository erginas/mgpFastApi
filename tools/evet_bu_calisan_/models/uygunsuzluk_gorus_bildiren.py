from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UygunsuzlukGorusBildiren(Base):
    __tablename__ = 'uygunsuzluk_gorus_bildiren'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    rapor_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    uygunsuzluk: Mapped[Optional['Uygunsuzluk']] = relationship(back_populates='uygunsuzluk_gorus_bildiren')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uygunsuzluk_gorus_bildiren')