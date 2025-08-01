import sqlite3

DB_PATH = "data/jemaat.db"

def get_all_jemaat():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jemaat ORDER BY id ASC")
    result = cursor.fetchall()
    conn.close()
    return result

def add_jemaat(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO jemaat (nama_lengkap, alamat, no_hp, tanggal_lahir, jenis_kelamin,
                            status, riwayat_pemuridan, baptis, pelayanan)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def update_jemaat(jemaat_id, data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE jemaat SET
            nama_lengkap=?, alamat=?, no_hp=?, tanggal_lahir=?, jenis_kelamin=?,
            status=?, riwayat_pemuridan=?, baptis=?, pelayanan=?
        WHERE id=?
    ''', (*data, jemaat_id))
    conn.commit()
    conn.close()

def delete_jemaat(jemaat_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jemaat WHERE id=?", (jemaat_id,))
    conn.commit()
    conn.close()
