import tkinter as tk
from tkinter import messagebox
from core.auth import save_profile

def show_registration_form(root, on_success):
    def submit():
        nama = entry_nama.get().strip()
        pw = entry_pw.get().strip()

        if not nama or not pw:
            messagebox.showwarning("Peringatan", "Nama dan password tidak boleh kosong.")
            return

        save_profile(nama, pw)
        messagebox.showinfo("Berhasil", "Registrasi gereja berhasil disimpan.")
        form.destroy()
        on_success()

    form = tk.Toplevel(root)
    form.title("Registrasi Gereja")
    form.geometry("300x180")
    form.resizable(False, False)

    tk.Label(form, text="Nama Gereja").pack(pady=(10, 0))
    entry_nama = tk.Entry(form, width=30)
    entry_nama.pack(pady=5)

    tk.Label(form, text="Password").pack(pady=(10, 0))
    entry_pw = tk.Entry(form, width=30, show="*")
    entry_pw.pack(pady=5)

    tk.Button(form, text="Simpan", command=submit).pack(pady=15)
