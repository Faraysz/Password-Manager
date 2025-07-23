import json
import os
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

def add_password():
    key = load_key()
    site = input("Nama situs: ")
    username = input("Username: ")
    password = getpass("Password: ")
    encrypted_pw = encrypt_password(password, key)

    data = load_data()
    data[site] = {"username": username, "password": encrypted_pw}
    save_data(data)
    print("[✔] Password berhasil disimpan!")

def view_passwords():
    key = load_key()
    data = load_data()

    if not data:
        print("Vault kosong.")
        return

    for site, info in data.items():
        decrypted_pw = decrypt_password(info["password"], key)
        print(f"🧩 {site} | {info['username']} | {decrypted_pw}")

def search_site():
    key = load_key()
    site = input("Cari situs: ")
    data = load_data()

    if site in data:
        info = data[site]
        password = decrypt_password(info["password"], key)
        print(f"🔍 {site} | {info['username']} | {password}")
    else:
        print("❌ Situs tidak ditemukan.")
