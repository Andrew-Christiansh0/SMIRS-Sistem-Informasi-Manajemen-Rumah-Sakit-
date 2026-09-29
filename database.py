from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL Koneksi Database PostgreSQL (Sesuaikan username, password, dan nama DB kamu)
# Format: postgresql://username:password@localhost:5432/nama_database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/simrs_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency untuk mengambil session database di FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()