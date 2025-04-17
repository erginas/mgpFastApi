from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.astip_tipsan_depo import AstipTipsanDepo

async def get_all_astip_tipsan_depo(db: AsyncSession):
    result = await db.execute(select(AstipTipsanDepo))
    return result.scalars().all()

async def get_astip_tipsan_depo_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AstipTipsanDepo).where(AstipTipsanDepo.id == id))
    return result.scalar_one_or_none()

async def create_astip_tipsan_depo(db: AsyncSession, obj: AstipTipsanDepo):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj