from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tedarikci_emri_detay import TedarikciEmriDetay, TedarikciEmriDetayCreate
from models.tedarikci_emri_detay import TedarikciEmriDetay as DBTedarikciEmriDetay
from crud.tedarikci_emri_detay import get_all_tedarikci_emri_detay, get_tedarikci_emri_detay_by_id, create_tedarikci_emri_detay

router = APIRouter(prefix='/tedarikci_emri_detay', tags=['TedarikciEmriDetay'])

@router.get('/', response_model=list[TedarikciEmriDetay])
async def list_tedarikci_emri_detay(db: AsyncSession = Depends()):
    return await get_all_tedarikci_emri_detay(db)

@router.get('/{id}', response_model=TedarikciEmriDetay)
async def get_tedarikci_emri_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_tedarikci_emri_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TedarikciEmriDetay)
async def create_tedarikci_emri_detay_item(data: TedarikciEmriDetayCreate, db: AsyncSession = Depends()):
    db_item = DBTedarikciEmriDetay(**data.dict())
    return await create_tedarikci_emri_detay(db, db_item)