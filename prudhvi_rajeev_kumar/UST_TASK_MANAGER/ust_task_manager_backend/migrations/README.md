Use Alembic for real migrations in production.

Quick start:
- pip install alembic
- alembic init migrations
- Configure `sqlalchemy.url` in alembic.ini to your MySQL URI
- Generate: alembic revision --autogenerate -m "init"
- Apply: alembic upgrade head
