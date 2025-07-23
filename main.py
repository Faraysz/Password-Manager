import os
from crypto_utils import generate_key
from manager import add_password, view_passwords, search_site

def main():
    if not os.path.exists("key.key"):
        print("[+] Key belum ditemukan. Membuat key baru...")
        generate_key()

    while True:
        print("\n🔐 PASSWORD MANAGER")
        print("1. Tambah Password")
        print("2. Lihat Semua Password")
        print("3. Cari Password")
        print("4. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_site()
        elif choice == "4":
            print("Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
