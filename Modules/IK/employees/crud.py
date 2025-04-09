from sqlalchemy.orm import Session
from .models import Employee  # Employee modelini import ediyoruz
from .schemas import EmployeeCreate, EmployeeUpdate

# Create a new employee
def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(
        name=employee.name,
        hire_date=employee.hire_date
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Get all employees
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

# Get an employee by ID
def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()

# Update employee details
def update_employee(db: Session, employee_id: int, employee: EmployeeUpdate):
    db_employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if db_employee:
        if employee.name:
            db_employee.name = employee.name
        if employee.hire_date:
            db_employee.hire_date = employee.hire_date
        db.commit()
        db.refresh(db_employee)
    return db_employee

# Delete an employee
def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
