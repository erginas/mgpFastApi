from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UygulamaMenusu(Base):
    __tablename__ = 'uygulama_menusu'

    menu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sinif_adi: Mapped[Optional[String]] = mapped_column(String)
    basligi: Mapped[Optional[String]] = mapped_column(String)
    tanimi: Mapped[Optional[String]] = mapped_column(String)
    ust_menu: Mapped[Optional[Float]] = mapped_column(Float)
    sira: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    uygulama_menusu: Mapped[Optional['UygulamaMenusu']] = relationship(back_populates='uygulama_menusu')