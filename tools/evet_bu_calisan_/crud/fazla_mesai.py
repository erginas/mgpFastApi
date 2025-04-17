from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.fazla_mesai import FazlaMesai

async def get_all_fazla_mesai(db: AsyncSession):
    result = await db.execute(select(FazlaMesai))
    return result.scalars().all()

async def get_fazla_mesai_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FazlaMesai).where(FazlaMesai.id == id))
    return result.scalar_one_or_none()

async def create_fazla_mesai(db: AsyncSession, obj: FazlaMesai):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj