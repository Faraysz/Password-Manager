import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
from crypto_utils import generate_key
from manager import add_password_gui, view_passwords_gui, search_site_gui
from tkinter import ttk

# Inisialisasi Key
if not os.path.exists("key.key"):
    generate_key()

# GUI Window
root = tk.Tk()
root.title("🔐 Password Manager")
root.geometry("400x300")
root.resizable(False, False)

# ===== SET DARK MODE DI SINI =====
def set_dark_mode():
    style = ttk.Style()
    style.theme_use("clam")

    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    btn_color = "#444"
    hover_color = "#555"

    root.configure(bg=bg_color)

    style.configure(".", background=bg_color, foreground=fg_color, fieldbackground=bg_color)
    style.configure("TButton", background=btn_color, foreground=fg_color, relief="flat")
    style.map("TButton",
              background=[("active", hover_color)],
              foreground=[("active", "#fff")])
    
    style.configure("TLabel", background=bg_color, foreground=fg_color)

set_dark_mode()
# ==================================

# Tombol dan UI lainnya di sini...

# Fungsi tombol
def tambah_password():
    add_password_gui()

def lihat_password():
    view_passwords_gui()

def cari_password():
    search_site_gui()

# GUI Layout
title_label = ttk.Label(root, text="🔐 Password Manager", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

btn_add = ttk.Button(root, text="➕ Tambah Password", width=30, command=tambah_password)
btn_add.pack(pady=5)

btn_view = ttk.Button(root, text="📋 Lihat Semua Password", width=30, command=lihat_password)
btn_view.pack(pady=5)

btn_search = ttk.Button(root, text="🔍 Cari Password", width=30, command=cari_password)
btn_search.pack(pady=5)

btn_exit = ttk.Button(root, text="🚪 Keluar", width=30, command=root.quit)
btn_exit.pack(pady=20)

root.mainloop()
