from contextlib import asynccontextmanager
from core.database import SessionFactory, execute_raw_sql


async def get_db():
    async with SessionFactory() as session:
        yield session


# Raw SQL bağlam yöneticisi (Opsiyonel)
@asynccontextmanager
async def get_raw_db():
    connection = await execute_raw_sql("SELECT 1 FROM DUAL")  # Sadece örnek, test etmek için basit bir sorgu
    try:
        yield connection
    finally:
        await connection.close()