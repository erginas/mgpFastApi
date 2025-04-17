from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IsEmriOperasyonuChecklist(Base):
    __tablename__ = 'is_emri_operasyonu_checklist'

    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    islem_sirasi: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    operasyon_no: Mapped[Optional[Float]] = mapped_column(Float)
    check_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    olcu_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    sk_plan_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    paraf: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    is_emri_operasyonu: Mapped[Optional['IsEmriOperasyonu']] = relationship(back_populates='is_emri_operasyonu_checklist')
    operasyon_checklist: Mapped[Optional['OperasyonChecklist']] = relationship(back_populates='is_emri_operasyonu_checklist')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='is_emri_operasyonu_checklist')
    sk_plan_olcusu: Mapped[Optional['SkPlanOlcusu']] = relationship(back_populates='is_emri_operasyonu_checklist')