from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base


DATABASE_URL="mysql+pymysql://root:1234@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)

SessionaLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class Person(Base):
    __tablename__='persons'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=True)
    
    def __repr__(self):
        return f"User(id={self.id} | name ={self.name}  | email= {self.email})"
    
print("Creating tables in MYsql Db...")
Base.metadata.create_all(bind=engine)

print("Table creation completed")




def create_user(name:str,email:str):
    try:
        #create session
        session=SessionaLocal()
        
        #create user
        new_person=Person(name=name,email=email)
        
        #add new person to session
        session.add(new_person)
        
        #commit session        
        session.commit()
        
        #refresh session
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    
    finally:
        
        #close session
        session.close()
    print(f"Name:{new_person.name}  | Email:{new_person.email}")  
    return new_person



def get_all_users():
    try:
        session=SessionaLocal()
        
        persons=session.query(Person).all()
      
        return persons
            
    except Exception as e:
        session.rollback()
        
        print("Exception", e)
        return None
    
    finally:
        session.close()
        
def get_person_by_id(person_id:int):
    try:
        session=SessionaLocal()
        
        person=session.query(Person).filter(Person.id==person_id).first()
        
    except Exception as e:
        session.rollback()
        print("exception",e)
    
    finally:
        session.close()
        
    return person       

def update_person_by_id(person_id:int, new_email=str):
    session=SessionaLocal()
    
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("Person Not found")
        session.close()
        return None
    
    person.email=new_email
    session.commit()
    session.close()
    return person

def delete_person_by_id(person_id:int):
    session=SessionaLocal()
    
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("Person Not found")
        session.close()
        return None
    
    session.delete(person)
    session.commit()
    session.close()
    return person

if __name__=="__main__":
    
    # create_user("sai","yash@gmail.com")
    # person=get_all_users()
    # for i in person:
    #     print(i)
    

    # update_person_by_id(2,"niranjan123@gmail.com")
    
    delete_person_by_id(3)
    
    
    # print(get_person_by_id(1))
    
    
