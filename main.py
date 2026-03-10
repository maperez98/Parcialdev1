from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum,auto


app= FastAPI()

class caballero(BaseModel):
    id: int
    name :str
    attack : int
    constelation : str 

class material(enum):
    bronce = auto()
    plata = auto()
    oro = auto()




