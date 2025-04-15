# core/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

ORACLE_URL = "oracle+oracledb://mgp:mgp@cloud.tipsan.com:3521/tpsn"

# Async SQLAlchemy engine
engine = create_async_engine(ORACLE_URL, echo=True, pool_size=10, max_overflow=20)

# Async session factory
SessionFactory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)