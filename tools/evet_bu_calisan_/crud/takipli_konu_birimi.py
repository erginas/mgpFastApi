from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.takipli_konu_birimi import TakipliKonuBirimi

async def get_all_takipli_konu_birimi(db: AsyncSession):
    result = await db.execute(select(TakipliKonuBirimi))
    return result.scalars().all()

async def get_takipli_konu_birimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TakipliKonuBirimi).where(TakipliKonuBirimi.id == id))
    return result.scalar_one_or_none()

async def create_takipli_konu_birimi(db: AsyncSession, obj: TakipliKonuBirimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj