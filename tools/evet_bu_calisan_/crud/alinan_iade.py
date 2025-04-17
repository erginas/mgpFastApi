from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_iade import AlinanIade

async def get_all_alinan_iade(db: AsyncSession):
    result = await db.execute(select(AlinanIade))
    return result.scalars().all()

async def get_alinan_iade_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanIade).where(AlinanIade.id == id))
    return result.scalar_one_or_none()

async def create_alinan_iade(db: AsyncSession, obj: AlinanIade):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj