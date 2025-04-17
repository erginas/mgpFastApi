from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ValidasyonDetay(Base):
    __tablename__ = 'validasyon_detay'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kts: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    kk_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    menu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    onay_durumu: Mapped[Optional[Float]] = mapped_column(Float)
    ust_menu: Mapped[Optional[Float]] = mapped_column(Float)
    validasyon_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='validasyon_detay')
    uygulama_menusu: Mapped[Optional['UygulamaMenusu']] = relationship(back_populates='validasyon_detay')
    kodlar: Mapped[Optional['Kodlar']] = relationship(back_populates='validasyon_detay')
    uygulama_menusu_1: Mapped[Optional['UygulamaMenusu']] = relationship(back_populates='validasyon_detay')
    validasyon: Mapped[Optional['Validasyon']] = relationship(back_populates='validasyon_detay')