import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog, messagebox
from getpass import getpass
from crypto_utils import encrypt_password, decrypt_password, load_key

VAULT_PATH = "data/vault.json"

def load_data():
    if not os.path.exists(VAULT_PATH):
        return {}
    with open(VAULT_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(VAULT_PATH, "w") as f:
        json.dump(data, f, indent=4)

# --- Fungsi Versi GUI ---

def add_password_gui():
    key = load_key()
    site = simpledialog.askstring("Tambah", "Nama situs:")
    if not site:
        return
    username = simpledialog.askstring("Tambah", "Username:")
    if not username:
        return
    password = simpledialog.askstring("Tambah", "Password:")
    if not password:
        return

    encrypted_pw = encrypt_password(password, key)
    data = load_data()
    data[site] = {"username": username, "password": encrypted_pw}
    save_data(data)
    messagebox.showinfo("Berhasil", f"Password untuk {site} disimpan!")

def view_passwords_gui():
    key = load_key()
    data = load_data()
    if not data:
        messagebox.showinfo("Info", "Vault kosong.")
        return
    
    # Buat jendela baru
    window = tk.Toplevel()
    window.title("📋 Semua Password")
    window.geometry("500x300")

    # Tabel
    tree = ttk.Treeview(window, columns=("Site", "Username", "Password"), show="headings")
    tree.heading("Site", text="Situs")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")

    # Scrollbar
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both")

     # Isi data ke tabel
    for site, info in data.items():
        pw = decrypt_password(info["password"], key)
        tree.insert("", "end", values=(site, info["username"], pw))

    result = ""
    for site, info in data.items():
        pw = decrypt_password(info["password"], key)
        result += f"{site} | {info['username']} | {pw}\n"

    messagebox.showinfo("Semua Password", result)

def search_site_gui():
    key = load_key()
    site = simpledialog.askstring("Cari", "Nama situs:")
    data = load_data()
    if site in data:
        info = data[site]
        pw = decrypt_password(info["password"], key)
        messagebox.showinfo("Hasil", f"{site} | {info['username']} | {pw}")
    else:
        messagebox.showwarning("Tidak Ditemukan", "Situs tidak ditemukan.")
