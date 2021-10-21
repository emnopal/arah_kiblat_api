import numpy as np
import time
import requests


def konversi_koordinat_lokasi(koordinat_lokasi):
    if "," in koordinat_lokasi:
        koordinat_lokasi_raw = koordinat_lokasi
        koordinat_lokasi = koordinat_lokasi.split(",").replace("'","")

    if isinstance(koordinat_lokasi, list):
        if len(koordinat_lokasi) != 2:
            raise ValueError("Format Koordinat (Garis dan Bujur) salah!")
        else:
            lintang_lokasi, bujur_lokasi = list(map(float, koordinat_lokasi))
            return [koordinat_lokasi_raw], [np.deg2rad(np.abs(lintang_lokasi))], [np.deg2rad(np.abs(bujur_lokasi))]

    if isinstance(koordinat_lokasi, str):
        lokasi_ = koordinat_lokasi.replace(" ", "+")
        api = f"http://nominatim.openstreetmap.org/search?q={lokasi_}&format=json&polygon=1&addressdetails=1"
        lokasi, lintang, bujur = [], [], []
        r = requests.get(api)
        time.sleep(2)  # biar gak dianggap bot
        data = r.json()
        for parse in data:
            lokasi.append(parse['display_name'])
            lintang.append(parse['lat'])
            bujur.append(parse['lon'])
        lintang = list(map(np.rad2deg, map(np.abs, map(float, lintang))))
        bujur = list(map(np.rad2deg, map(np.abs, map(float, bujur))))
        return lokasi, lintang, bujur


def konversi_koordinat_kabah(koordinat_kabah=[21.422510, 39.826172]):
    return np.deg2rad(koordinat_kabah[0]), np.deg2rad(koordinat_kabah[1])
