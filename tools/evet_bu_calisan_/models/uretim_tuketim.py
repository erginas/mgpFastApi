from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UretimTuketim(Base):
    __tablename__ = 'uretim_tuketim'

    asama_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    uretim_tuketim_fl: Mapped[Optional[String]] = mapped_column(String)
    giris_cikis_fl: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Float]] = mapped_column(Float)
    tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    nedeni: Mapped[Optional[String]] = mapped_column(String)
    birimi: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    boy: Mapped[Optional[Float]] = mapped_column(Float)
    en: Mapped[Optional[Float]] = mapped_column(Float)
    cap: Mapped[Optional[Float]] = mapped_column(Float)
    recete_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    yeni: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    uretim_asamasi: Mapped[Optional['UretimAsamasi']] = relationship(back_populates='uretim_tuketim')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='uretim_tuketim')
    malzeme_birimi: Mapped[Optional['MalzemeBirimi']] = relationship(back_populates='uretim_tuketim')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uretim_tuketim')