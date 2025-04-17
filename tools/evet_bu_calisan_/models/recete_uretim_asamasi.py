from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteUretimAsamasi(Base):
    __tablename__ = 'recete_uretim_asamasi'

    asama_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    tercih_onceligi: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    tanim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    recete_no: Mapped[Optional[Float]] = mapped_column(Float)
    operasyon_no: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    recete_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='recete_uretim_asamasi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='recete_uretim_asamasi')
    malzeme_recete: Mapped[Optional['MalzemeRecete']] = relationship(back_populates='recete_uretim_asamasi')
    operasyon: Mapped[Optional['Operasyon']] = relationship(back_populates='recete_uretim_asamasi')