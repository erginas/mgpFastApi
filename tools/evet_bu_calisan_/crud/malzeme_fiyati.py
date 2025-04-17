from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_fiyati import MalzemeFiyati

async def get_all_malzeme_fiyati(db: AsyncSession):
    result = await db.execute(select(MalzemeFiyati))
    return result.scalars().all()

async def get_malzeme_fiyati_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeFiyati).where(MalzemeFiyati.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_fiyati(db: AsyncSession, obj: MalzemeFiyati):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj