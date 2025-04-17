from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GeciciStokDetay(Base):
    __tablename__ = 'gecici_stok_detay'

    giris_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    malzeme_adi: Mapped[Optional[String]] = mapped_column(String)
    miktar_gelen: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_red: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_sartli: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_kabul: Mapped[Optional[Float]] = mapped_column(Float)
    giris_kk_rapor_no: Mapped[Optional[String]] = mapped_column(String)
    aktarilan_sartli: Mapped[Optional[Float]] = mapped_column(Float)
    aktarilan_kabul: Mapped[Optional[Float]] = mapped_column(Float)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    hareket_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    birimi: Mapped[Optional[String]] = mapped_column(String)
    uretici_lot_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    hareket_sebebi: Mapped[Optional['HareketSebebi']] = relationship(back_populates='gecici_stok_detay')
    gecici_stok: Mapped[Optional['GeciciStok']] = relationship(back_populates='gecici_stok_detay')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='gecici_stok_detay')