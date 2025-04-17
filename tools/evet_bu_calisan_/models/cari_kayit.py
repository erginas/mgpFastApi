from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CariKayit(Base):
    __tablename__ = 'cari_kayit'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    araci_firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iade_yil: Mapped[Optional[Float]] = mapped_column(Float)
    iade_ay: Mapped[Optional[Float]] = mapped_column(Float)
    iade_fis_no: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_yil: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_ay: Mapped[Optional[Float]] = mapped_column(Float)
    siparis_no: Mapped[Optional[Float]] = mapped_column(Float)
    banka_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    hesap_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    vade_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tutar: Mapped[Optional[Float]] = mapped_column(Float)
    kredi_bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    islem_gerekcesi: Mapped[Optional[Float]] = mapped_column(Float)
    borc_alacak_fl: Mapped[Optional[String]] = mapped_column(String)
    islem_ref_belge: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='cari_kayit')
    firma_1: Mapped[Optional['Firma']] = relationship(back_populates='cari_kayit')
    para_birimi: Mapped[Optional['ParaBirimi']] = relationship(back_populates='cari_kayit')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='cari_kayit')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='cari_kayit')
    alinan_iade: Mapped[Optional['AlinanIade']] = relationship(back_populates='cari_kayit')
    alinan_siparis: Mapped[Optional['AlinanSiparis']] = relationship(back_populates='cari_kayit')
    banka_hesabi: Mapped[Optional['BankaHesabi']] = relationship(back_populates='cari_kayit')
