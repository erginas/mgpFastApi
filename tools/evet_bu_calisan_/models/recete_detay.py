from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteDetay(Base):
    __tablename__ = 'recete_detay'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    recete_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    adi: Mapped[Optional[String]] = mapped_column(String)
    operasyon_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    teknik_resim_no: Mapped[Optional[String]] = mapped_column(String)
    tezgah_grup_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    net_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    alt_recete_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    yari_mamul: Mapped[Optional[Integer]] = mapped_column(Integer)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    boy: Mapped[Optional[Integer]] = mapped_column(Integer)
    en: Mapped[Optional[Integer]] = mapped_column(Integer)
    cap: Mapped[Optional[Integer]] = mapped_column(Integer)
    birimi: Mapped[Optional[String]] = mapped_column(String)
    temin_sekli: Mapped[Optional[String]] = mapped_column(String)
    temp_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    temp_parent: Mapped[Optional[Integer]] = mapped_column(Integer)
    master_operasyon_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    bilesen: Mapped[Optional[Float]] = mapped_column(Float)
    master_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='recete_detay')
    recete: Mapped[Optional['Recete']] = relationship(back_populates='recete_detay')