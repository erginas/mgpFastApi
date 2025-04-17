from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemePlani(Base):
    __tablename__ = 'malzeme_plani'

    donem_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    miktar_eldeki: Mapped[Optional[Float]] = mapped_column(Float)
    tarih_eldeki: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    miktar_bloke: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_uretim: Mapped[Optional[Float]] = mapped_column(Float)
    tarih_uretim: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    miktar_emniyet_1: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_emniyet_2: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_hesap: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_hedef: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_oncelikli_hedef: Mapped[Optional[Float]] = mapped_column(Float)
    oncelik: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    bitis_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    surum: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    miktar_fasonda: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_fasona: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_satinalma: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_satinalinacak: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_is_emri: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_acilmamis_ie: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_bekleme_bolgesi: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_iptal: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_bek_bol_cikilan: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='malzeme_plani')
    plan_donemi: Mapped[Optional['PlanDonemi']] = relationship(back_populates='malzeme_plani')