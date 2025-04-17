from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SkPlanOlcusu(Base):
    __tablename__ = 'sk_plan_olcusu'

    olcu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sk_plan_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    sk_plani: Mapped[Optional['SkPlani']] = relationship(back_populates='sk_plan_olcusu')
    sk_olcusu: Mapped[Optional['SkOlcusu']] = relationship(back_populates='sk_plan_olcusu')