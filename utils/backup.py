import shutil
import os
from tkinter import filedialog

DB_PATH = "data/jemaat.db"
AUTO_BACKUP_PATH = "data/backup_auto.db"

def backup_manual():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".db",
        filetypes=[("SQLite Database", "*.db")],
        title="Simpan Backup Manual"
    )
    if filepath:
        shutil.copyfile(DB_PATH, filepath)

def backup_otomatis():
    try:
        shutil.copyfile(DB_PATH, AUTO_BACKUP_PATH)
    except Exception as e:
        print(f"Gagal auto backup: {e}")

def import_database():
    filepath = filedialog.askopenfilename(
        title="Pilih File Database Cadangan",
        filetypes=[("SQLite Database", "*.db")]
    )
    if filepath:
        shutil.copyfile(filepath, DB_PATH)
