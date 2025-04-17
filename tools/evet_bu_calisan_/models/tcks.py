from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Tcks(Base):
    __tablename__ = 'tcks'

    bm_sk: Mapped[Optional[String]] = mapped_column(String)
    bm_tanim: Mapped[Optional[String]] = mapped_column(String)
    bm_yeni_tanim: Mapped[Optional[String]] = mapped_column(String)
    bm_ozellik: Mapped[Optional[String]] = mapped_column(String)
    tp_sk: Mapped[Optional[String]] = mapped_column(String)
    tp_tanim: Mapped[Optional[String]] = mapped_column(String)
    tp_etiket: Mapped[Optional[String]] = mapped_column(String)
    ems_kodu: Mapped[Optional[String]] = mapped_column(String)
    gmdn_kategori: Mapped[Optional[Float]] = mapped_column(Float)
    gmdn_bolum: Mapped[Optional[Float]] = mapped_column(Float)
    gmdn_kod: Mapped[Optional[Float]] = mapped_column(Float)
    tp_katalog: Mapped[Optional[String]] = mapped_column(String)
    bm_tp_tanim: Mapped[Optional[String]] = mapped_column(String)
    ems_sira: Mapped[Optional[Float]] = mapped_column(Float)
    liste_disi: Mapped[Optional[String]] = mapped_column(String)
    gmdn: Mapped[Optional[String]] = mapped_column(String)
    ce_sinifi: Mapped[Optional[String]] = mapped_column(String)
    bm_durum: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)