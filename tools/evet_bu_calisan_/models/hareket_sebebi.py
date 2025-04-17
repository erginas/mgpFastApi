from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HareketSebebi(Base):
    __tablename__ = 'hareket_sebebi'

    hareket_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    giris_cikis_fl: Mapped[Optional[String]] = mapped_column(String)
    davranis_sekli: Mapped[Optional[String]] = mapped_column(String)
    e_kodu: Mapped[Optional[String]] = mapped_column(String)
    imza_ister_fl: Mapped[Optional[String]] = mapped_column(String)
    class_name: Mapped[Optional[String]] = mapped_column(String)
    karsi_hareket_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    goster_fl: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    hareket_sebebi: Mapped[Optional['HareketSebebi']] = relationship(back_populates='hareket_sebebi')