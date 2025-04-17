from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tedarikci_emri import TedarikciEmri, TedarikciEmriCreate
from models.tedarikci_emri import TedarikciEmri as DBTedarikciEmri
from crud.tedarikci_emri import get_all_tedarikci_emri, get_tedarikci_emri_by_id, create_tedarikci_emri

router = APIRouter(prefix='/tedarikci_emri', tags=['TedarikciEmri'])

@router.get('/', response_model=list[TedarikciEmri])
async def list_tedarikci_emri(db: AsyncSession = Depends()):
    return await get_all_tedarikci_emri(db)

@router.get('/{id}', response_model=TedarikciEmri)
async def get_tedarikci_emri_item(id: int, db: AsyncSession = Depends()):
    result = await get_tedarikci_emri_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TedarikciEmri)
async def create_tedarikci_emri_item(data: TedarikciEmriCreate, db: AsyncSession = Depends()):
    db_item = DBTedarikciEmri(**data.dict())
    return await create_tedarikci_emri(db, db_item)