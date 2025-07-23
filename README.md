# 🔐 Password Manager GUI dengan Python & Tkinter

Aplikasi sederhana untuk menyimpan dan mengelola password secara lokal menggunakan Python. Dilengkapi tampilan GUI (Tkinter) yang bersih, fitur pencarian, dan mode gelap. Password disimpan secara terenkripsi agar tetap aman.

![Tampilan Aplikasi](demo.png) <!-- Ganti dengan screenshot buatanmu -->

---

## ✨ Fitur

- ➕ Tambah password baru (situs, username, password)
- 🔍 Cari password berdasarkan nama situs
- 📋 Lihat semua password dalam tampilan tabel
- 🌙 Mode gelap (dark mode)
- 🔒 Enkripsi menggunakan `cryptography (Fernet)`
- 💾 Penyimpanan lokal dalam file JSON

---

## ⚙️ Teknologi yang Digunakan

- Python 3
- Tkinter (untuk GUI)
- Cryptography (Fernet encryption)
- JSON (penyimpanan lokal)

---

## ⚠️ Catatan Keamanan

Aplikasi ini dibuat untuk **tujuan pembelajaran**.

Tidak disarankan digunakan untuk menyimpan data sensitif dalam skala nyata tanpa fitur keamanan tambahan seperti:
- Otentikasi master password
- Penyimpanan terenkripsi di luar (bukan hanya file JSON lokal)
- Sistem proteksi tambahan lainnya
