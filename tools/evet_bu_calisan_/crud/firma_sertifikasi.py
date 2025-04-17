from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.firma_sertifikasi import FirmaSertifikasi

async def get_all_firma_sertifikasi(db: AsyncSession):
    result = await db.execute(select(FirmaSertifikasi))
    return result.scalars().all()

async def get_firma_sertifikasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FirmaSertifikasi).where(FirmaSertifikasi.id == id))
    return result.scalar_one_or_none()

async def create_firma_sertifikasi(db: AsyncSession, obj: FirmaSertifikasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj