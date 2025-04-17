from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteMalzeme(Base):
    __tablename__ = 'recete_malzeme'

    recete_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    sira_no: Mapped[Optional[Float]] = mapped_column(Float)
    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    master_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    detay_stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    detay_operasyon_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='recete_malzeme')
    recete_detay: Mapped[Optional['ReceteDetay']] = relationship(back_populates='recete_malzeme')