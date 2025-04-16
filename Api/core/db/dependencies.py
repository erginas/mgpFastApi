# dependencies.py
import logging
from contextlib import asynccontextmanager

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text
from starlette import status

from core.db.database import SessionFactory
import oracledb as oradb

# Log ayarları
logging.basicConfig(level=logging.DEBUG)

# ORM Session
async def get_session() -> AsyncSession:
    async with SessionFactory() as session:
        yield session

# Raw bağlantı
@asynccontextmanager
async def get_raw_connection():
    """Raw Oracle bağlantısı (oracledb)"""
    connection = await oradb.connect_async(
        user="mgp",
        password="mgp",
        dsn="192.168.0.253/tpsn",
        # dsn="cloud.tipsan.com:3521/tpsn",
    )
    try:
        yield connection
    finally:
        await connection.close()

# Raw SQL Executor
async def execute_raw_sql(query: str, params: dict = None, fetch_all: bool = True):
    async with get_raw_connection() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(query, params or {})

            if fetch_all:
                columns = [col[0].upper() for col in cursor.description]
                rows = await cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
            else:
                await connection.commit()
                return None


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

async def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        await db.close()