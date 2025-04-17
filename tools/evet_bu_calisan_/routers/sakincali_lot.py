from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sakincali_lot import SakincaliLot, SakincaliLotCreate
from models.sakincali_lot import SakincaliLot as DBSakincaliLot
from crud.sakincali_lot import get_all_sakincali_lot, get_sakincali_lot_by_id, create_sakincali_lot

router = APIRouter(prefix='/sakincali_lot', tags=['SakincaliLot'])

@router.get('/', response_model=list[SakincaliLot])
async def list_sakincali_lot(db: AsyncSession = Depends()):
    return await get_all_sakincali_lot(db)

@router.get('/{id}', response_model=SakincaliLot)
async def get_sakincali_lot_item(id: int, db: AsyncSession = Depends()):
    result = await get_sakincali_lot_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SakincaliLot)
async def create_sakincali_lot_item(data: SakincaliLotCreate, db: AsyncSession = Depends()):
    db_item = DBSakincaliLot(**data.dict())
    return await create_sakincali_lot(db, db_item)