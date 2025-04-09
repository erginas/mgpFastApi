
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from routers import router
from users.user_routers import user_router

app = FastAPI()
app = FastAPI(title="FastAPI + Oracle + Raw SQL")

origins = [
    "http://localhost:5173",  # React uygulamasının çalıştığı port
    "http://127.0.0.1:5173",  # Alternatif olarak bunu da ekleyebilirsin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # veya ["*"] geliştirirken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(user_router)