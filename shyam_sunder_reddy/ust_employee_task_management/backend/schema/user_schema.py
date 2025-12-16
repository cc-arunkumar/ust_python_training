from sqlalchemy import Column, Integer, String, ForeignKey,ARRAY,JSON
from database.sql_db import Base, engine


class UserSchema(Base):
    __tablename__ = "users"
    e_id = Column(Integer, primary_key=True, index=True)
    password = Column(String(100), nullable=False)
    role = Column(JSON, nullable=False)  
    status = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<User(e_id={self.e_id}, role={self.role}, status={self.status})>"


Base.metadata.create_all(bind=engine)