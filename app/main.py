import uvicorn
from fastapi import FastAPI

from app.core.config import Setting

app = FastAPI(title="Event manager backend", version="0.1.0")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=Setting.DEFAULT_HOST,
        port=Setting.DEFAULT_PORT,
        reload=Setting.DEBUG,
    )
