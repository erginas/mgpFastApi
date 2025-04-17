from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.dosya_malzeme import DosyaMalzeme

async def get_all_dosya_malzeme(db: AsyncSession):
    result = await db.execute(select(DosyaMalzeme))
    return result.scalars().all()

async def get_dosya_malzeme_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DosyaMalzeme).where(DosyaMalzeme.id == id))
    return result.scalar_one_or_none()

async def create_dosya_malzeme(db: AsyncSession, obj: DosyaMalzeme):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj