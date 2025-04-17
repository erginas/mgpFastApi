from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tezgah_grubu import TezgahGrubu

async def get_all_tezgah_grubu(db: AsyncSession):
    result = await db.execute(select(TezgahGrubu))
    return result.scalars().all()

async def get_tezgah_grubu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TezgahGrubu).where(TezgahGrubu.id == id))
    return result.scalar_one_or_none()

async def create_tezgah_grubu(db: AsyncSession, obj: TezgahGrubu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj