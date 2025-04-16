import asyncio
from Modules.kisi.crud import kisi_listesi  # Fonksiyonlarınızı içe aktarın

async def test_kisi_listesi():
    try:
        result = await kisi_listesi()
        print("Kişi Listesi:", result)
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    asyncio.run(test_kisi_listesi())