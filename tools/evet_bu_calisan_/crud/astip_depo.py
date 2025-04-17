from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.astip_depo import AstipDepo

async def get_all_astip_depo(db: AsyncSession):
    result = await db.execute(select(AstipDepo))
    return result.scalars().all()

async def get_astip_depo_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AstipDepo).where(AstipDepo.id == id))
    return result.scalar_one_or_none()

async def create_astip_depo(db: AsyncSession, obj: AstipDepo):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj