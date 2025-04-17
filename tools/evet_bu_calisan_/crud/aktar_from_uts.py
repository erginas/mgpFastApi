from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aktar_from_uts import AktarFromUts

async def get_all_aktar_from_uts(db: AsyncSession):
    result = await db.execute(select(AktarFromUts))
    return result.scalars().all()

async def get_aktar_from_uts_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AktarFromUts).where(AktarFromUts.id == id))
    return result.scalar_one_or_none()

async def create_aktar_from_uts(db: AsyncSession, obj: AktarFromUts):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj