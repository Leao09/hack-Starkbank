from pydantic import BaseModel, Field

class WarehouseSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    Name: str = Field(default=None)
    Status: bool = Field(default=None)
    Amount: int = Field(default=None)

class UserSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    Name: str = Field(default=None)
    Last_Name: str = Field(default=None)
    Password : str = Field(default=None)
    Document: str = Field(default=None)

class HistoricSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    Id_P: int = Field(default=None, gt=0)
    Name: str = Field(default=None) 
    Name_P: str = Field(default=None)
    Amount: int = Field(default=None)
