from fastapi import APIRouter, Body
from model import HistoricSchema
from db import database, Historic

app = APIRouter()


@app.get("/historic")
async def read_Historic():
    if not database.is_connected:
        await database.connect()

    return await Historic.objects.all()


@app.post("/historic")
async def create_Historic(hist: HistoricSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()

    await Historic.objects.create(Id_P=hist.Id_P,
                                  Name=hist.Name,
                                  Name_P=hist.Name_P,
                                  amount=hist.amount)
    return {"success": "Successfully created"}


@app.put("/historic")
async def update_Historic(new_Hist: HistoricSchema):
    if not database.is_connected:
        await database.connect()
    return await Historic.objects.update_or_create(id=new_Hist.id,
                                               Id_P=new_Hist.Id_P,
                                               Name=new_Hist.Name,
                                               Name_P=new_Hist.Name_P,
                                               amount=new_Hist.amount)


@app.delete("/historic/{Id}")
async def delete_Historic(Id: int):
    if not database.is_connected:
        await database.connect()
    return await Historic.objects.delete(id=Id)