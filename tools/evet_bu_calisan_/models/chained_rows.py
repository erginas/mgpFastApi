from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ChainedRows(Base):
    __tablename__ = 'chained_rows'

    owner_name: Mapped[Optional[String]] = mapped_column(String)
    table_name: Mapped[Optional[String]] = mapped_column(String)
    cluster_name: Mapped[Optional[String]] = mapped_column(String)
    partition_name: Mapped[Optional[String]] = mapped_column(String)
    subpartition_name: Mapped[Optional[String]] = mapped_column(String)
    head_rowid: Mapped[Optional[String]] = mapped_column(String)
    analyze_timestamp: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
