import uvicorn
from fastapi import FastAPI

from app.api import router
from app.core.config import Setting
from app.models.database import database

app = FastAPI(title="Event manager backend", version="0.1.0")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=Setting.DEFAULT_HOST,
        port=Setting.DEFAULT_PORT,
        reload=Setting.DEBUG,
    )
