from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.islem_merkezi import IslemMerkezi

async def get_all_islem_merkezi(db: AsyncSession):
    result = await db.execute(select(IslemMerkezi))
    return result.scalars().all()

async def get_islem_merkezi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IslemMerkezi).where(IslemMerkezi.id == id))
    return result.scalar_one_or_none()

async def create_islem_merkezi(db: AsyncSession, obj: IslemMerkezi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj