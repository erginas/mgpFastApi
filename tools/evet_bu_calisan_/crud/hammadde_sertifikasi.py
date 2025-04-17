from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.hammadde_sertifikasi import HammaddeSertifikasi

async def get_all_hammadde_sertifikasi(db: AsyncSession):
    result = await db.execute(select(HammaddeSertifikasi))
    return result.scalars().all()

async def get_hammadde_sertifikasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HammaddeSertifikasi).where(HammaddeSertifikasi.id == id))
    return result.scalar_one_or_none()

async def create_hammadde_sertifikasi(db: AsyncSession, obj: HammaddeSertifikasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj