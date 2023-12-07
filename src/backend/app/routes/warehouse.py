from fastapi import APIRouter, Body
from model import WarehouseSchema
from db import database, Warehouse

app = APIRouter()


@app.get("/warehouse")
async def read_Warehouse():
    if not database.is_connected:
        await database.connect()

    return await Historic.objects.all()


@app.post("/warehouse")
async def create_Warehouse(hist: HistoricSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()

    await Historic.objects.create(Id_P=hist.Id_P,
                                  Name=hist.Name,
                                  Name_P=hist.Name_P,
                                  amount=hist.amount)
    return {"success": "Successfully created"}


@app.put("/warehouse")
async def update_Warehouse(new_Hist: HistoricSchema):
    if not database.is_connected:
        await database.connect()
    return await Historic.objects.update_or_create(id=new_Hist.id,
                                               Id_P=new_Hist.Id_P,
                                               Name=new_Hist.Name,
                                               Name_P=new_Hist.Name_P,
                                               amount=new_Hist.amount)


@app.delete("/historic/{Id}")
async def delete_Warehouse(Id: int):
    if not database.is_connected:
        await database.connect()
    return await Historic.objects.delete(id=Id)