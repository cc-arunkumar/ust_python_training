from app.database.db import SessionLocal   # Add "app."

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
