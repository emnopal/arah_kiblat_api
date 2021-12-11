import json

from fastapi import FastAPI
from src.count import penentuan_arah
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union, Tuple

app = FastAPI()

class Koordinat(BaseModel):
    latitude: Union[float, str] = None
    longitude: Union[float, str] = None
    latlong: str = None
    wilayah: str = None

@app.get("/{koordinat_lokasi}")
async def koordinat_get(koordinat_lokasi: str):
    return penentuan_arah(koordinat_lokasi)

@app.post("/")
async def koordinat_post(koordinat: Koordinat):
    if koordinat.latlong:
        return penentuan_arah(koordinat.latlong)
    if koordinat.wilayah:
        return penentuan_arah(koordinat.wilayah)
    else:
        koordinat_lokasi = str(koordinat.latitude) + "," + str(koordinat.longitude)
        print(koordinat_lokasi)
        return penentuan_arah(koordinat_lokasi)
