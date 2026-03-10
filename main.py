from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum, auto

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
    Caballero(id=2, name="andres", material=Material.PLATA, attack=35, constelation="caballo"),
    Caballero(id=3, name="rodolfo", material=Material.ORO, attack=35, constelation="caballo"),
    Caballero(id=4, name="juan", material=Material.BRONCE, attack=35, constelation="caballo"),
    Caballero(id=5, name="julian", material=Material.PLATA, attack=35, constelation="caballo"),
    Caballero(id=6, name="sebas", material=Material.ORO, attack=35, constelation="caballo"),
    Caballero(id=7, name="jorge", material=Material.BRONCE, attack=35, constelation="caballo"),
    Caballero(id=8, name="carlos", material=Material.PLATA, attack=35, constelation="caballo"),
    Caballero(id=9, name="nicolas", material=Material.ORO, attack=35, constelation="caballo"),
    Caballero(id=10, name="polo", material=Material.BRONCE, attack=35, constelation="caballo"),
]

