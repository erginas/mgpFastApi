from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sevk_edilen_siparis import SevkEdilenSiparis, SevkEdilenSiparisCreate
from models.sevk_edilen_siparis import SevkEdilenSiparis as DBSevkEdilenSiparis
from crud.sevk_edilen_siparis import get_all_sevk_edilen_siparis, get_sevk_edilen_siparis_by_id, create_sevk_edilen_siparis

router = APIRouter(prefix='/sevk_edilen_siparis', tags=['SevkEdilenSiparis'])

@router.get('/', response_model=list[SevkEdilenSiparis])
async def list_sevk_edilen_siparis(db: AsyncSession = Depends()):
    return await get_all_sevk_edilen_siparis(db)

@router.get('/{id}', response_model=SevkEdilenSiparis)
async def get_sevk_edilen_siparis_item(id: int, db: AsyncSession = Depends()):
    result = await get_sevk_edilen_siparis_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SevkEdilenSiparis)
async def create_sevk_edilen_siparis_item(data: SevkEdilenSiparisCreate, db: AsyncSession = Depends()):
    db_item = DBSevkEdilenSiparis(**data.dict())
    return await create_sevk_edilen_siparis(db, db_item)