from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Tezgah(Base):
    __tablename__ = 'tezgah'

    tezgah_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    org_birimi: Mapped[Optional[String]] = mapped_column(String)
    grup_no: Mapped[Optional[Float]] = mapped_column(Float)
    diagram_no: Mapped[Optional[Float]] = mapped_column(Float)
    x_pos: Mapped[Optional[Float]] = mapped_column(Float)
    y_pos: Mapped[Optional[Float]] = mapped_column(Float)
    cap: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ilk_calisma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    guc: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='tezgah')
    tezgah_grubu: Mapped[Optional['TezgahGrubu']] = relationship(back_populates='tezgah')