from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.parti_alt_grubu import PartiAltGrubu

async def get_all_parti_alt_grubu(db: AsyncSession):
    result = await db.execute(select(PartiAltGrubu))
    return result.scalars().all()

async def get_parti_alt_grubu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(PartiAltGrubu).where(PartiAltGrubu.id == id))
    return result.scalar_one_or_none()

async def create_parti_alt_grubu(db: AsyncSession, obj: PartiAltGrubu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj