from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeFiyati(Base):
    __tablename__ = 'malzeme_fiyati'

    tarife_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    gecerlilik_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String)
    birim_fiyati: Mapped[Optional[Float]] = mapped_column(Float)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ems_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiyat_tarifesi: Mapped[Optional['FiyatTarifesi']] = relationship(back_populates='malzeme_fiyati')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='malzeme_fiyati')
    para_birimi: Mapped[Optional['ParaBirimi']] = relationship(back_populates='malzeme_fiyati')