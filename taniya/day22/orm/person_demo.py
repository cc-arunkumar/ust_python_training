from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class Person(Base):
    __tablename__='Person'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=True)
    
    def __repr__(self):
        return f"User(id={self.id},name='{self.name}',email='{self.email}')"
print("Creating tables in MySQL DB..")
Base.metadata.create_all(bind=engine)
print("Table creation completed")


def create_user(name:str,email:str):
    try:
        session = SessionLocal()
        new_person = Person(name=name,email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()
    return new_person

def get_all_users():
    session=SessionLocal()
    persons=session.query(Person).all()
    session.close()
    return persons
def get_person_by_id(person_id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    session.close()
    return person

def update_user(person_id: int, new_name: str, new_email: str):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
        if not person:
            print(f"No user found with id={person_id}")
            return None

        if new_name:
            person.name = new_name
        if new_email:
            person.email = new_email

        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception while updating user:", e)
        return None
    finally:
        session.close()
        
def delete_user(person_id: int):
    
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("Person not found")
            session.close()
            return None

        session.delete(person)
        session.commit()
        print(f"User with id={person_id} deleted successfully")
        session.close()

if __name__ == "__main__":
    # person = create_user("Taniya", "taniya22@gmail.com")
    # print(person)

    # person = create_user("Tanu", "taniya2219@gmail.com")
    # print(person)

    # person = create_user("Tanvi", "tanvii21220@gmail.com")
    # print(person)

    # users = get_all_users()
    # for user in users:
    #     # print("All users:", user)
    #     print("id :",user.id,"name :",user.name,"email :",user.email)
    # person_id = get_person_by_id(5)
    # if person_id:
    #     print("id :",person_id.id,"name :",person_id.name,"email :",person_id.email)
    # else:
    #     print("no user found",person_id)
        
    # updated = update_user(5, new_name="Tanu singh", new_email="tanu2219@gmail.com")
    # print("Updated user:", updated)
    # deleted = delete_user(8)
    # if deleted:
    #     print("user deleted successfully")
    users = get_all_users()
    for user in users:
        # print("All users:", user)
        print("id :",user.id,"name :",user.name,"email :",user.email)
