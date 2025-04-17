from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class StokDurum(Base):
    __tablename__ = 'stok_durum'

    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    ce_bilgisi: Mapped[Optional[String]] = mapped_column(String)
    son_kullanma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    giren_miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    cikan_miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    kalan_miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    depo: Mapped[Optional['Depo']] = relationship(back_populates='stok_durum')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='stok_durum')