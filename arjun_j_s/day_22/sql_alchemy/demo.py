from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base


D_B = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(D_B,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base= declarative_base()

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)

    def __repr__(self):
        return f"User(id = {self.id}, name = {self.name}, email = {self.email})"
    
print("Creating Table in Mysql")
Base.metadata.create_all(bind=engine)
print("Completed Creating")


def create_user(name:str,email:str):
    try:
        session = SessionLocal()
        new_person = Person(name=name,email=email)

        session.add(new_person)

        session.commit()

        session.refresh(new_person)

        return new_person.__dict__
    
    except Exception as e:
        session.rollback()
        print(str(e))
    
    finally:
        session.close()

# print(create_user("Arjun","ajs@ust.com"))
# print(create_user("Arjun","ajs1@ust.com"))
# print(create_user("Arjun","ajs2@ust.com"))
# print(create_user("Arjun","ajs3@ust.com"))

def get_all_users():
    try:
        session = SessionLocal()
        persons = session.query(Person).all()
        for data in persons:
            print(data)
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()
get_all_users()

def get_by_id(id:int):
    try:
        session = SessionLocal()
        persons = session.query(Person).filter(Person.id==id).first()
        print(persons)
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()

get_by_id(3)

def update(id:int,email:str):
    try:
        session = SessionLocal()
        persons = session.query(Person).filter(Person.id==id).first()
        if not persons:
            print("Not found")
        persons.email = email
        session.commit()
        session.refresh(persons)
        print(persons)
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()

update(3,"arjun@ust.com")

def delete(id:int):
    try:
        session = SessionLocal()
        persons = session.query(Person).filter(Person.id==id).first()
        if not persons:
            print("Not found")
        session.delete(persons)
        session.commit()
        print("Deleted")
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()

delete(7)