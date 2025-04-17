from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.takipli_konu_asamasi import TakipliKonuAsamasi

async def get_all_takipli_konu_asamasi(db: AsyncSession):
    result = await db.execute(select(TakipliKonuAsamasi))
    return result.scalars().all()

async def get_takipli_konu_asamasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TakipliKonuAsamasi).where(TakipliKonuAsamasi.id == id))
    return result.scalar_one_or_none()

async def create_takipli_konu_asamasi(db: AsyncSession, obj: TakipliKonuAsamasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj