from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum, auto
import random
app = FastAPI()

class Material(Enum):
    BRONCE = auto()
    PLATA = auto()
    ORO = auto()

class Caballero(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelation: str

caballeros = [
    Caballero(id=1, name="miguel", material=Material.BRONCE, attack=35, constelation="caballo"),
    Caballero(id=2, name="andres", material=Material.PLATA, attack=3, constelation="mono"),
    Caballero(id=3, name="rodolfo", material=Material.ORO, attack=5, constelation="perro"),
    Caballero(id=4, name="juan", material=Material.BRONCE, attack=29, constelation="gato"),
    Caballero(id=5, name="julian", material=Material.PLATA, attack=55, constelation="elefante"),
    Caballero(id=6, name="sebas", material=Material.ORO, attack=78, constelation="zorro"),
    Caballero(id=7, name="jorge", material=Material.BRONCE, attack=67, constelation="gato"),
    Caballero(id=8, name="carlos", material=Material.PLATA, attack=32, constelation="animals"),
    Caballero(id=9, name="nicolas", material=Material.ORO, attack=65, constelation="sura"),
    Caballero(id=10, name="polo", material=Material.BRONCE, attack=23, constelation="epsesremalo"),
]

@app.get("/showCaballero")
def showCaballero():
    return caballeros

@app.get("/fightCaballero")
def fightCaballero():

    caballero1 = random.choice(caballeros)
    caballero2 = random.choice(caballeros)

    while caballero1.id == caballero2.id:
        caballero2 = random.choice(caballeros)

    if caballero1.attack > caballero2.attack:
        ganador = caballero1
    elif caballero2.attack > caballero1.attack:
        ganador = caballero2
    else:
        ganador = "empate"

    return {
        "caballero1": caballero1,
        "caballero2": caballero2,
        "ganador": ganador
    }


#@app.get("/showConstelation")


#@app.get("/showYourCaballero")

