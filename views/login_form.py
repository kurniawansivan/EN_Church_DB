import tkinter as tk
from tkinter import messagebox
from core.auth import verify_login, get_nama_gereja

def show_login_form(root, on_success):
    def submit():
        pw = entry_pw.get().strip()
        if not pw:
            messagebox.showwarning("Peringatan", "Password tidak boleh kosong.")
            return

        if verify_login(pw):
            form.destroy()
            on_success()
        else:
            messagebox.showerror("Gagal", "Password salah!")

    form = tk.Toplevel(root)
    form.title("Login Gereja")
    form.geometry("300x180")
    form.resizable(False, False)

    nama_gereja = get_nama_gereja()

    tk.Label(form, text=f"Hi, {nama_gereja}", font=("Helvetica", 12, "bold")).pack(pady=(10, 5))
    tk.Label(form, text="Masukkan Password").pack()
    entry_pw = tk.Entry(form, width=30, show="*")
    entry_pw.pack(pady=10)

    tk.Button(form, text="Login", command=submit).pack(pady=10)
