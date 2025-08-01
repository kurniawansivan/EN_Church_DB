import hashlib
import sqlite3

DB_PATH = "data/jemaat.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_profile_exists():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM profile")
    result = cursor.fetchone()[0]
    conn.close()
    return result > 0

def save_profile(nama_gereja, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    hashed_pw = hash_password(password)
    cursor.execute("INSERT INTO profile (nama_gereja, password_hash) VALUES (?, ?)", (nama_gereja, hashed_pw))
    conn.commit()
    conn.close()

def verify_login(input_password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM profile LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    if result:
        return hash_password(input_password) == result[0]
    return False

def get_nama_gereja():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nama_gereja FROM profile LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else ""