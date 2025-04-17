from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IzinTalebi(Base):
    __tablename__ = 'izin_talebi'

    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kayit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    sebep_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    baslama_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    izin_suresi: Mapped[Optional[Integer]] = mapped_column(Integer)
    bitis_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    izin_veren: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    fiili_kayit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiili_giris_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiili_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    fiili_cikis_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    onaylayan: Mapped[Optional[Float]] = mapped_column(Float)
    izin_durumu: Mapped[Optional[String]] = mapped_column(String)
    izin_sure_tipi: Mapped[Optional[String]] = mapped_column(String)
    fiili_sure_tipi: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    izin_nedeni: Mapped[Optional[String]] = mapped_column(String)
    vardiya_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    vardiya: Mapped[Optional['Vardiya']] = relationship(back_populates='izin_talebi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='izin_talebi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='izin_talebi')
    kisi_1_2: Mapped[Optional['Kisi']] = relationship(back_populates='izin_talebi')
    izin_sebebi: Mapped[Optional['IzinSebebi']] = relationship(back_populates='izin_talebi')
    kisi_1_2_3: Mapped[Optional['Kisi']] = relationship(back_populates='izin_talebi')