from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UrunAlternatifi(Base):
    __tablename__ = 'urun_alternatifi'

    asama_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    temel_malzeme: Mapped[Optional[Integer]] = mapped_column(Integer)
    nedeni: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    giris_cikis_fl: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Float]] = mapped_column(Float)
    tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='urun_alternatifi')
    uretim_asamasi: Mapped[Optional['UretimAsamasi']] = relationship(back_populates='urun_alternatifi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='urun_alternatifi')
    malzeme_1: Mapped[Optional['Malzeme']] = relationship(back_populates='urun_alternatifi')