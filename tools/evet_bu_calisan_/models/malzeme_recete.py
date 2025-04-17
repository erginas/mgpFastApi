from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeRecete(Base):
    __tablename__ = 'malzeme_recete'

    recete_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    resim_no: Mapped[Optional[String]] = mapped_column(String)
    ust_recete: Mapped[Optional[Float]] = mapped_column(Float)
    sira_no: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme_recete: Mapped[Optional['MalzemeRecete']] = relationship(back_populates='malzeme_recete')