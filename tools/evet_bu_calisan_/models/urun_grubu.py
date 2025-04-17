from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UrunGrubu(Base):
    __tablename__ = 'urun_grubu'

    urun_grup_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ust_grup: Mapped[Optional[Float]] = mapped_column(Float)
    adi: Mapped[Optional[String]] = mapped_column(String)
    grup_kodu: Mapped[Optional[String]] = mapped_column(String)
    analiz_fl: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    urun_grubu: Mapped[Optional['UrunGrubu']] = relationship(back_populates='urun_grubu')