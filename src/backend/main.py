from fastapi import FastAPI, Request, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import database

from routes.user import app as user_router
from routes.historic import app as historic_router
from routes.warehouse import app as warehouse_router
from routes.robot import app as robot_router
from routes.tts import app as tts_router

import uvicorn


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
app.include_router(historic_router)
app.include_router(warehouse_router)
app.include_router(robot_router)
app.include_router(tts_router)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)