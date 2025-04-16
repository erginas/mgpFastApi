from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from core.dependencies import  execute_raw_sql
from .models import Kisi

from fastapi import HTTPException, Query
from sqlalchemy import text
from typing import List, Optional
import logging

app = FastAPI()

# Log ayarları
logging.basicConfig(level=logging.DEBUG)


async def kisi_listesi(
        adi: Optional[str] = Query(None, description="Kişinin adı"),
        soyadi: Optional[str] = Query(None, description="Kişinin soyadı"),
        kimlik_no: Optional[int] = Query(None, description="Kişinin Kimlik Numarası"),
        page: int = Query(1, ge=1, description="Sayfa numarası"),
        limit: int = Query(10, ge=1, le=100, description="Her sayfada gösterilecek kayıt sayısı")
) -> List[Kisi]:

    try:
        # Temel sorgu
        query = "SELECT * FROM Kisi WHERE 1=1"
        params = {}

        # Filtreleme parametreleri
        if adi:
            query += " AND ADI = :adi"
            params["adi"] = adi

        if soyadi:
            query += " AND SOYADI = :soyadi"
            params["soyadi"] = soyadi

        if kimlik_no:
            query += " AND KIMLIK_NO = :kimlik_no"
            params["kimlik_no"] = kimlik_no  # Note: Changed from "KIMLIK_NO" to match the parameter name

        # Paginasyon
        offset = (page - 1) * limit
        query += " OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY"
        params["offset"] = offset
        params["limit"] = limit

        # Logla sorguyu ve parametreleri
        logging.debug(f"Sorgu: {query}")
        logging.debug(f"Parametreler: {params}")

        # Sorguyu çalıştır - pass the raw string directly
        result = await execute_raw_sql(query, params)

        # Sonuç boşsa hata fırlat
        if not result:
            logging.warning("Kişi listesi boş.")
            raise HTTPException(status_code=404, detail="Kişi listesi bulunamadı.")

        # Kisi modeline dönüştürme
        kisiler = [Kisi(**item) for item in result]
        logging.debug(f"Model Dönüştürme Başarılı: {len(kisiler)} kişi bulundu.")
        return kisiler

    except ValueError as e:
        logging.error(f"Veri dönüşüm hatası: {e}")
        raise HTTPException(status_code=500, detail=f"Veri dönüşüm hatası: {str(e)}")

    except Exception as e:
        logging.error(f"Beklenmeyen hata: {e}")
        raise HTTPException(status_code=500, detail=f"Beklenmeyen hata: {str(e)}")

# async def kisi_listesi() -> List[Kisi]:
#     """
#     Veritabanından kişi listesini çeker ve Kisi modeline dönüştürür.
#
#     Returns:
#         List[Kisi]: Kişi listesi (Kisi modeli formatında).
#
#     Raises:
#         HTTPException: Eğer kişi bulunamazsa veya dönüşüm hatası olursa.
#     """
#     query = "SELECT * FROM Kisi"
#     try:
#         # Sorguyu logla
#         logging.debug(f"Sorgu: {query}")
#
#         # execute_raw_sql fonksiyonunu çağır (text() ile sar)
#         result = await execute_raw_sql(text(query))  # Artık result bir dict listesi olmalı
#
#         # Sonuç boşsa hata fırlat
#         if not result:
#             logging.warning("Kişi listesi boş.")
#             raise HTTPException(status_code=404, detail="Kişi listesi bulunamadı.")
#
#         # Sorgu sonucunu logla
#         logging.debug(f"Sorgu Sonucu: {result}")
#
#         # Kisi modeline dönüştürme
#         kisiler = [Kisi(**item) for item in result]
#         logging.debug(f"Model Dönüştürme Başarılı: {len(kisiler)} kişi bulundu.")
#         return kisiler
#
#     except ValueError as e:
#         # Veri dönüşüm hatası durumunda hata fırlat
#         logging.error(f"Veri dönüşüm hatası: {e}")
#         raise HTTPException(status_code=500, detail=f"Veri dönüşüm hatası: {str(e)}")
#
#     except Exception as e:
#         # Diğer tüm hatalar için genel hata fırlat
#         logging.error(f"Beklenmeyen hata: {e}")
#         raise HTTPException(status_code=500, detail=f"Beklenmeyen hata: {str(e)}")
# @app.post("/kisi/")
# async def create_kisi(kisi: kisiCreate, db: Session = Depends(get_db)):
#     db_kisi = Kisi(**kisi.dict())
#     db.add(db_kisi)
#     db.commit()
#     db.refresh(db_kisi)
#     return db_kisi


# @app.put("/kisi/{kisi_id}")
# async def update_kisi(kisi_id: int, kisi: kisiCreate, db: Session = Depends(get_db)):
#     db_kisi = db.query(kisi).filter(kisi.KIMLIK_NO == kisi_id).first()
#     if db_kisi is None:
#         raise HTTPException(status_code=404, detail="kisi not found")
#
#     # Güncelleme
#     for key, value in Kisi.dict().items():
#         setattr(db_kisi, key, value)
#
#     db.commit()
#     db.refresh(db_kisi)
#     return db_kisi
#
# @app.get("/kisi/{kisi_id}")
# async def get_kisi(kisi_id: int, db: Session = Depends(get_db)):
#     query = "SELECT * FROM kisi WHERE KIMLIK_NO = :kisi_id"
#     result = await execute_raw_sql(query, {"kisi_id": kisi_id})
#     if not result:
#         raise HTTPException(status_code=404, detail="kisi not found")
#     return result[0]
#
# @app.put("/raw-kisi/{kisi_id}")
# async def update_raw_kisi(kisi_id: int, kisi: kisiCreate, db: Session = Depends(get_db)):
#     query = """
#     UPDATE kisi
#     SET ADI = :ADI, SOYADI = :SOYADI, EMAIL = :EMAIL
#     WHERE KIMLIK_NO = :kisi_id
#     """
#     params = Kisi.dict()
#     params["kisi_id"] = kisi_id
#     await execute_raw_sql(query, params)
#     return {"message": "kisi updated successfully"}