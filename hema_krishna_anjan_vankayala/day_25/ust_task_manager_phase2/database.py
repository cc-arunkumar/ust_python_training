from sqlalchemy import create_engine,Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base,relationship
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models import TaskSchema,UserSchema
from mongodb_logger import logger
DATABASEURL = "mysql+pymysql://root:password123@localhost:3306/ust_mysql_db"
engine = create_engine(DATABASEURL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

#Task ORM Class
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True, index=True, unique =True)
    title = Column(String(50),nullable=False,unique=True)
    description = Column(String(100),nullable=False)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    
    user = relationship("User",back_populates="tasks")
    
    def __repr__(self):
        return f'Task(id = {self.id}, title = {self.title}, description = {self.description}, completed = {self.completed}, user_id= {self.user_id})'
  
#User ORM Class  
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String(50),nullable=False, unique=True)
    user_password = Column(String(50),nullable=False)
    tasks = relationship("Task",back_populates="user")
    
    def __repr__(self):
        return f'User(id = {self.user_id}, user_name= {self.user_name}, user_password ={self.user_password})'
    
    
# Base.metadata.create_all(bind=engine)

#Create User
def create_user(name:str,password:str):
    try:
        #1.Create session
        session = SessionLocal()
        #Create User
        new_person = User(user_name=name,user_password=password)
        #Add User in Session
        session.add(new_person)
        #Commit Session
        session.commit()
        #Refresh Session
        session.refresh(new_person)
        
        logger.info(f"User created: {new_person.user_name}")
        
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        session.rollback()
        print("Exception:",e)
    
    finally:
        #Close Session
        session.close()
    
    return new_person
  
# create_user("rahul","password123")
def fetch_user_by_name(name,password):
    try:
        #create Session
        session = SessionLocal()
        #Execute Query to get all the Users
        person = session.query(User).filter(User.user_name==name, User.user_password==password).first()
        #Returns the List
        return person.user_id
        
    except Exception as e:

        session.rollback()
        print("Error:",e)
        
    finally:
        session.close()

#Fetch User by ID        
def fetch_user_by_id(id):
    try:
        #create Session
        session = SessionLocal()
        #Execute Query to get all the Users
        person = session.query(User).filter(User.user_id==id).first()
        #Returns the List
        return person.user_id
        
    except Exception as e:

        session.rollback()
        print("Error:",e)
        
    finally:
        session.close()

#Read Task by ID
def read_task_by_title(title):
    try:
        #create Session
        session = SessionLocal()
        #Execute Query to get all the Users
        task = session.query(Task).filter(Task.title==title).first()
        #Returns the List
        if task is not None:
            return task 
        else:
            return False
        
    except Exception as e:

        session.rollback()
        print("Error:",e)
        
    finally:
        session.close()
        
#Create a New Task
def create_new_task(new_task:TaskSchema,user_id):
    try:
        
        #1.Create session
        session = SessionLocal()
        #Create User
        new_task_data = Task(title=new_task.title,
                             description=new_task.description,
                             completed=new_task.completed,
                             user_id=user_id)
        #Add User in Session
        session.add(new_task_data)
        #Commit Session
        session.commit()
        #Refresh Session
        session.refresh(new_task_data)
        
        return new_task_data

    except IntegrityError:
        session.rollback()
        # Raise a clean error instead of raw DB error
        raise HTTPException(
            status_code=400,
            detail="Task with this title already exists"
        )
        
    except Exception as e:
        session.rollback()
        raise Exception(f"{e}")
    
    finally:
        #Close Session
        session.close()
    
# READ all tasks for a user
def read_all_tasks(user_id: int):
    session = SessionLocal()
    try:
        tasks = session.query(Task).filter(Task.user_id == user_id).all()
        return tasks
    finally:
        session.close()

# READ single task by ID
def read_task_by_id(task_id: int, user_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        return task
    finally:
        session.close()

# UPDATE task
def update_task(task_id: int, user_id: int, updated_task: TaskSchema):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None
        task.title = updated_task.title
        task.description = updated_task.description
        task.completed = updated_task.completed
        session.commit()
        session.refresh(task)
        return task
    except IntegrityError:
        session.rollback()
        raise Exception("Task with this title already exists")
    finally:
        session.close()

# DELETE task
def delete_task(task_id: int, user_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None
        session.delete(task)
        session.commit()
        return True
    finally:
        session.close()

# print(create_new_task(Task(title="new Task", description="thi si taks"), 1))