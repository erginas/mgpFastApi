from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.deleted_sakincali_lot import DeletedSakincaliLot, DeletedSakincaliLotCreate
from models.deleted_sakincali_lot import DeletedSakincaliLot as DBDeletedSakincaliLot
from crud.deleted_sakincali_lot import get_all_deleted_sakincali_lot, get_deleted_sakincali_lot_by_id, create_deleted_sakincali_lot

router = APIRouter(prefix='/deleted_sakincali_lot', tags=['DeletedSakincaliLot'])

@router.get('/', response_model=list[DeletedSakincaliLot])
async def list_deleted_sakincali_lot(db: AsyncSession = Depends()):
    return await get_all_deleted_sakincali_lot(db)

@router.get('/{id}', response_model=DeletedSakincaliLot)
async def get_deleted_sakincali_lot_item(id: int, db: AsyncSession = Depends()):
    result = await get_deleted_sakincali_lot_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DeletedSakincaliLot)
async def create_deleted_sakincali_lot_item(data: DeletedSakincaliLotCreate, db: AsyncSession = Depends()):
    db_item = DBDeletedSakincaliLot(**data.dict())
    return await create_deleted_sakincali_lot(db, db_item)