from fastapi import APIRouter, Depends, Body
from app.model import UserSchema
from app.db import database, User

app = APIRouter()

@app.get("/users")
async def read_users():
    if not database.is_connected:
        await database.connect()
        
    return await User.objects.all()