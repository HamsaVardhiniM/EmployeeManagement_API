from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100, description="Employee full name")
    email: str = Field(..., pattern=r'^[^@]+@[^@]+\.[^@]+$', description="Employee email address")
    department: str = Field(..., min_length=1, max_length=50, description="Employee department")
    position: str = Field(..., min_length=1, max_length=50, description="Employee position")
    salary: float = Field(..., gt=0, description="Employee salary")
    hire_date: datetime = Field(default_factory=datetime.now, description="Employee hire date")

class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Employee full name")
    email: str = Field(..., pattern=r'^[^@]+@[^@]+\.[^@]+$', description="Employee email address")
    department: str = Field(..., min_length=1, max_length=50, description="Employee department")
    position: str = Field(..., min_length=1, max_length=50, description="Employee position")
    salary: float = Field(..., gt=0, description="Employee salary")

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Employee full name")
    email: Optional[str] = Field(None, pattern=r'^[^@]+@[^@]+\.[^@]+$', description="Employee email address")
    department: Optional[str] = Field(None, min_length=1, max_length=50, description="Employee department")
    position: Optional[str] = Field(None, min_length=1, max_length=50, description="Employee position")
    salary: Optional[float] = Field(None, gt=0, description="Employee salary")

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    position: str
    salary: float
    hire_date: datetime
    
    class Config:
        from_attributes = True