from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.resim_grubu import ResimGrubu

async def get_all_resim_grubu(db: AsyncSession):
    result = await db.execute(select(ResimGrubu))
    return result.scalars().all()

async def get_resim_grubu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ResimGrubu).where(ResimGrubu.id == id))
    return result.scalar_one_or_none()

async def create_resim_grubu(db: AsyncSession, obj: ResimGrubu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj