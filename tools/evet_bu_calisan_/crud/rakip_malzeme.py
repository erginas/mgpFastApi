from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.rakip_malzeme import RakipMalzeme

async def get_all_rakip_malzeme(db: AsyncSession):
    result = await db.execute(select(RakipMalzeme))
    return result.scalars().all()

async def get_rakip_malzeme_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(RakipMalzeme).where(RakipMalzeme.id == id))
    return result.scalar_one_or_none()

async def create_rakip_malzeme(db: AsyncSession, obj: RakipMalzeme):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj