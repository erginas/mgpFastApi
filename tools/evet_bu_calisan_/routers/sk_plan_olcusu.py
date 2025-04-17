from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sk_plan_olcusu import SkPlanOlcusu, SkPlanOlcusuCreate
from models.sk_plan_olcusu import SkPlanOlcusu as DBSkPlanOlcusu
from crud.sk_plan_olcusu import get_all_sk_plan_olcusu, get_sk_plan_olcusu_by_id, create_sk_plan_olcusu

router = APIRouter(prefix='/sk_plan_olcusu', tags=['SkPlanOlcusu'])

@router.get('/', response_model=list[SkPlanOlcusu])
async def list_sk_plan_olcusu(db: AsyncSession = Depends()):
    return await get_all_sk_plan_olcusu(db)

@router.get('/{id}', response_model=SkPlanOlcusu)
async def get_sk_plan_olcusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_sk_plan_olcusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SkPlanOlcusu)
async def create_sk_plan_olcusu_item(data: SkPlanOlcusuCreate, db: AsyncSession = Depends()):
    db_item = DBSkPlanOlcusu(**data.dict())
    return await create_sk_plan_olcusu(db, db_item)