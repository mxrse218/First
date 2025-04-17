def hitung_umur(tahun_lahir):
    tahun_sekarang = 2025
    umur = tahun_sekarang - tahun_lahir
    return umur


tahun_lahir = int(input("tahun lahir: "))
print(f"Umur Anda: {hitung_umur(tahun_lahir)} tahun")
