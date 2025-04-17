from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_relations import MalzemeRelations

async def get_all_malzeme_relations(db: AsyncSession):
    result = await db.execute(select(MalzemeRelations))
    return result.scalars().all()

async def get_malzeme_relations_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeRelations).where(MalzemeRelations.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_relations(db: AsyncSession, obj: MalzemeRelations):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj