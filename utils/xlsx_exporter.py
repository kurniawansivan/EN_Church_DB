import sqlite3
from openpyxl import Workbook
from tkinter import filedialog

DB_PATH = "data/jemaat.db"

def export_to_excel():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jemaat ORDER BY id ASC")
    data = cursor.fetchall()
    conn.close()

    headers = [
        "ID", "Nama Lengkap", "Alamat", "No. HP", "Tanggal Lahir",
        "Jenis Kelamin", "Status", "Riwayat Pemuridan", "Baptis", "Pelayanan"
    ]

    wb = Workbook()
    ws = wb.active
    ws.append(headers)

    for row in data:
        ws.append(row)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx")],
        title="Simpan File Excel"
    )
    if file_path:
        wb.save(file_path)
