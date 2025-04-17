from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KitaplarYorum(Base):
    __tablename__ = 'kitaplar_yorum'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yorum: Mapped[Optional[String]] = mapped_column(String)
    yaratilma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    guncellenme_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    degerlendirme: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kitap_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yorum_sahibi_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kitaplar_kitap: Mapped[Optional['KitaplarKitap']] = relationship(back_populates='kitaplar_yorum')