from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aa_uts import AaUts

async def get_all_aa_uts(db: AsyncSession):
    result = await db.execute(select(AaUts))
    return result.scalars().all()

async def get_aa_uts_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AaUts).where(AaUts.id == id))
    return result.scalar_one_or_none()

async def create_aa_uts(db: AsyncSession, obj: AaUts):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj