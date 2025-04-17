from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RolePermissions(Base):
    __tablename__ = 'role_permissions'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    role_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    permission_id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    permission: Mapped[Optional['Permission']] = relationship(back_populates='role_permissions')
    role: Mapped[Optional['Role']] = relationship(back_populates='role_permissions')