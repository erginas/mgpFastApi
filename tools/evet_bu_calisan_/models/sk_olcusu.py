from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SkOlcusu(Base):
    __tablename__ = 'sk_olcusu'

    olcu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    tipi: Mapped[Optional[String]] = mapped_column(String)
    kontrol_grubu: Mapped[Optional[String]] = mapped_column(String)
    control_group: Mapped[Optional[String]] = mapped_column(String)
    name: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)