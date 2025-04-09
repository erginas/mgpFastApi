from contextlib import asynccontextmanager
from users.database import SessionFactory, execute_raw_sql

# ORM session bağlam yöneticisi
# @asynccontextmanager
# async def get_db():
#     async with SessionFactory() as session:
#         try:
#             yield session
#         finally:
#             await session.close()


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