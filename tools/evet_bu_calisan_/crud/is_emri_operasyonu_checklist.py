from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_operasyonu_checklist import IsEmriOperasyonuChecklist

async def get_all_is_emri_operasyonu_checklist(db: AsyncSession):
    result = await db.execute(select(IsEmriOperasyonuChecklist))
    return result.scalars().all()

async def get_is_emri_operasyonu_checklist_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriOperasyonuChecklist).where(IsEmriOperasyonuChecklist.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_operasyonu_checklist(db: AsyncSession, obj: IsEmriOperasyonuChecklist):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj