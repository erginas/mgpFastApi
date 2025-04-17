from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_tedarik_fiyati import MalzemeTedarikFiyati

async def get_all_malzeme_tedarik_fiyati(db: AsyncSession):
    result = await db.execute(select(MalzemeTedarikFiyati))
    return result.scalars().all()

async def get_malzeme_tedarik_fiyati_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeTedarikFiyati).where(MalzemeTedarikFiyati.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_tedarik_fiyati(db: AsyncSession, obj: MalzemeTedarikFiyati):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj