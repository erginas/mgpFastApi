from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UretimEmriTipi(Base):
    __tablename__ = 'uretim_emri_tipi'

    uretim_emri_tip_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    acik_nesne: Mapped[Optional[String]] = mapped_column(String)
    tamir_malzeme_fl: Mapped[Optional[String]] = mapped_column(String)
    tamir_lot_fl: Mapped[Optional[String]] = mapped_column(String)
    uretim_malzeme_fl: Mapped[Optional[String]] = mapped_column(String)
    uretim_lot_fl: Mapped[Optional[String]] = mapped_column(String)
    gerekcesi: Mapped[Optional[String]] = mapped_column(String)
    oncelik: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)