from app.database.connection import SessionLocal, engine, Base
from app.models.employee import Employee
from app.models.user import User, UserRole, UserStatus
from app.utils.auth import create_access_token

# Create tables just in case
Base.metadata.create_all(bind=engine)

session = SessionLocal()
try:
    # Create an employee
    emp = Employee(name="Admin User", email="admin@example.com", designation="Administrator")
    session.add(emp)
    session.commit()
    session.refresh(emp)
    print("Created employee with emp_id:", emp.emp_id)

    # Create corresponding user
    user = User(emp_id=emp.emp_id, password="password@123", role=UserRole.admin, status=UserStatus.active)
    session.add(user)
    session.commit()
    print("Created admin user for emp_id:", emp.emp_id)

    # Print a token for convenience
    token = create_access_token({"emp_id": str(emp.emp_id), "role": user.role.value})
    print("Use this token to authenticate (emp_id and password):")
    print("emp_id=", emp.emp_id)
    print("password=password@123")
    print("token=", token)
finally:
    session.close()
