from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UbbTransfer(Base):
    __tablename__ = 'ubb_transfer'

    stok_kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    c09_ubb_kodu: Mapped[Optional[String]] = mapped_column(String)
    c35_unspsc_kodu: Mapped[Optional[String]] = mapped_column(String)
    c36_unspsc_adi: Mapped[Optional[String]] = mapped_column(String)
    c10_ambalaj_turu: Mapped[Optional[String]] = mapped_column(String)
    c18_ambalaj_miktar: Mapped[Optional[String]] = mapped_column(String)
    c19_ambalaj_birimi: Mapped[Optional[String]] = mapped_column(String)
    c20_genislik: Mapped[Optional[String]] = mapped_column(String)
    c21_yukseklik: Mapped[Optional[String]] = mapped_column(String)
    c22_derinlik: Mapped[Optional[String]] = mapped_column(String)
    c02_gmdn_kodu: Mapped[Optional[String]] = mapped_column(String)
    c32_gmdn_adi: Mapped[Optional[String]] = mapped_column(String)
    c40_ubb_kayit_tarihi: Mapped[Optional[String]] = mapped_column(String)
    c41_brans_kodu: Mapped[Optional[String]] = mapped_column(String)
    c42_brans_adi: Mapped[Optional[String]] = mapped_column(String)
    c37_ubb_kayitli: Mapped[Optional[String]] = mapped_column(String)
    mlz_no: Mapped[Optional[Float]] = mapped_column(Float)
    c12_ubb_adi: Mapped[Optional[String]] = mapped_column(String)
    c00_kok_urun: Mapped[Optional[String]] = mapped_column(String)
    fiyat: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)