from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.iyilestirici_faaliyet import IyilestiriciFaaliyet

async def get_all_iyilestirici_faaliyet(db: AsyncSession):
    result = await db.execute(select(IyilestiriciFaaliyet))
    return result.scalars().all()

async def get_iyilestirici_faaliyet_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IyilestiriciFaaliyet).where(IyilestiriciFaaliyet.id == id))
    return result.scalar_one_or_none()

async def create_iyilestirici_faaliyet(db: AsyncSession, obj: IyilestiriciFaaliyet):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj