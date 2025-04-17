from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KitaplarKitap(Base):
    __tablename__ = 'kitaplar_kitap'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    isim: Mapped[Optional[String]] = mapped_column(String)
    yazar: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    yaratilma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    guncellenme_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    yayin_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)