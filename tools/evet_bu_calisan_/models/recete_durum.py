from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteDurum(Base):
    __tablename__ = 'recete_durum'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    durum_tipi: Mapped[Optional[String]] = mapped_column(String)
    istem_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    recete_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    recete: Mapped[Optional['Recete']] = relationship(back_populates='recete_durum')