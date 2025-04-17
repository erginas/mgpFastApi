from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aktar_iade import AktarIade

async def get_all_aktar_iade(db: AsyncSession):
    result = await db.execute(select(AktarIade))
    return result.scalars().all()

async def get_aktar_iade_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AktarIade).where(AktarIade.id == id))
    return result.scalar_one_or_none()

async def create_aktar_iade(db: AsyncSession, obj: AktarIade):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj