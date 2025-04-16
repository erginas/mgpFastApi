import asyncio

from core.database import get_raw_connection


async def test_get_raw_connection():
    try:
        async with get_raw_connection() as connection:
            print("Bağlantı başarıyla alındı:", connection)
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    asyncio.run(test_get_raw_connection())