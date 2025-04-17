from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tedarikci_degerlendirmesi import TedarikciDegerlendirmesi, TedarikciDegerlendirmesiCreate
from models.tedarikci_degerlendirmesi import TedarikciDegerlendirmesi as DBTedarikciDegerlendirmesi
from crud.tedarikci_degerlendirmesi import get_all_tedarikci_degerlendirmesi, get_tedarikci_degerlendirmesi_by_id, create_tedarikci_degerlendirmesi

router = APIRouter(prefix='/tedarikci_degerlendirmesi', tags=['TedarikciDegerlendirmesi'])

@router.get('/', response_model=list[TedarikciDegerlendirmesi])
async def list_tedarikci_degerlendirmesi(db: AsyncSession = Depends()):
    return await get_all_tedarikci_degerlendirmesi(db)

@router.get('/{id}', response_model=TedarikciDegerlendirmesi)
async def get_tedarikci_degerlendirmesi_item(id: int, db: AsyncSession = Depends()):
    result = await get_tedarikci_degerlendirmesi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TedarikciDegerlendirmesi)
async def create_tedarikci_degerlendirmesi_item(data: TedarikciDegerlendirmesiCreate, db: AsyncSession = Depends()):
    db_item = DBTedarikciDegerlendirmesi(**data.dict())
    return await create_tedarikci_degerlendirmesi(db, db_item)