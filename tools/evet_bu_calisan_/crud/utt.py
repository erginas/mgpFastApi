from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.utt import Utt

async def get_all_utt(db: AsyncSession):
    result = await db.execute(select(Utt))
    return result.scalars().all()

async def get_utt_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Utt).where(Utt.id == id))
    return result.scalar_one_or_none()

async def create_utt(db: AsyncSession, obj: Utt):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj