from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

class regcliente(BaseModel):
    nombre: str
    email : str    

app = FastAPI()


@app.get("/", response_model=Respuesta)
async def index():
    return{"message":"Hello World"}
@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect('code/sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response

@app.get("/clientes/{id_cliente}")
async def clientes(id_cliente):
    with sqlite3.connect('code/sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id_cliente={}".format(int(id_cliente)))
        response=cursor.fetchall()
        return response

@app.post("/clientes/", response_model=Respuesta)
def post_cliente(cliente: regcliente):
    with sqlite3.connect('code/sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor=connection.cursor()
        cursor.execute("INSERT INTO clientes(nombre,email) VALUES(?,?)", (cliente.nombre,cliente.email))
        cursor.fetchall()
        response = {"message":"Insertaste un cliente correctamente :)"}
        return response


@app.put("/clientes/", response_model=Respuesta)
async def clientes_update(nombre: str="", email:str="", id_cliente:int=0):
    with sqlite3.connect("code/sql/clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("UPDATE clientes SET nombre =?, email= ? WHERE id_cliente =?;",(nombre, email, id_cliente))
        connection.commit()
        response = {"message":"Actualizaste un cliente correctamente :)"}
        return response


@app.delete("/clientes/{id}")
async def clientes_delete(id):
    with sqlite3.connect('code/sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor=connection.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente ={}".format(int(id)))
        cursor.fetchall()
        response = {"message":"Eliminaste un cliente correctamente :("}
        return response               





