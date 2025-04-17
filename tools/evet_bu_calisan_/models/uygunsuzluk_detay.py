from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UygunsuzlukDetay(Base):
    __tablename__ = 'uygunsuzluk_detay'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    rapor_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    parti_no: Mapped[Optional[String]] = mapped_column(String)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    konu: Mapped[Optional[String]] = mapped_column(String)
    parti_miktari: Mapped[Optional[Float]] = mapped_column(Float)
    uygunsuzluk_miktari: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    isemri_no: Mapped[Optional[String]] = mapped_column(String)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    hareket_no: Mapped[Optional[Float]] = mapped_column(Float)
    dof_no: Mapped[Optional[String]] = mapped_column(String)
    diger_ref_no: Mapped[Optional[String]] = mapped_column(String)
    fonksiyon: Mapped[Optional[String]] = mapped_column(String)
    tespit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tespit_yeri: Mapped[Optional[String]] = mapped_column(String)
    kk_lot_no: Mapped[Optional[String]] = mapped_column(String)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='uygunsuzluk_detay')
    uygunsuzluk: Mapped[Optional['Uygunsuzluk']] = relationship(back_populates='uygunsuzluk_detay')
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='uygunsuzluk_detay')
    malzeme_hareketi: Mapped[Optional['MalzemeHareketi']] = relationship(back_populates='uygunsuzluk_detay')