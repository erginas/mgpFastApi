from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tedarikci_emri_detay import TedarikciEmriDetay

async def get_all_tedarikci_emri_detay(db: AsyncSession):
    result = await db.execute(select(TedarikciEmriDetay))
    return result.scalars().all()

async def get_tedarikci_emri_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TedarikciEmriDetay).where(TedarikciEmriDetay.id == id))
    return result.scalar_one_or_none()

async def create_tedarikci_emri_detay(db: AsyncSession, obj: TedarikciEmriDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj