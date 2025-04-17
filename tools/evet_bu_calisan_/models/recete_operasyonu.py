from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteOperasyonu(Base):
    __tablename__ = 'recete_operasyonu'

    recete_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kayit_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    operasyon_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ozel_not: Mapped[Optional[String]] = mapped_column(String)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    resim_no: Mapped[Optional[String]] = mapped_column(String)
    sure_formulu: Mapped[Optional[String]] = mapped_column(String)
    parca: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    resim_grubu: Mapped[Optional[String]] = mapped_column(String)
    tr_sira_no: Mapped[Optional[String]] = mapped_column(String)
    grup_no: Mapped[Optional[Float]] = mapped_column(Float)
    kisa_kodu: Mapped[Optional[String]] = mapped_column(String)
    fason_maliyeti: Mapped[Optional[Float]] = mapped_column(Float)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    uretim_aciklamasi: Mapped[Optional[String]] = mapped_column(String)
    kalite_aciklamasi: Mapped[Optional[String]] = mapped_column(String)
    recete_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    para_birimi: Mapped[Optional['ParaBirimi']] = relationship(back_populates='recete_operasyonu')
    operasyon: Mapped[Optional['Operasyon']] = relationship(back_populates='recete_operasyonu')
    malzeme_recete: Mapped[Optional['MalzemeRecete']] = relationship(back_populates='recete_operasyonu')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='recete_operasyonu')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='recete_operasyonu')
    tezgah_grubu: Mapped[Optional['TezgahGrubu']] = relationship(back_populates='recete_operasyonu')
    tb_resim_tbl: Mapped[Optional['TbResimTbl']] = relationship(back_populates='recete_operasyonu')