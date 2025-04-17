from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tedarikci_emri_fv import TedarikciEmriFv, TedarikciEmriFvCreate
from models.tedarikci_emri_fv import TedarikciEmriFv as DBTedarikciEmriFv
from crud.tedarikci_emri_fv import get_all_tedarikci_emri_fv, get_tedarikci_emri_fv_by_id, create_tedarikci_emri_fv

router = APIRouter(prefix='/tedarikci_emri_fv', tags=['TedarikciEmriFv'])

@router.get('/', response_model=list[TedarikciEmriFv])
async def list_tedarikci_emri_fv(db: AsyncSession = Depends()):
    return await get_all_tedarikci_emri_fv(db)

@router.get('/{id}', response_model=TedarikciEmriFv)
async def get_tedarikci_emri_fv_item(id: int, db: AsyncSession = Depends()):
    result = await get_tedarikci_emri_fv_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TedarikciEmriFv)
async def create_tedarikci_emri_fv_item(data: TedarikciEmriFvCreate, db: AsyncSession = Depends()):
    db_item = DBTedarikciEmriFv(**data.dict())
    return await create_tedarikci_emri_fv(db, db_item)