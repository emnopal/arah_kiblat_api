import json

from fastapi import FastAPI
from src.count import penentuan_arah
from typing import Union

app = FastAPI()

@app.get("/")
async def koordinat_get(
    latlong: str = None,
    latitude: Union[float, str] = None,
    longitude: Union[float, str] = None,
    wilayah: str = None,
):
    if latlong:
        return penentuan_arah(latlong)
    if wilayah:
        return penentuan_arah(wilayah)
    else:
        koordinat_lokasi = str(latitude) + "," + str(longitude)
        return penentuan_arah(koordinat_lokasi)
