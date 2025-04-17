from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.plan_donemi import PlanDonemi, PlanDonemiCreate
from models.plan_donemi import PlanDonemi as DBPlanDonemi
from crud.plan_donemi import get_all_plan_donemi, get_plan_donemi_by_id, create_plan_donemi

router = APIRouter(prefix='/plan_donemi', tags=['PlanDonemi'])

@router.get('/', response_model=list[PlanDonemi])
async def list_plan_donemi(db: AsyncSession = Depends()):
    return await get_all_plan_donemi(db)

@router.get('/{id}', response_model=PlanDonemi)
async def get_plan_donemi_item(id: int, db: AsyncSession = Depends()):
    result = await get_plan_donemi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=PlanDonemi)
async def create_plan_donemi_item(data: PlanDonemiCreate, db: AsyncSession = Depends()):
    db_item = DBPlanDonemi(**data.dict())
    return await create_plan_donemi(db, db_item)