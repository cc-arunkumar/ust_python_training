from database import engine
from database import Base  # Adjust the import path based on where your Base is defined

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
