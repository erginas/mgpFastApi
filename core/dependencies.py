import logging
from contextlib import asynccontextmanager
from typing import List, Dict, Tuple
from requests import session
from core.database import SessionFactory, execute_raw_sql, get_raw_connection
from typing import List, Dict, Any

from sqlalchemy import text


# Log ayarları
logging.basicConfig(level=logging.DEBUG)

async def get_db():
    async with SessionFactory() as session:
        yield session


from contextlib import asynccontextmanager
import logging


@asynccontextmanager
async def get_raw_connection():
    """
    Oracle bağlantısı oluşturur ve context manager ile yönetir.
    """
    connection = None  # connection değişkenini başlangıçta tanımla
    try:
        # Asenkron session oluştur
        connection = SessionFactory()  # SessionFactory bir asenkron session factory
        logging.debug("Bağlantı oluşturuldu.")

        # Bağlantıyı yield ile sağla
        yield connection
    except Exception as e:
        # Hata durumunda logla ve hata fırlat
        logging.error(f"Bağlantı hatası: {e}")
        raise e
    finally:
        # Bağlantıyı kapat (eğer tanımlıysa)
        if connection:
            try:
                await connection.close()
                logging.debug("Bağlantı kapatıldı.")
            except Exception as close_error:
                logging.error(f"Bağlantı kapatma hatası: {close_error}")

# async def execute_raw_sql(query, params: dict = None) -> list[dict]:
#     """
#     Raw SQL sorgusunu çalıştırır ve sonucu sözlük listesi olarak döndürür.
#     """
#     try:
#         # async with ile bağlantıyı al
#         async with get_raw_connection() as session:
#             # Eğer query bir string ise, text() ile sar
#             if isinstance(query, str):
#                 query = text(query)
#             # Sorguyu çalıştır
#             result = await session.execute(query, params or {})
#
#             # Sütun isimlerini al ve BÜYÜK HARFE çevir
#             columns = [col.upper() for col in result.keys()]
#             if not columns:
#                 raise ValueError("Sorgu sonucunda sütun bulunamadı.")
#
#             ## Satırları al
#              #rows = result.fetchall()
#
#             ##Logla sorgu sonuçlarını
#             # logging.debug(f"Sütunlar: {columns}")
#             # logging.debug(f"Satırlar: {rows}")
#
#             # Satırları sözlük listesine dönüştür (sütun isimlerini büyük harfle eşleştir)
#             return [dict(zip(columns, row)) for row in rows]
#     except ValueError as ve:
#         logging.error(f"Değer Hatası: {ve}")
#         raise ve
#     except Exception as e:
#         logging.error(f"Beklenmeyen Hata: {e}")
#         raise e

from sqlalchemy import text


async def execute_raw_sql(query, params: dict = None) -> list[dict]:
    """
    Raw SQL sorgusunu çalıştırır ve sonucu sözlük listesi olarak döndürür.

    Args:
        query (str or TextClause): Çalıştırılacak SQL sorgusu.
        params (dict, optional): Sorgu parametreleri. Varsayılan None.

    Returns:
        list[dict]: Sorgu sonucu (sözlük listesi).

    Raises:
        ValueError: Eğer sorgu sonucunda sütun bulunamazsa.
        Exception: Diğer tüm hatalar için.
    """
    try:
        # async with ile bağlantıyı al
        async with get_raw_connection() as session:
            # Eğer query bir string ise, text() ile sar
            if isinstance(query, str):
                query = text(query)

            # Sorguyu çalıştır
            result = await session.execute(query, params or {})

            # Sütun isimlerini al ve BÜYÜK HARFE çevir
            columns = [col.upper() for col in result.keys()]
            if not columns:
                raise ValueError("Sorgu sonucunda sütun bulunamadı.")

            # Satırları al
            rows = result.fetchall()

            # Logla sorgu sonuçlarını
            logging.debug(f"Sütunlar: {columns}")
            logging.debug(f"Satırlar: {rows}")

            # Satırları sözlük listesine dönüştür
            return [dict(zip(columns, row)) for row in rows]
    except ValueError as ve:
        logging.error(f"Değer Hatası: {ve}")
        raise ve
    except Exception as e:
        logging.error(f"Beklenmeyen Hata: {e}")
        raise e