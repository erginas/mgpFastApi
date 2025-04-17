from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_tedarik_fiyat_detay import MalzemeTedarikFiyatDetay

async def get_all_malzeme_tedarik_fiyat_detay(db: AsyncSession):
    result = await db.execute(select(MalzemeTedarikFiyatDetay))
    return result.scalars().all()

async def get_malzeme_tedarik_fiyat_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeTedarikFiyatDetay).where(MalzemeTedarikFiyatDetay.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_tedarik_fiyat_detay(db: AsyncSession, obj: MalzemeTedarikFiyatDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj