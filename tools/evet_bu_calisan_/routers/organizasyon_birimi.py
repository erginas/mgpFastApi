from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.organizasyon_birimi import OrganizasyonBirimi, OrganizasyonBirimiCreate
from models.organizasyon_birimi import OrganizasyonBirimi as DBOrganizasyonBirimi
from crud.organizasyon_birimi import get_all_organizasyon_birimi, get_organizasyon_birimi_by_id, create_organizasyon_birimi

router = APIRouter(prefix='/organizasyon_birimi', tags=['OrganizasyonBirimi'])

@router.get('/', response_model=list[OrganizasyonBirimi])
async def list_organizasyon_birimi(db: AsyncSession = Depends()):
    return await get_all_organizasyon_birimi(db)

@router.get('/{id}', response_model=OrganizasyonBirimi)
async def get_organizasyon_birimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_organizasyon_birimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=OrganizasyonBirimi)
async def create_organizasyon_birimi_item(data: OrganizasyonBirimiCreate, db: AsyncSession = Depends()):
    db_item = DBOrganizasyonBirimi(**data.dict())
    return await create_organizasyon_birimi(db, db_item)