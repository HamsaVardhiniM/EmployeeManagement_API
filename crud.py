from typing import List, Optional
from models import Employee, EmployeeCreate, EmployeeUpdate
from storage import employee_storage

class EmployeeCRUD:
    def __init__(self):
        self.storage = employee_storage
    
    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        """Create a new employee"""
        return self.storage.add_employee(employee_data)
    
    def get_all_employees(self) -> List[Employee]:
        """Get all employees"""
        return self.storage.get_all_employees()
    
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID"""
        return self.storage.get_employee_by_id(employee_id)
    
    def update_employee(self, employee_id: int, employee_data: EmployeeUpdate) -> Optional[Employee]:
        """Update an existing employee"""
        return self.storage.update_employee(employee_id, employee_data)
    
    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee"""
        return self.storage.delete_employee(employee_id)
    
    def employee_exists(self, employee_id: int) -> bool:
        """Check if employee exists"""
        return self.storage.employee_exists(employee_id)

# Global CRUD instance
employee_crud = EmployeeCRUD()