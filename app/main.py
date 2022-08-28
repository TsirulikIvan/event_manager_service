from fastapi import FastAPI
from app.core.config import Setting
import uvicorn


app = FastAPI(title="Event manager backend", version="0.1.0")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=Setting.DEFAULT_HOST,
        port=Setting.DEFAULT_PORT,
        reload=Setting.DEBUG
    )