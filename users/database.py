from typing import Any

import oracledb
from sqlalchemy import create_engine
from sqlalchemy import text

from fastapi import HTTPException, status
from pydantic import PostgresDsn
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

from .core import config


ORACLE_URL = PostgresDsn.build(
    #scheme="oracle+asyncpg",
    user=config.ORACLE_USER,
    password=config.ORACLE_PASSWORD,
    host=config.ORACLE_HOST,
    port=config.ORACLE_PORT,
    path=f"/{config.ORACLE_DB}",
)


engine = create_async_engine(ORACLE_URL, future=True, echo=True)


SessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    async def save(self, db: AsyncSession):
        """
        :param db:
        :return:
        """
        try:
            db.add(self)
            return await db.commit()
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
            ) from ex

    @classmethod
    async def find_by_id(cls, db: AsyncSession, id: str):
        query = select(cls).where(cls.id == id)
        result = await db.execute(query)
        return result.scalars().first()