from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Depo(Base):
    __tablename__ = 'depo'

    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    e_kodu: Mapped[Optional[String]] = mapped_column(String)
    rengi: Mapped[Optional[Float]] = mapped_column(Float)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String)
    emniyet_stok_fl: Mapped[Optional[String]] = mapped_column(String)
    davranis_sekli: Mapped[Optional[Float]] = mapped_column(Float)
    ce_bilgisi: Mapped[Optional[String]] = mapped_column(String)
    uygunsuzluk_bilgisi: Mapped[Optional[String]] = mapped_column(String)
    karsi_hareket: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)