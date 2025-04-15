# dependencies.py
import logging
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from core.database import SessionFactory

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
        dsn="cloud.tipsan.com:3521/tpsn",
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
