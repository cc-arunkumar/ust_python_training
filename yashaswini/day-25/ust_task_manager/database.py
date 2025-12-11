from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import TaskModel


database_url = "mysql+pymysql://root:password123@localhost:3306/task_manger_db"

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    # name = Column(String(50), nullable=False)
    password=Column(String(50), nullable=False)

    # One employee → Many tasks
    tasks = relationship("Tasks", back_populates="employee")

    def __repr__(self):
        return f"<Employee user_id={self.user_id}, name='{self.name}'>"


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)

    # FK must match Employee.user_id datatype (Integer)
    user_id = Column(Integer, ForeignKey("employees.user_id"), nullable=False)

    # Many tasks → One employee
    employee = relationship("Employee", back_populates="tasks")

    def __repr__(self):
        return f"<Task id={self.id}, title='{self.title}', user_id={self.user_id}>"


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")


# def create_task(task: TaskModel, current_user: User = Depends(get_current_user)):
from sqlalchemy.orm import Session
from db_connection import SessionLocal

# class Tasks


# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
          
# def create_task_db(db: Session, task, user_id: int):
#     new_task = Tasks(
#         title=task.title,
#         description=task.description,
#         user_id=user_id
#     )

#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)
#     return new_task
