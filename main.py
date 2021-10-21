import json

from fastapi import FastAPI
from src.count import penentuan_arah

app = FastAPI()


@app.get("/{koordinat_lokasi}")
async def main(koordinat_lokasi):
    return penentuan_arah(koordinat_lokasi)#json.dumps(penentuan_arah(koordinat_lokasi))
