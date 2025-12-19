from app.database.connection import engine
from app.database.connection import Base
from app.models import employee, user, task

Base.metadata.create_all(bind=engine)
print("Tables created successfully")
