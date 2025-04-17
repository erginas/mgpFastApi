from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Operasyon(Base):
    __tablename__ = 'operasyon'

    operasyon_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ust_operasyon: Mapped[Optional[Float]] = mapped_column(Float)
    isleme_sinifi: Mapped[Optional[String]] = mapped_column(String)
    bilgisayarli_fl: Mapped[Optional[String]] = mapped_column(String)
    tezgah_fl: Mapped[Optional[String]] = mapped_column(String)
    personel_fl: Mapped[Optional[String]] = mapped_column(String)
    recete_bagimsiz: Mapped[Optional[String]] = mapped_column(String)
    iscilik_maliyeti: Mapped[Optional[Float]] = mapped_column(Float)
    firma_ister_fl: Mapped[Optional[String]] = mapped_column(String)
    recete_olustururken_gosterme: Mapped[Optional[Integer]] = mapped_column(Integer)
    vakum_ister: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    operasyon: Mapped[Optional['Operasyon']] = relationship(back_populates='operasyon')