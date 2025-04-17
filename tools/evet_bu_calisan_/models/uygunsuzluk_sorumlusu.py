from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UygunsuzlukSorumlusu(Base):
    __tablename__ = 'uygunsuzluk_sorumlusu'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    rapor_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    karar_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sorumlu_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    hata_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adet: Mapped[Optional[Float]] = mapped_column(Float)
    hatayi_yapan: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    tezgah_no: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    uygunsuzluk_karari: Mapped[Optional['UygunsuzlukKarari']] = relationship(back_populates='uygunsuzluk_sorumlusu')
    hata_kodlari: Mapped[Optional['HataKodlari']] = relationship(back_populates='uygunsuzluk_sorumlusu')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uygunsuzluk_sorumlusu')
    firma: Mapped[Optional['Firma']] = relationship(back_populates='uygunsuzluk_sorumlusu')
    tezgah: Mapped[Optional['Tezgah']] = relationship(back_populates='uygunsuzluk_sorumlusu')