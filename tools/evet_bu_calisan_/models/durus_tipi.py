from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DurusTipi(Base):
    __tablename__ = 'durus_tipi'

    durus_detay_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kullanim_alani: Mapped[Optional[String]] = mapped_column(String)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)