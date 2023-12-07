from fastapi import APIRouter, Body
from model import WarehouseSchema
from db import database, Warehouse

app = APIRouter()


@app.get("/warehouse")
async def read_Warehouse():
    if not database.is_connected:
        await database.connect()

    return await Warehouse.objects.all()


@app.post("/warehouse")
async def create_Warehouse(ware: WarehouseSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()

    await Warehouse.objects.create(Name=ware.Name,
                                  Status=ware.Status,
                                  Amout=ware.Amout)
    return {"success": "Successfully created"}


@app.put("/warehouse")
async def update_Warehouse(new_Ware: WarehouseSchema):
    if not database.is_connected:
        await database.connect()
    return await Warehouse.objects.update_or_create(id=new_Ware.id,
                                               Name=new_Ware.Name,
                                               Status=new_Ware.Status,
                                               Amout=new_Ware.Amout)


@app.delete("/warehouse/{Id}")
async def delete_Warehouse(Id: int):
    if not database.is_connected:
        await database.connect()
    return await Warehouse.objects.delete(id=Id)