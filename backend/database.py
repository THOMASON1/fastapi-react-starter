from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Zmień poniższy adres na swój własny
# Format: postgresql://użytkownik:hasło@host/nazwa_bazy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:su@localhost/SF_SGP"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Funkcja pomocnicza do pobierania sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
