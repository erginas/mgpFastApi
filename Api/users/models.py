import uuid
from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlalchemy import select, Column, String, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Base
from users.core.hash import verify_password
from users.utils import utcnow




class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(unique=True, index=True)
    full_name: Mapped[str]
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
        onupdate=datetime.utcnow
    )

    # DÜZENLENEN ALANLAR:
    profile_path: Mapped[Optional[str]] = mapped_column(nullable=True)
    title: Mapped[Optional[str]] = mapped_column(nullable=True)

    @classmethod
    async def find_by_email(cls, db: AsyncSession, email: str):
        stmt = select(cls).filter(cls.email == email)
        result = await db.execute(stmt)
        return result.scalars().first()

    @classmethod
    async def authenticate(cls, db: AsyncSession, email: str, password: str):
        user = await cls.find_by_email(db=db, email=email)
        if not user or not verify_password(password, user.password):
            return False
        return user

    @classmethod
    async def find_by_id(cls, db: AsyncSession, id: UUID):
        result = await db.execute(select(cls).where(cls.id == id))
        return result.scalar_one_or_none()

    async def save(self, db):
        db.add(self)
        await db.commit()
        await db.refresh(self)

    # class Config:
    #     orm_mode = True

class BlackListToken(Base):
    __tablename__ = "blacklisttokens"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    expire: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(server_default=utcnow())

    @classmethod
    async def find_by_id(cls, db: AsyncSession, id: str):
        query = select(cls).where(cls.id == id)
        result = await db.execute(query)
        return result.scalars().first()

