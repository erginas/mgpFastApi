
from fastapi import FastAPI, Depends

from routers import router

app = FastAPI()


app = FastAPI(title="FastAPI + Oracle + Raw SQL")
app.include_router(router)