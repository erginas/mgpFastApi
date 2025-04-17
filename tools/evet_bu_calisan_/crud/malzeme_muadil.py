from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_muadil import MalzemeMuadil

async def get_all_malzeme_muadil(db: AsyncSession):
    result = await db.execute(select(MalzemeMuadil))
    return result.scalars().all()

async def get_malzeme_muadil_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeMuadil).where(MalzemeMuadil.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_muadil(db: AsyncSession, obj: MalzemeMuadil):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj