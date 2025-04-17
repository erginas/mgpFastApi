from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.scheduler$_job_arg import Scheduler$JobArg, Scheduler$JobArgCreate
from models.scheduler$_job_arg import Scheduler$JobArg as DBScheduler$JobArg
from crud.scheduler$_job_arg import get_all_scheduler$_job_arg, get_scheduler$_job_arg_by_id, create_scheduler$_job_arg

router = APIRouter(prefix='/scheduler$_job_arg', tags=['Scheduler$JobArg'])

@router.get('/', response_model=list[Scheduler$JobArg])
async def list_scheduler$_job_arg(db: AsyncSession = Depends()):
    return await get_all_scheduler$_job_arg(db)

@router.get('/{id}', response_model=Scheduler$JobArg)
async def get_scheduler$_job_arg_item(id: int, db: AsyncSession = Depends()):
    result = await get_scheduler$_job_arg_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Scheduler$JobArg)
async def create_scheduler$_job_arg_item(data: Scheduler$JobArgCreate, db: AsyncSession = Depends()):
    db_item = DBScheduler$JobArg(**data.dict())
    return await create_scheduler$_job_arg(db, db_item)