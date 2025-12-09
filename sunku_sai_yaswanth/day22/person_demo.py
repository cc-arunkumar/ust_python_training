from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:1234@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=False)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class Person(Base):
    __tablename__='persons'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id= {self.id},name= '{self.name}', email='{self.email}')"
    
print("Creating tables in mysql")
Base.metadata.create_all(bind=engine)
print("Table creation complete")




# def create_user(name:str,email:str):
#     try:
#         session=SessionLocal()
#         new_person=Person(name=name,email=email)
#         session.add(new_person)
#         session.commit()
#         session.refresh(new_person)
#     except Exception as e:
#         session.rollback()
#         print("Error: ",e)
#         return None
#     finally:
#         session.close()
#     return new_person

# if __name__=="__main__":
#     created_user=create_user("yaswanth","yaswanth@gmail.com")
    
#     if created_user:
#         print(f"Created User: {created_user}")


# def get_all_persons():
#     try:
#         session=SessionLocal()
#         persons=session.query(Person).all()
#         session.close()
#         return persons
#     except Exception as e:
#         session.rollback()
#         print("Error:",e)
#     finally:
#         session.close()
        
# if __name__=="__main__":        
#     get_persons=get_all_persons()
#     for i in get_persons:
#         print(i)
        
        
# def get_person_by_id(person_id:int):
#     try:
#         session=SessionLocal()
#         person=session.query(Person).filter(Person.id == person_id).first()
#         session.close()
#         return person
#     except Exception as e:
#         session.rollback()
#         print("Error:",e)
#     finally:
#         session.close()

        
# if __name__=="__main__":        
#     get_persons_id=get_person_by_id(3)
#     print(get_persons_id)

def update_person(person_id:int,new_email:str):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("person not found")
        session.close()
        return None
    person.email=new_email
    # session.(person)
    session.commit()
    session.close()
    return person

delete=update_person(3,"name@gmail.com")      

# def delete_person(person_id:int):
#     session=SessionLocal()
#     person=session.query(Person).filter(Person.id==person_id).first()
    
#     if person is None:
#         print("person not found")
#         session.close()
#         return None
#     session.delete(person)
#     session.commit()
#     session.close()
#     return person

# delete=delete_person(4)

        
        
