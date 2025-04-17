from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri import IsEmri

async def get_all_is_emri(db: AsyncSession):
    result = await db.execute(select(IsEmri))
    return result.scalars().all()

async def get_is_emri_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmri).where(IsEmri.id == id))
    return result.scalar_one_or_none()

async def create_is_emri(db: AsyncSession, obj: IsEmri):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj