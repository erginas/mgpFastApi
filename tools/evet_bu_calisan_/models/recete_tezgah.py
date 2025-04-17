from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteTezgah(Base):
    __tablename__ = 'recete_tezgah'

    recete_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    tezgah_grup_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    master_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    recete_detay: Mapped[Optional['ReceteDetay']] = relationship(back_populates='recete_tezgah')
    tezgah_grubu: Mapped[Optional['TezgahGrubu']] = relationship(back_populates='recete_tezgah')