from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router
from users.user_routers import user_router
from Modules.IK.employees.routers import router as employees_router
from Modules.IK.leave.routers import router as leave_router
from Modules.kisi.routers import router as kisi_router
from core.routers import router as huffma_router # xrouter yerine router

app = FastAPI(title="FastAPI + Oracle + Raw SQL")

# CORS ayarları
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router'ları ekleme
app.include_router(router)
app.include_router(user_router)
app.include_router(employees_router, prefix="/employees", tags=["Employees"])
app.include_router(leave_router, prefix="/leaves", tags=["Leaves"])
app.include_router(kisi_router, prefix="/ik", tags=["Kisi"])
app.include_router(huffma_router, prefix="/hf", tags=["Huffman"])