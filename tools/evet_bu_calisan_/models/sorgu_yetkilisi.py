from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SorguYetkilisi(Base):
    __tablename__ = 'sorgu_yetkilisi'

    sorgu_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    okuma: Mapped[Optional[String]] = mapped_column(String)
    calistirma: Mapped[Optional[String]] = mapped_column(String)
    yazma: Mapped[Optional[String]] = mapped_column(String)
    yetkilendirme: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='sorgu_yetkilisi')
    veri_tabani_sorgusu: Mapped[Optional['VeriTabaniSorgusu']] = relationship(back_populates='sorgu_yetkilisi')