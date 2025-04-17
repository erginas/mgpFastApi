from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DovizKuru(Base):
    __tablename__ = 'doviz_kuru'

    gecerlilik_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    para_birimi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    temel_para_birimi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    kayit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kur: Mapped[Optional[Float]] = mapped_column(Float)
    doviz_alis: Mapped[Optional[Float]] = mapped_column(Float)
    doviz_satis: Mapped[Optional[Float]] = mapped_column(Float)
    efektif_alis: Mapped[Optional[Float]] = mapped_column(Float)
    efektif_satis: Mapped[Optional[Float]] = mapped_column(Float)
    katsayi: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    para_birimi: Mapped[Optional['ParaBirimi']] = relationship(back_populates='doviz_kuru')
    para_birimi_1: Mapped[Optional['ParaBirimi']] = relationship(back_populates='doviz_kuru')