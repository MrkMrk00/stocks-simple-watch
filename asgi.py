from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from lib.database import connection_pool 
from api import transactions


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await connection_pool.open()
    yield
    await connection_pool.close()

app = FastAPI(lifespan=app_lifespan)
api = APIRouter(prefix='/api')

api.include_router(transactions.r)

app.include_router(api)
app.mount('/', StaticFiles(directory='static'), name='static')

