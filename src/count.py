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
        lintang_lokasi_ = np.deg2rad(-lintang_lokasi)
        bujur_lokasi_ = np.deg2rad(bujur_lokasi)
        blt_bk_rel = np.abs(bujur_lokasi_ - bujur_kabah)
        kibla = np.arctan((np.tan(lintang_kabah) * np.cos(lintang_lokasi_)) /
                          (np.sin(blt_bk_rel)) + (np.sin(lintang_lokasi_)) / (np.tan(blt_bk_rel)))
        kibla_final[lokasi] = [np.rad2deg(kibla) + 270, lintang_lokasi, bujur_lokasi]
        print(
            f"Sudut Relatif di Daerah {lokasi} dengan koordinat: {lintang_lokasi}, {bujur_lokasi}:\n{np.rad2deg(kibla) + 270}°\n")
    return kibla_final
