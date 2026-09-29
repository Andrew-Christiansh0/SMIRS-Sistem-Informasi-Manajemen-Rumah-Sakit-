from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI(
    title="SIMRS API Portal",
    description="Sistem Informasi Manajemen Rumah Sakit dengan SQLite",
    version="1.0.0"
)

# Izinkan Front-End mengakses Back-End (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect("simrs.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pasien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomor_rm TEXT UNIQUE NOT NULL,
            nama TEXT NOT NULL,
            tanggal_lahir TEXT NOT NULL,
            jenis_kelamin TEXT NOT NULL,
            alamat TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class PasienCreate(BaseModel):
    nomor_rm: str
    nama: str
    tanggal_lahir: str
    jenis_kelamin: str
    alamat: str

@app.get("/")
def home():
    return {"status": "Aktif", "message": "API SIMRS terhubung ke SQLite!"}

@app.post("/api/pasien")
def tambah_pasien(pasien: PasienCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO pasien (nomor_rm, nama, tanggal_lahir, jenis_kelamin, alamat)
            VALUES (?, ?, ?, ?, ?)
            """,
            (pasien.nomor_rm, pasien.nama, pasien.tanggal_lahir, pasien.jenis_kelamin, pasien.alamat)
        )
        conn.commit()
        pasien_id = cursor.lastrowid
        conn.close()
        return {
            "status": "Sukses",
            "message": f"Pasien {pasien.nama} berhasil tersimpan!",
            "id": pasien_id
        }
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Nomor RM sudah terdaftar!")
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/pasien")
def get_semua_pasien():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pasien")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]