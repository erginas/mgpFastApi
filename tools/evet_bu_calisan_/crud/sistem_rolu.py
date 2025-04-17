from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sistem_rolu import SistemRolu

async def get_all_sistem_rolu(db: AsyncSession):
    result = await db.execute(select(SistemRolu))
    return result.scalars().all()

async def get_sistem_rolu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SistemRolu).where(SistemRolu.id == id))
    return result.scalar_one_or_none()

async def create_sistem_rolu(db: AsyncSession, obj: SistemRolu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj