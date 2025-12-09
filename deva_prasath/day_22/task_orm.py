from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=True,autocommit=False)


Base=declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(50))
    user_address=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},user_name={self.user_name},user_address={self.user_address},email={self.email})"

# Base.metadata.create_all(bind=engine)


def create_user(user_name:str,user_address:str,email:str):
    try:
        session=SessionLocal()
        new_user=User(user_name=user_name,user_address=user_address,email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    
    return new_user

def get_all_users():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        return users
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
        
def get_user_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        return user
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
        
    
def update_user_by_id(user_id:int,user_name:str,user_address:str,email:str):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        user.user_name=user_name
        user.user_address=user_address
        user.email=email
        return user
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()

def delete_user_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        if user is None:
            print("User not found!")
            session.close()
            return None
        session.delete(user)
        session.commit()
        return user
    
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()


# create_user("Dustin","Hawkins","dustin@gmail.com")

print(get_all_users())
print("----------------------")
print(get_user_by_id(1))
print("----------------------")
update_user_by_id(1,"Will","hawk","will@gmail.com")