from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tpc_c_properties import TpcCProperties, TpcCPropertiesCreate
from models.tpc_c_properties import TpcCProperties as DBTpcCProperties
from crud.tpc_c_properties import get_all_tpc_c_properties, get_tpc_c_properties_by_id, create_tpc_c_properties

router = APIRouter(prefix='/tpc_c_properties', tags=['TpcCProperties'])

@router.get('/', response_model=list[TpcCProperties])
async def list_tpc_c_properties(db: AsyncSession = Depends()):
    return await get_all_tpc_c_properties(db)

@router.get('/{id}', response_model=TpcCProperties)
async def get_tpc_c_properties_item(id: int, db: AsyncSession = Depends()):
    result = await get_tpc_c_properties_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TpcCProperties)
async def create_tpc_c_properties_item(data: TpcCPropertiesCreate, db: AsyncSession = Depends()):
    db_item = DBTpcCProperties(**data.dict())
    return await create_tpc_c_properties(db, db_item)