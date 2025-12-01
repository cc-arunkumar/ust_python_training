from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:vinnu_4545@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Create tables
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")


def create_user(name: str, email: str):
    session = SessionLocal()
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        print("Exception:", e)
        return None
    finally:
        session.close()


def get_user_by_id(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    except Exception as e:
        print("Exception:", e)
        return None
    finally:
        session.close()


def update_user(user_id: int, new_email: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print("User not found!")
            return None
        user.email = new_email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


def delete_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print("User not found!")
            return None
        session.delete(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


if __name__ == "__main__":
    # Create a new user
    new_user = create_user('Bujji1', 'bujji1@ust.com')
    if new_user:
        print(f"New user created ====> Name: {new_user.name}, Email: {new_user.email}")

    # Get all users
    users = get_all_users()
    if users:
        print("All Users:")
        for u in users:
            print(f" ====> Name: {u.name}, Email: {u.email}")

    # Get a user by ID
    user = get_user_by_id(1)
    if user:
        print(f"User by ID ====> Name: {user.name}, Email: {user.email}")

    # Update a user's email
    updated_user = update_user(1, "updated_email@ust.com")
    if updated_user:
        print(f"Updated User ====> Name: {updated_user.name}, Email: {updated_user.email}")

    # Delete a user
    deleted_user = delete_user(1)
    if deleted_user:
        print(f"Deleted User ====> Name: {deleted_user.name}, Email: {deleted_user.email}")

#SAMPLE OUTPUT

# Creating tables in MySQL DB...
# 2025-12-01 22:10:31,913 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2025-12-01 22:10:31,913 INFO sqlalchemy.engine.Engine [raw sql] {}     
# 2025-12-01 22:10:31,914 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2025-12-01 22:10:31,914 INFO sqlalchemy.engine.Engine [raw sql] {}     
# 2025-12-01 22:10:31,915 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2025-12-01 22:10:31,915 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:10:31,916 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,917 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`users`
# 2025-12-01 22:10:31,917 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:10:31,920 INFO sqlalchemy.engine.Engine COMMIT
# Table creation completed
# 2025-12-01 22:10:31,922 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,925 INFO sqlalchemy.engine.Engine INSERT INTO users (name, email) VALUES (%(name)s, %(email)s)
# 2025-12-01 22:10:31,925 INFO sqlalchemy.engine.Engine [generated in 0.00039s] {'name': 'Bujji1', 'email': 'bujji1@ust.com'}
# 2025-12-01 22:10:31,926 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:10:31,932 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,935 INFO sqlalchemy.engine.Engine SELECT users.id, users.name, users.email
# FROM users
# WHERE users.id = %(pk_1)s
# 2025-12-01 22:10:31,935 INFO sqlalchemy.engine.Engine [generated in 0.00040s] {'pk_1': 4}
# 2025-12-01 22:10:31,936 INFO sqlalchemy.engine.Engine ROLLBACK
# New user created ====> Name: Bujji1, Email: bujji1@ust.com
# 2025-12-01 22:10:31,938 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,941 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# 2025-12-01 22:10:31,943 INFO sqlalchemy.engine.Engine [generated in 0.00149s] {}
# 2025-12-01 22:10:31,944 INFO sqlalchemy.engine.Engine ROLLBACK
# All Users:
#  ====> Name: Bujji1, Email: bujji1@ust.com
# 2025-12-01 22:10:31,950 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,951 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# WHERE users.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:10:31,951 INFO sqlalchemy.engine.Engine [generated in 0.00057s] {'id_1': 1, 'param_1': 1}
# 2025-12-01 22:10:31,952 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-01 22:10:31,953 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,953 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# WHERE users.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:10:31,953 INFO sqlalchemy.engine.Engine [cached since 0.002733s ago] {'id_1': 1, 'param_1': 1}     
# User not found!
# 2025-12-01 22:10:31,954 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-01 22:10:31,955 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:10:31,955 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# WHERE users.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:10:31,955 INFO sqlalchemy.engine.Engine [cached since 0.004837s ago] {'id_1': 1, 'param_1': 1}     
# User not found!
# 2025-12-01 22:10:31,956 INFO sqlalchemy.engine.Engine ROLLBACK