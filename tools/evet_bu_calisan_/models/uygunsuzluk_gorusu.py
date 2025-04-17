from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UygunsuzlukGorusu(Base):
    __tablename__ = 'uygunsuzluk_gorusu'

    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    rapor_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    gorus: Mapped[Optional[String]] = mapped_column(String)
    gorus_karar_fl: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    uygunsuzluk_gorus_bildiren: Mapped[Optional['UygunsuzlukGorusBildiren']] = relationship(back_populates='uygunsuzluk_gorusu')
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(back_populates='uygunsuzluk_gorusu')