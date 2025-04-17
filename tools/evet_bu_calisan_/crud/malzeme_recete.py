from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_recete import MalzemeRecete

async def get_all_malzeme_recete(db: AsyncSession):
    result = await db.execute(select(MalzemeRecete))
    return result.scalars().all()

async def get_malzeme_recete_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeRecete).where(MalzemeRecete.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_recete(db: AsyncSession, obj: MalzemeRecete):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj