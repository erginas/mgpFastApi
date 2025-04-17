from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ozellik_secenegi import OzellikSecenegi, OzellikSecenegiCreate
from models.ozellik_secenegi import OzellikSecenegi as DBOzellikSecenegi
from crud.ozellik_secenegi import get_all_ozellik_secenegi, get_ozellik_secenegi_by_id, create_ozellik_secenegi

router = APIRouter(prefix='/ozellik_secenegi', tags=['OzellikSecenegi'])

@router.get('/', response_model=list[OzellikSecenegi])
async def list_ozellik_secenegi(db: AsyncSession = Depends()):
    return await get_all_ozellik_secenegi(db)

@router.get('/{id}', response_model=OzellikSecenegi)
async def get_ozellik_secenegi_item(id: int, db: AsyncSession = Depends()):
    result = await get_ozellik_secenegi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=OzellikSecenegi)
async def create_ozellik_secenegi_item(data: OzellikSecenegiCreate, db: AsyncSession = Depends()):
    db_item = DBOzellikSecenegi(**data.dict())
    return await create_ozellik_secenegi(db, db_item)