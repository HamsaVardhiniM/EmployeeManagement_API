from typing import List, Optional
from datetime import datetime
from database import db
from models import Employee, EmployeeCreate, EmployeeUpdate

def create_employee(employee_data: EmployeeCreate) -> Employee:
    """Create a new employee"""
    employee_id = db.get_next_id()
    now = datetime.now()
    
    employee = Employee(
        id=employee_id,
        name=employee_data.name,
        email=employee_data.email,
        department=employee_data.department,
        position=employee_data.position,
        salary=employee_data.salary,
        created_at=now,
        updated_at=now
    )
    
    db.employees[employee_id] = employee
    return employee

def get_all_employees() -> List[Employee]:
    """Get all employees"""
    return list(db.employees.values())

def get_employee_by_id(employee_id: int) -> Optional[Employee]:
    """Get employee by ID"""
    return db.employees.get(employee_id)

def update_employee(employee_id: int, employee_data: EmployeeUpdate) -> Optional[Employee]:
    """Update employee data"""
    employee = db.employees.get(employee_id)
    if not employee:
        return None
    
    # Update only provided fields
    update_data = employee_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(employee, field, value)
    
    employee.updated_at = datetime.now()
    db.employees[employee_id] = employee
    return employee

def delete_employee(employee_id: int) -> bool:
    """Delete employee"""
    if employee_id in db.employees:
        del db.employees[employee_id]
        return True
    return False

def check_email_exists(email: str, exclude_id: Optional[int] = None) -> bool:
    """Check if email already exists"""
    for emp_id, employee in db.employees.items():
        if employee.email == email and emp_id != exclude_id:
            return True
    return False
