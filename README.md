# SIMRS - System Informasi Manajemen Rumah Sakit

Projek web app SIMRS sederhana untuk pendaftaran dan manajemen data rekam medis pasien. Dibuat dengan stack Python FastAPI dan SQLite untuk backend, serta HTML/JavaScript dengan Tailwind CSS untuk tampilan antarmuka (frontend).

## Tech Stack

- **Backend**: Python 3, FastAPI, Uvicorn
- **Database**: SQLite
- **Frontend**: HTML5, JavaScript (Fetch API), Tailwind CSS (via CDN)

## Fitur

- Input data pasien baru (Nomor RM, Nama, Tanggal Lahir, Jenis Kelamin, Alamat).
- Menampilkan list pasien terdaftar secara real-time dari database.
- Menghapus record pasien dari SQLite.
- Integrasi CORS agar frontend dapat mengonsumsi endpoint FastAPI secara langsung.
- Dokumentasi API otomatis via Swagger UI (`/docs`).

## Struktur File

```text
├── main.py            # Script FastAPI, definisi endpoint & koneksi SQLite
├── simrs.db           # File database SQLite
├── index.html         # Tampilan dashboard (Frontend)
├── requirements.txt   # Daftar dependensi Python
└── Procfile           # Konfigurasi deployment untuk server cloud
