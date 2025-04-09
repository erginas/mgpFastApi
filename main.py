
from fastapi import FastAPI, Depends

from routers import router
from users.user_routers import user_router

app = FastAPI()


app = FastAPI(title="FastAPI + Oracle + Raw SQL")
app.include_router(router)
app.include_router(user_router)