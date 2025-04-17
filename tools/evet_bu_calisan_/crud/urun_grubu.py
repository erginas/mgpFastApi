from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.urun_grubu import UrunGrubu

async def get_all_urun_grubu(db: AsyncSession):
    result = await db.execute(select(UrunGrubu))
    return result.scalars().all()

async def get_urun_grubu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UrunGrubu).where(UrunGrubu.id == id))
    return result.scalar_one_or_none()

async def create_urun_grubu(db: AsyncSession, obj: UrunGrubu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj