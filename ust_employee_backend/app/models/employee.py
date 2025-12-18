from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class EmployeeDB(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    designation = Column(String(100), nullable=False)

    manager_id = Column(
        Integer,
        ForeignKey("employees.emp_id"),
        nullable=True
    )

    manager = relationship(
        "EmployeeDB",
        remote_side=[emp_id],
        backref="subordinates"
    )

    user = relationship(
        "UserDB",
        back_populates="employee",
        uselist=False
    )
