import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from api.handlers import controller_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="controller-api")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_api_router = APIRouter()

main_api_router.include_router(
    controller_router, prefix="/controller", tags=["controller"]
)

app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
