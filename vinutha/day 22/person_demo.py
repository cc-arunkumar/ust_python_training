from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database Connection
DATABASE_URL = "mysql+pymysql://root:vinnu_4545@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base declaration
Base = declarative_base()

# Person Model
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Person(id={self.id}, name='{self.name}', email='{self.email}')"


# Create table
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed.")


# Create a new person
def create_person(name: str, email: str):
    session = SessionLocal()
    try:
        new_person = Person(name=name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        return new_person   # MUST RETURN THE OBJECT
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Get all persons
def get_all_users():
    session = SessionLocal()
    try:
        return session.query(Person).all()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Get person by ID
def get_person_by_id(person_id: int):
    session = SessionLocal()
    try:
        return session.query(Person).filter(Person.id == person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Update person email
def update_person(person_id: int, new_email: str):
    session = SessionLocal()
    try:
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("Person not found")
            return None

        person.email = new_email
        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Main Execution
if __name__ == "__main__":
    # 1. Create new person
    new_person = create_person("Bujji1", "bujji1@ust.com")
    if new_person:
        print(f"New person created ====> Name: {new_person.name}, Email: {new_person.email}")
    else:
        print("Failed to create person")

    # 2. Get all users
    persons = get_all_users()
    print("All Persons:")
    if persons:
        for p in persons:
            print(f" ====> Name: {p.name}, Email: {p.email}")

    # 3. Get person by ID
    person = get_person_by_id(2)
    print("Fetched Person:", person)

    # 4. Update email
    updated_person = update_person(2, "updated_email@ust.com")
    if updated_person:
        print(f"Updated Person ====> Name: {updated_person.name}, Email: {updated_person.email}")



#SAMPLE OUTPUT:
# Creating tables in MySQL DB...
# 2025-12-01 22:05:20,140 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2025-12-01 22:05:20,140 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:05:20,141 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2025-12-01 22:05:20,141 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:05:20,142 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2025-12-01 22:05:20,142 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:05:20,142 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:05:20,143 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`persons`
# 2025-12-01 22:05:20,143 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:05:20,146 INFO sqlalchemy.engine.Engine COMMIT
# Table creation completed.
# 2025-12-01 22:05:20,148 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:05:20,150 INFO sqlalchemy.engine.Engine INSERT INTO persons (name, email) VALUES (%(name)s, %(email)s)
# 2025-12-01 22:05:20,151 INFO sqlalchemy.engine.Engine [generated in 0.00057s] {'name': 'Bujji1', 'email': 'bujji1@ust.com'}
# 2025-12-01 22:05:20,152 INFO sqlalchemy.engine.Engine ROLLBACK
# Exception: (pymysql.err.IntegrityError) (1062, "Duplicate entry 'bujji1@ust.com' for key 'persons.email'")       
# [SQL: INSERT INTO persons (name, email) VALUES (%(name)s, %(email)s)]
# [parameters: {'name': 'Bujji1', 'email': 'bujji1@ust.com'}]
# (Background on this error at: https://sqlalche.me/e/20/gkpj)
# Failed to create person
# 2025-12-01 22:05:20,164 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:05:20,168 INFO sqlalchemy.engine.Engine SELECT persons.id AS persons_id, persons.name AS persons_name, persons.email AS persons_email
# FROM persons
# 2025-12-01 22:05:20,169 INFO sqlalchemy.engine.Engine [generated in 0.00037s] {}
# 2025-12-01 22:05:20,170 INFO sqlalchemy.engine.Engine ROLLBACK
# All Persons:
#  ====> Name: Vinnu, Email: vkolla@gitam.in
#  ====> Name: Vinnu1, Email: vinn@gmail.com
#  ====> Name: Chinnu, Email: chinnu@ust.com
#  ====> Name: Chinnu1, Email: chinnu1@ust.com
#  ====> Name: Bujji, Email: bujji@ust.com
#  ====> Name: Bujji1, Email: bujji1@ust.com
# 2025-12-01 22:05:20,172 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:05:20,173 INFO sqlalchemy.engine.Engine SELECT persons.id AS persons_id, persons.name AS persons_name, persons.email AS persons_email
# FROM persons
# WHERE persons.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:05:20,173 INFO sqlalchemy.engine.Engine [generated in 0.00038s] {'id_1': 2, 'param_1': 1}
# 2025-12-01 22:05:20,174 INFO sqlalchemy.engine.Engine ROLLBACK
# Fetched Person: None
# 2025-12-01 22:05:20,175 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:05:20,175 INFO sqlalchemy.engine.Engine SELECT persons.id AS persons_id, persons.name AS persons_name, persons.email AS persons_email
# FROM persons
# WHERE persons.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:05:20,176 INFO sqlalchemy.engine.Engine [cached since 0.002877s ago] {'id_1': 2, 'param_1': 1}     
# Person not found
# 2025-12-01 22:05:20,177 INFO sqlalchemy.engine.Engine ROLLBACK