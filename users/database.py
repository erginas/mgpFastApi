from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.oracle import oracledb
from .core import config

Base = declarative_base()

# ORM bağlantısı için URL
ORACLE_URL = f'oracle+oracledb://{"mgp"}:{"mgp"}@{"192.168.0.253/tpsn"}'

# ORM engine ve session
engine = create_async_engine(ORACLE_URL, echo=True, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Asenkron session factory
SessionFactory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)



# Raw SQL bağlantısı
async def get_raw_connection():
    """Raw SQL bağlantısı oluşturuyor."""
    connection = await oracledb.connect(
        user="mgp",
        password="mgp",
        dsn="192.168.0.253/tpsn",
        async_=True  # Asenkron bağlantı
    )
    return connection


async def execute_raw_sql(query: str, params: dict = None):
    """Raw SQL sorgusunu çalıştır."""
    connection = await get_raw_connection()
    try:
        cursor = await connection.cursor()
        await cursor.execute(query, params)
        result = await cursor.fetchall()  # Sonuçları al
        return result
    finally:
        await cursor.close()
        await connection.close()