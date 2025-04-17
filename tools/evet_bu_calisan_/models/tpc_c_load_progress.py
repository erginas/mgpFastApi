from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TpcCLoadProgress(Base):
    __tablename__ = 'tpc_c_load_progress'

    tablename: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    version: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    setnumber: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    prop_name: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    prop_value: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)