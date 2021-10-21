import sys
import numpy as np

from utils.utils import konversi_koordinat_kabah, konversi_koordinat_lokasi
sys.path.append('..')


def penentuan_arah(koordinat_lokasi, koordinat_kabah=""):
    kibla_final = {}
    if koordinat_kabah == "":
        lintang_kabah, bujur_kabah = konversi_koordinat_kabah()
    else:
        lintang_kabah, bujur_kabah = konversi_koordinat_kabah(koordinat_kabah)

    lok, lintang, bujur = konversi_koordinat_lokasi(koordinat_lokasi)
    data = zip(lok, lintang, bujur)
    print()
    for lokasi, lintang_lokasi, bujur_lokasi in data:
        blt_bk_rel = bujur_lokasi - bujur_kabah
        kibla = np.arctan((np.tan(lintang_kabah) * np.cos(lintang_lokasi)) /
                          (np.sin(blt_bk_rel)) + (np.sin(lintang_lokasi)) / (np.tan(blt_bk_rel)))
        kibla_final[lokasi] = np.rad2deg(kibla) + 270
        print(
            f"Sudut Relatif di Daerah {lokasi}:\n{np.rad2deg(kibla) + 270}°\n")
    return kibla_final
