from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UretimTakipSistemi(Base):
    __tablename__ = 'uretim_takip_sistemi'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    hareket_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    uretim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bildirim_tipi: Mapped[Optional[String]] = mapped_column(String)
    bildirim_no: Mapped[Optional[String]] = mapped_column(String)
    bildirim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kaydeden_kimlik: Mapped[Optional[Integer]] = mapped_column(Integer)
    iptal_eden: Mapped[Optional[Integer]] = mapped_column(Integer)
    g_c: Mapped[Optional[String]] = mapped_column(String)
    paket_no: Mapped[Optional[String]] = mapped_column(String)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    iptal_no: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    tekrar_bildir: Mapped[Optional[Integer]] = mapped_column(Integer)
    bildirim_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    als_fatura_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    kayit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis_fatura_detay: Mapped[Optional['AlinanSiparisFaturaDetay']] = relationship(back_populates='uretim_takip_sistemi')
    uretim_takip_sistemi: Mapped[Optional['UretimTakipSistemi']] = relationship(back_populates='uretim_takip_sistemi')
    malzeme_hareketi: Mapped[Optional['MalzemeHareketi']] = relationship(back_populates='uretim_takip_sistemi')