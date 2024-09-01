from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.csvProcessor import database
from routes.csvProcessor import app as csv_router
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

app.include_router(robot_router)
app.include_router(tts_router)
app.include_router(csv_router)


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