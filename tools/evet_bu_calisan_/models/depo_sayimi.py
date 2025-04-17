from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DepoSayimi(Base):
    __tablename__ = 'depo_sayimi'

    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    lot_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    ilk_miktar: Mapped[Optional[Float]] = mapped_column(Float)
    son_miktar: Mapped[Optional[Float]] = mapped_column(Float)
    ilk_hareket: Mapped[Optional[Float]] = mapped_column(Float)
    son_hareket: Mapped[Optional[Float]] = mapped_column(Float)
    ilk_zaman: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    son_zaman: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    sayilan_miktar: Mapped[Optional[Float]] = mapped_column(Float)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    son_kullanma_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ce_fl: Mapped[Optional[String]] = mapped_column(String)
    bt_note: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='depo_sayimi')
    depo: Mapped[Optional['Depo']] = relationship(back_populates='depo_sayimi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='depo_sayimi')