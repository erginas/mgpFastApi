from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteOzelligi(Base):
    __tablename__ = 'recete_ozelligi'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    master_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    sinif_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    operasyon_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    yari_mamul: Mapped[Optional[Integer]] = mapped_column(Integer)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    boy: Mapped[Optional[Integer]] = mapped_column(Integer)
    en: Mapped[Optional[Integer]] = mapped_column(Integer)
    cap: Mapped[Optional[Integer]] = mapped_column(Integer)
    birimi: Mapped[Optional[String]] = mapped_column(String)
    temin_sekli: Mapped[Optional[String]] = mapped_column(String)
    teknik_resim_no: Mapped[Optional[String]] = mapped_column(String)
    net_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)