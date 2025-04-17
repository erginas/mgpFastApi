from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tedarikci_emri_fv import TedarikciEmriFv

async def get_all_tedarikci_emri_fv(db: AsyncSession):
    result = await db.execute(select(TedarikciEmriFv))
    return result.scalars().all()

async def get_tedarikci_emri_fv_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TedarikciEmriFv).where(TedarikciEmriFv.id == id))
    return result.scalar_one_or_none()

async def create_tedarikci_emri_fv(db: AsyncSession, obj: TedarikciEmriFv):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj