from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Firma(Base):
    __tablename__ = 'firma'

    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    unvani: Mapped[Optional[String]] = mapped_column(String)
    adresi: Mapped[Optional[String]] = mapped_column(String)
    tel: Mapped[Optional[String]] = mapped_column(String)
    fax: Mapped[Optional[String]] = mapped_column(String)
    eposta: Mapped[Optional[String]] = mapped_column(String)
    url: Mapped[Optional[String]] = mapped_column(String)
    ic_dis_fl: Mapped[Optional[String]] = mapped_column(String)
    satici_fl: Mapped[Optional[String]] = mapped_column(String)
    alici_fl: Mapped[Optional[String]] = mapped_column(String)
    bayi_fl: Mapped[Optional[String]] = mapped_column(String)
    vergi_dairesi: Mapped[Optional[String]] = mapped_column(String)
    vergi_no: Mapped[Optional[String]] = mapped_column(String)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String)
    ulke: Mapped[Optional[String]] = mapped_column(String)
    onay_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    ilgili_kisi: Mapped[Optional[String]] = mapped_column(String)
    cari_kodu: Mapped[Optional[String]] = mapped_column(String)
    il: Mapped[Optional[String]] = mapped_column(String)
    ilce: Mapped[Optional[String]] = mapped_column(String)
    uts_tanimlayici_no: Mapped[Optional[String]] = mapped_column(String)
    uts_unvan: Mapped[Optional[String]] = mapped_column(String)
    uts_durum: Mapped[Optional[String]] = mapped_column(String)
    uts_mersis_no: Mapped[Optional[String]] = mapped_column(String)
    uts_ckys_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='firma')