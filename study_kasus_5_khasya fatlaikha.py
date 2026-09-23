def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan.lower() == "mobil":
        tarif = 5000
    elif jenis_kendaraan.lower() == "motor":
        tarif = 3000
    else:
        return 0

    total_biaya = tarif * lama_parkir
    return total_biaya

# input data
jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

# menghitung lama parkir
lama_parkir =  jam_keluar - jam_masuk
# memanggil function
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

if total_biaya is not None:
    print(f"jenis kendaraan: {jenis_kendaraan}")
    print(f"jam masuk: {jam_masuk}:00")
    print(f"jam keluar: {jam_keluar}:00")
    print(f"lama parkir: {lama_parkir} jam")
    print(f"total biaya: Rp{total_biaya}")
else:
    print("jenis kedaraan tidak dikenali.")