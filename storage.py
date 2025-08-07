from typing import Dict, List, Optional
from models import Employee, EmployeeCreate, EmployeeUpdate
from datetime import datetime

class EmployeeStorage:
    def __init__(self):
        self.employees: Dict[int, Employee] = {}
        self.next_id: int = 1
        
        # Add some sample data
        self._add_sample_data()
    
    def _add_sample_data(self):
        """Add sample employees for demonstration"""
        sample_employees = [
            EmployeeCreate(
                name="John Doe",
                email="john.doe@company.com",
                department="Engineering",
                position="Senior Developer",
                salary=85000.0
            ),
            EmployeeCreate(
                name="Jane Smith",
                email="jane.smith@company.com",
                department="Marketing",
                position="Marketing Manager",
                salary=65000.0
            ),
            EmployeeCreate(
                name="Bob Johnson",
                email="bob.johnson@company.com",
                department="HR",
                position="HR Specialist",
                salary=55000.0
            )
        ]
        
        for emp_data in sample_employees:
            self.add_employee(emp_data)
    
    def add_employee(self, employee_data: EmployeeCreate) -> Employee:
        """Add a new employee to storage"""
        employee = Employee(
            id=self.next_id,
            **employee_data.model_dump()
        )
        self.employees[self.next_id] = employee
        self.next_id += 1
        return employee
    
    def get_all_employees(self) -> List[Employee]:
        """Get all employees"""
        return list(self.employees.values())
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID"""
        return self.employees.get(employee_id)
    
    def update_employee(self, employee_id: int, employee_data: EmployeeUpdate) -> Optional[Employee]:
        """Update an existing employee"""
        if employee_id not in self.employees:
            return None
        
        employee = self.employees[employee_id]
        update_data = employee_data.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(employee, field, value)
        
        return employee
    
    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee by ID"""
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False
    
    def employee_exists(self, employee_id: int) -> bool:
        """Check if employee exists"""
        return employee_id in self.employees

# Global storage instance
employee_storage = EmployeeStorage()