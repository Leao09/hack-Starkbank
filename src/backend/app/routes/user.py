from fastapi import APIRouter, Body
from model import UserSchema
from db import database, User

app = APIRouter()


@app.get("/users")
async def read_users():
    if not database.is_connected:
        await database.connect()

    return await User.objects.all()


@app.post("/users")
async def create_User(user: UserSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()

    await User.objects.create(Name=user.Name,
                              Last_Name=user.Last_Name,
                              Password=user.Password,
                              Document=user.Document)
    return {"success": "Successfully created"}


@app.put("/users")
async def update_User(new_User: UserSchema):
    if not database.is_connected:
        await database.connect()
    return await User.objects.update_or_create(Id=new_User.id,
                                               Name=new_User.Name,
                                               Last_Name=new_User.Last_Name,
                                               Password=new_User.Password,
                                               Document=new_User.Document)


@app.delete("/users/{Id}")
async def delete_User(Id: int):
    if not database.is_connected:
        await database.connect()
    return await User.objects.delete(Id=Id)
