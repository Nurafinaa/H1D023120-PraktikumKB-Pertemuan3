import random
import datetime

def tampilkan_film():
    film = {
        "A001": "Avengers: Endgame",
        "A002": "Spider-Man: No Way Home",
        "A003": "The Batman",
        "A004": "Interstellar"
    }
    print("Daftar Film:")
    for kode, nama in film.items():
        print(f"{kode}: {nama}")
    return film

def pilih_kursi():
    kursi_tersedia = [f"{chr(row)}{col}" for row in range(65, 69) for col in range(1, 6)]  # A1-E5
    return random.choice(kursi_tersedia)

def pesan_tiket():
    film = tampilkan_film()
    kode_pilihan = input("Masukkan kode film yang dipilih: ").strip().upper()
    
    if kode_pilihan not in film:
        print("Kode film tidak valid!")
        return
    
    nama_film = film[kode_pilihan]
    kursi = pilih_kursi()
    waktu_pemesanan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n=== Tiket Berhasil Dipesan! ===")
    print(f"Film       : {nama_film}")
    print(f"Kursi      : {kursi}")
    print(f"Waktu Pesan: {waktu_pemesanan}")
    print("==============================")

if __name__ == "__main__":
    pesan_tiket()
