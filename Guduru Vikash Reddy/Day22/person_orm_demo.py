from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import  sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:password123@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
class Person(Base):
    __tablename__="persons"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),nullable=False,unique=True)
    
    def __repr__(self):
        return f"User(id ={self.id},name = {self.name},email ={self.email})"
    
print("creating the table in mysql")
Base.metadata.create_all(bind=engine)
print("table created")

def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_person=Person(name=name,email=email)
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

def get_all():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
        return persons
    except Exception as e:
        session.rollback()
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def get_person_by_id(id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==id).first()
        return person
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def update_person_by_id(id:int,new_email:str):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==id).first()
        if person is None:
            print("Person Not Found")
            return None
        person.email=new_email
        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def delete_person_by_id(id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==id).first()
        if person is None:
            print("Person Not Found")
            return None
        session.delete(person)
        session.commit()
        return "deleted"
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
    
        



if __name__ == "__main__":
    # user = create_user("ram", "ram24@gmail.com")
    # print(user)
    
    # data=get_all()
    # for row in data:
    #     print(row)\
        
    # print(get_person_by_id(4) )   
    
    # print(update_person_by_id(4,"mango@gmail.com"))
    
    print(delete_person_by_id(7))