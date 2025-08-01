# core/init.py
import sqlite3
import os

DB_PATH = "data/jemaat.db"

def initialize_database():
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabel untuk menyimpan profil gereja dan password
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_gereja TEXT,
            password_hash TEXT
        )
    ''')

    # Tabel untuk menyimpan data jemaat
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jemaat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_lengkap TEXT,
            alamat TEXT,
            no_hp TEXT,
            tanggal_lahir TEXT,
            jenis_kelamin TEXT,
            status TEXT,
            riwayat_pemuridan TEXT,
            baptis TEXT,
            pelayanan TEXT
        )
    ''')

    conn.commit()
    conn.close()
