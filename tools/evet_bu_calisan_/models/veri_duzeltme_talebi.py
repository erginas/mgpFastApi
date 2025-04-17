from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VeriDuzeltmeTalebi(Base):
    __tablename__ = 'veri_duzeltme_talebi'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    veri_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kayit_yili: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kayit_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    hata_sebebi: Mapped[Optional[String]] = mapped_column(String)
    yapilacak_islem: Mapped[Optional[String]] = mapped_column(String)
    duzenleyen: Mapped[Optional[Float]] = mapped_column(Float)
    duzenleme_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    onaylayan: Mapped[Optional[Float]] = mapped_column(Float)
    onaylama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    duzelten: Mapped[Optional[Float]] = mapped_column(Float)
    duzeltme_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kontrollu_kayit: Mapped[Optional['KontrolluKayit']] = relationship(back_populates='veri_duzeltme_talebi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='veri_duzeltme_talebi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='veri_duzeltme_talebi')
    kisi_1_2: Mapped[Optional['Kisi']] = relationship(back_populates='veri_duzeltme_talebi')
    kisi_1_2_3: Mapped[Optional['Kisi']] = relationship(back_populates='veri_duzeltme_talebi')