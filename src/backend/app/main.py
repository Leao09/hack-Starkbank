from fastapi import FastAPI
from db import database

from app.routes.user import app as user_router

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
