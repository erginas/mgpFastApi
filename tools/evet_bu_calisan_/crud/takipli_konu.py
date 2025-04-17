from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.takipli_konu import TakipliKonu

async def get_all_takipli_konu(db: AsyncSession):
    result = await db.execute(select(TakipliKonu))
    return result.scalars().all()

async def get_takipli_konu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TakipliKonu).where(TakipliKonu.id == id))
    return result.scalar_one_or_none()

async def create_takipli_konu(db: AsyncSession, obj: TakipliKonu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj