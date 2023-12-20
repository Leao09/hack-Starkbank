import databases
import ormar
import sqlalchemy
from datetime import date
from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"
    Id: int = ormar.Integer(primary_key=True)
    Name: str = ormar.String(max_length=128,nullable=False)
    Last_Name: str = ormar.String(max_length=128,nullable=False)
    Password: str = ormar.String(max_length=128,nullable=False)
    Document: str = ormar.String(max_length=128,nullable=False)


class Historic(ormar.Model):
    class Meta(BaseMeta):
        tablename = "historic"
        
    id: int = ormar.Integer(primary_key=True)
    Id_P: int = ormar.Integer(foreing_key=True,nullable=False)
    Name: str = ormar.String(max_length=128,nullable=False)
    Name_P: str = ormar.String(max_length=128,nullable=False)
    amount: int = ormar.Integer(nullable=False)
    data: date = ormar.Date(nullable=False)


class Warehouse(ormar.Model):
    class Meta(BaseMeta):
        tablename = "warehouse"
        
    id: int = ormar.Integer(primary_key=True)
    Name: str = ormar.String(max_length=128,nullable=False)
    Status: bool = ormar.Boolean(nullable=False)
    Amout: int = ormar.Integer(nullable=False)

class Robot(ormar.Model):
    class Meta(BaseMeta):
        tablename = "robot"
        
    id: int = ormar.Integer(primary_key=True)
    X: str = ormar.String(max_length=128,nullable=False)
    Y: str = ormar.String(max_length=128,nullable=False)
    

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)