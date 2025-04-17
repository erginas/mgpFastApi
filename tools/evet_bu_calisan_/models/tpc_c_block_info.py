from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TpcCBlockInfo(Base):
    __tablename__ = 'tpc_c_block_info'

    tablename: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    current_block: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    max_block: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)