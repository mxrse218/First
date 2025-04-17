def cek_kelulusan(nilaiTeori, nilaiPraktek):
    return nilaiTeori >= 70 and nilaiPraktek >= 60

nilaiTeori = int(input("Masukkan nilai teori: "))
nilaiPraktek = int(input("Masukkan nilai praktek: "))

print(cek_kelulusan(nilaiTeori, nilaiPraktek))
