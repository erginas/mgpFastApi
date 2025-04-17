from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TedarikciDegerlendirmesi(Base):
    __tablename__ = 'tedarikci_degerlendirmesi'

    kriter_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    giris_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    degeri: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    gecici_stok: Mapped[Optional['GeciciStok']] = relationship(back_populates='tedarikci_degerlendirmesi')
    degerlendirme_kriteri: Mapped[Optional['DegerlendirmeKriteri']] = relationship(back_populates='tedarikci_degerlendirmesi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='tedarikci_degerlendirmesi')