from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IsEmriPlanlananAdim(Base):
    __tablename__ = 'is_emri_planlanan_adim'

    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adim_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    tezgah_no: Mapped[Optional[String]] = mapped_column(String)
    operasyon_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    pl_bas_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    pl_bit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    pl_miktar: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    teknik_dokuman: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    tezgah: Mapped[Optional['Tezgah']] = relationship(back_populates='is_emri_planlanan_adim')
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='is_emri_planlanan_adim')
    operasyon: Mapped[Optional['Operasyon']] = relationship(back_populates='is_emri_planlanan_adim')