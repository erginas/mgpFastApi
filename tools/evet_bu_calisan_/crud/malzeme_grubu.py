from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_grubu import MalzemeGrubu

async def get_all_malzeme_grubu(db: AsyncSession):
    result = await db.execute(select(MalzemeGrubu))
    return result.scalars().all()

async def get_malzeme_grubu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeGrubu).where(MalzemeGrubu.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_grubu(db: AsyncSession, obj: MalzemeGrubu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj