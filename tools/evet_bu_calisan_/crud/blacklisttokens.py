from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.blacklisttokens import Blacklisttokens

async def get_all_blacklisttokens(db: AsyncSession):
    result = await db.execute(select(Blacklisttokens))
    return result.scalars().all()

async def get_blacklisttokens_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Blacklisttokens).where(Blacklisttokens.id == id))
    return result.scalar_one_or_none()

async def create_blacklisttokens(db: AsyncSession, obj: Blacklisttokens):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj