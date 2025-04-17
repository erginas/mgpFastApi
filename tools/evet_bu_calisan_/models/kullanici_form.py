from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KullaniciForm(Base):
    __tablename__ = 'kullanici_form'

    kullanici_kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    menu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kullanici: Mapped[Optional['Kullanici']] = relationship(back_populates='kullanici_form')
    uygulama_menusu: Mapped[Optional['UygulamaMenusu']] = relationship(back_populates='kullanici_form')