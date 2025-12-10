from sqlalchemy import create_engine,Column,Integer,String 
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASEURL = 'mysql+pymysql://root:password123@localhost:3306/ust_db'
engine = create_engine(DATABASEURL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)
Base = declarative_base()

class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,nullable=False, index=True)
    name = Column(String(50),nullable=False)
    age = Column(Integer, nullable=False )
    
    def __repr__(self):
        return f"User - id : {self.id}, name : {self.name}, age: {self.age}"

Base.metadata.create_all(bind=engine)

def create_user(new_user : User):
    try:
        session = SessionLocal()
        
        session.add(new_user)
        
        session.commit()
        
        session.refresh(new_user)
        
        return new_user
        
    except Exception as e:
        session.rollback()
        
        print("Error:",e)
        return False 
    
    finally:
        session.close()

# print(create_user(User(name='Anjan',age=21)))
        
        