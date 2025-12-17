"""Script to add `status` column to `employees` table if missing.

Usage:
  python backend/scripts/add_employees_status.py

This uses the project's SQLAlchemy engine (from backend.database.mysql) and will:
 - check information_schema to see if the `status` column exists
 - if missing, run ALTER TABLE to add it with DEFAULT 'ACTIVE'

Run this from the project root (where `backend` package is importable).
"""
from sqlalchemy import text
from backend.database.mysql import engine


def column_exists(conn) -> bool:
    q = text(
        "SELECT COUNT(*) as cnt FROM information_schema.columns "
        "WHERE table_schema = DATABASE() AND table_name = 'employees' AND column_name = 'status'"
    )
    res = conn.execute(q).scalar()
    return bool(res)


def add_column(conn):
    alter = text("ALTER TABLE employees ADD COLUMN `status` VARCHAR(20) NOT NULL DEFAULT 'ACTIVE';")
    conn.execute(alter)


def main():
    print("Connecting to DB using project's engine...")
    with engine.connect() as conn:
        try:
            if column_exists(conn):
                print("Column 'status' already exists on employees table. No action taken.")
                return

            print("Column 'status' not found — adding column...")
            add_column(conn)
            print("Column 'status' added successfully.")
        except Exception as exc:
            print("Failed to add column:", exc)


if __name__ == "__main__":
    main()
