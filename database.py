from typing import Dict, List
from datetime import datetime
from models import Employee, EmployeeCreate

class InMemoryDatabase:
    def __init__(self):
        self.employees: Dict[int, Employee] = {}
        self.next_id: int = 1
    
    def get_next_id(self) -> int:
        current_id = self.next_id
        self.next_id += 1
        return current_id
    
    def reset(self):
        """Reset database for testing purposes"""
        self.employees.clear()
        self.next_id = 1

# Global database instance
db = InMemoryDatabase()
