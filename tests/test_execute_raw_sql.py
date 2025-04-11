import asyncio
import logging

from Modules.kisi.crud import kisi_listesi
#from core.database import execute_raw_sql  # Fonksiyonlarınızı içe aktarın

from core.dependencies import execute_raw_sql

# async def test_execute_raw_sql():
#     query = "SELECT * FROM Kisi WHERE id = :id"
#     params = {"id": 101}
#     result = await execute_raw_sql(query, params)
#     print("execute_raw_sql Sonucu:", result)
#
# async def test_kisi_listesi():
#     result = await kisi_listesi()
#     print("kisi_listesi Sonucu:", result)
#
# # Asenkron testleri çalıştır
# if __name__ == "__main__":
#     asyncio.run(test_execute_raw_sql())
#     asyncio.run(test_kisi_listesi())


# Log ayarları
logging.basicConfig(level=logging.DEBUG)


async def test_execute_raw_sql():
    query = "SELECT * FROM Kisi WHERE id = :id"
    params = {"id": 101}
    try:
        result = await execute_raw_sql(query, params)
        print("execute_raw_sql Sonucu:", result)
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    asyncio.run(test_execute_raw_sql())




