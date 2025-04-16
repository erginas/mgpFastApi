import logging
from http.client import HTTPException
from typing import List, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, text
from sqlalchemy.orm import Session

from Modules.Is_Emri.is_emri_operasyonu.models import IsEmriOperasyonu
from Modules.Is_Emri.is_emri_operasyonu.schemas import IsEmriOperasyonuCreate, IsEmriOperasyonuOut, IsEmriOperasyonuBase
from core.dependencies import execute_raw_sql


#
# async def get_all_is_emri_operasyonlari(session: AsyncSession):
#     result = await session.execute(select(IsEmriOperasyonu))
#     return result.scalars().all()

# Servis Fonksiyonu
async def get_all_is_emri_operasyonlari(session: AsyncSession, limit: int = 100) -> List[IsEmriOperasyonuOut]:
    # `select` ile sorgu oluştur
    stmt = select(IsEmriOperasyonu).limit(limit)

    # Sorguyu çalıştır ve sonuçları al
    result = await session.execute(stmt)
    db_records = result.scalars().all()

    # SQLAlchemy modelini Pydantic modeline dönüştür
    return [IsEmriOperasyonuOut.model_validate(record) for record in db_records]

async def get_is_emri_operasyonlari_raw(isemri_no: int) -> List[IsEmriOperasyonuBase]:
    try:
        query = """
        SELECT 
            io.OPERASYON_NO, 
            CASE 
                WHEN io.durumu = 'S' THEN 'Sonlanmş' 
                WHEN io.durumu = 'D' THEN 'Durmuş' 
                WHEN io.durumu = 'I' THEN 'İşler' 
                ELSE 'Diğer' 
            END Durumu,
            o.ADI operasyon_adi,
            io.ISLEM_BASLANGIC, 
            io.ISLEM_BITIS, 
            io.miktar_giren,
            io.miktar_cikan, 
            k.adi || ' ' || k.soyadi AS adi_soyadi,
            ie.ACIKLAMA, 
            ie.CE_FL, 
            ie.DURUMU AS isemri_durum, 
            ie.EK_BILGI, 
            ie.ONCELIK, 
            ie.RECETE_ID, 
            ie.RECETE_NO, 
            ie.REF_BELGE_NO,
            m.stok_kodu, 
            m.opsn, 
            m.malzeme_adi
            FROM IS_EMRI_OPERASYONU io
            LEFT OUTER JOIN kisi k ON k.kimlik_no = io.KIMLIK_NO
            LEFT OUTER JOIN is_emri ie ON io.ISEMRI_NO = ie.ISEMRI_NO
            LEFT OUTER JOIN OPERASYON o ON o.OPERASYON_NO = io.OPERASYON_NO
            LEFT OUTER JOIN malzeme m ON m.MALZEME_NO = ie.MALZEME_NO
            WHERE io.isemri_no = 1=1
                """
        params = {"isemri_no": isemri_no}

        if isemri_no:
            query +=  " and isemri_no = :isemri_no"
            params["isemri_no"] = isemri_no

        # Logla sorguyu ve parametreleri
        logging.debug(f"Sorgu: {query}")
        logging.debug(f"Parametreler: {params}")

        result = await execute_raw_sql(text(query), params)

        if not result:
            logging.warning("iş emrine ait herhangi bri operasyon bulunamadı")
            return HTTPException(status=404, detail="Operasyon Bulunamadı")

        operasyonlar = [IsEmriOperasyonuBase(**item) for item in result]
        logging.debug(f"Operasyonlar: {len(operasyonlar)} operasyon var")
        return operasyonlar

    except ValueError as e:
        logging.error(f"Veri dönüşüm hatası: {e}")
        raise HTTPException(status_code=500, detail=f"Veri dönüşüm hatası: {str(e)}")

    except Exception as e:
        logging.error(f"Beklenmeyen hata: {e}")
        raise HTTPException(status_code=500, detail=f"Beklenmeyen hata: {str(e)}")


    return await execute_raw_sql(query, params, fetch_all=True)

async def get_is_emri_operasyonu(session: AsyncSession, islem_sirasi: int, operasyon_no: int):
    result = await session.execute(
        select(IsEmriOperasyonu).where(
            IsEmriOperasyonu.ISLEM_SIRASI == islem_sirasi,
            IsEmriOperasyonu.OPERASYON_NO == operasyon_no
        )
    )
    return result.scalar_one_or_none()

async def create_is_emri_operasyonu(session: AsyncSession, data: IsEmriOperasyonuCreate):
    obj = IsEmriOperasyonu(**data.dict())
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj

async def update_is_emri_operasyonu(session: AsyncSession, islem_sirasi: int, operasyon_no: int, data: IsEmriOperasyonuCreate):
    await session.execute(
        update(IsEmriOperasyonu)
        .where(
            IsEmriOperasyonu.ISLEM_SIRASI == islem_sirasi,
            IsEmriOperasyonu.OPERASYON_NO == operasyon_no
        )
        .values(**data.dict())
    )
    await session.commit()
    return await get_is_emri_operasyonu(session, islem_sirasi, operasyon_no)

async def delete_is_emri_operasyonu(session: AsyncSession, islem_sirasi: int, operasyon_no: int):
    await session.execute(
        delete(IsEmriOperasyonu).where(
            IsEmriOperasyonu.ISLEM_SIRASI == islem_sirasi,
            IsEmriOperasyonu.OPERASYON_NO == operasyon_no
        )
    )
    await session.commit()
    return {"message": "Silindi"}
