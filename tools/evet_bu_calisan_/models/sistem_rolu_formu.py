from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SistemRoluFormu(Base):
    __tablename__ = 'sistem_rolu_formu'

    sistem_rol_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    menu_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    sistem_rolu: Mapped[Optional['SistemRolu']] = relationship(back_populates='sistem_rolu_formu')
    uygulama_menusu: Mapped[Optional['UygulamaMenusu']] = relationship(back_populates='sistem_rolu_formu')