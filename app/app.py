from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Dairy Diary API", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Dairy Diary API is running"}
