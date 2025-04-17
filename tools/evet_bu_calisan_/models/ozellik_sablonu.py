from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OzellikSablonu(Base):
    __tablename__ = 'ozellik_sablonu'

    grup_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ozellik_sinif_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    gosterim_sirasi: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kod_sirasi: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme_grubu: Mapped[Optional['MalzemeGrubu']] = relationship(back_populates='ozellik_sablonu')
    ozellik_sinifi: Mapped[Optional['OzellikSinifi']] = relationship(back_populates='ozellik_sablonu')