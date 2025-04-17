from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteIliski(Base):
    __tablename__ = 'recete_iliski'

    ana_recete_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    iliskili_recete_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    detay_parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    detay_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    recete: Mapped[Optional['Recete']] = relationship(back_populates='recete_iliski')
    recete_1: Mapped[Optional['Recete']] = relationship(back_populates='recete_iliski')
    recete_detay: Mapped[Optional['ReceteDetay']] = relationship(back_populates='recete_iliski')