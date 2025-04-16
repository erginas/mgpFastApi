from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.oracle import oracledb

import oracledb as oradb
from contextlib import asynccontextmanager

Base = declarative_base()

# ORM bağlantısı için URL
#ORACLE_URL = f'oracle+oracledb://{"mgp"}:{"mgp"}@{"192.168.0.253/tpsn"}'
ORACLE_URL = f'oracle+oracledb://{"mgp"}:{"mgp"}@{"cloud.tipsan.com:3521/tpsn"}'

# ORM engine ve session
engine = create_async_engine(ORACLE_URL, echo=True, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Asenkron session factory
SessionFactory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


@asynccontextmanager
async def get_raw_connection():
    """Raw SQL bağlantısı oluşturuyor."""
    # Asenkron bağlantıyı açıyoruz
    connection = await oradb.connect_async(
        user="mgp",
        password="mgp",
        dsn="cloud.tipsan.com:3521/tpsn",
        #dsn="192.168.0.253:1521/tpsn",
    )
    try:
        yield connection
    finally:
        await connection.close()