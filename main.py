
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from routers import router
from users.user_routers import user_router
from Modules.IK.employees.routers import router as employees_router  # Employee router'ını import edelim
from Modules.IK.leave.routers import router as leave_router  # Leave router'ını import edelim

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
app.include_router(employees_router, prefix="/employees", tags=["Employees"])  # Çalışanlar için router
app.include_router(leave_router, prefix="/leaves", tags=["Leaves"])  # İzinler için router