from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
import os

from models import Employee, EmployeeCreate, EmployeeUpdate, EmployeeResponse
from crud import employee_crud

# Create FastAPI app
app = FastAPI(
    title="Employee Management API",
    description="A simple and efficient Employee Management System with CRUD operations",
    version="1.0.0"
)

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create templates directory if it doesn't exist
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# API Endpoints

@app.post("/api/employees/", response_model=EmployeeResponse, status_code=201)
async def create_employee(employee: EmployeeCreate):
    """Create a new employee"""
    try:
        new_employee = employee_crud.create_employee(employee)
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/employees/", response_model=List[EmployeeResponse])
async def get_all_employees():
    """Get all employees"""
    return employee_crud.get_all_employees()

@app.get("/api/employees/{employee_id}", response_model=EmployeeResponse)
async def get_employee(employee_id: int):
    """Get employee by ID"""
    employee = employee_crud.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/api/employees/{employee_id}", response_model=EmployeeResponse)
async def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    """Update an existing employee"""
    if not employee_crud.employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    
    updated_employee = employee_crud.update_employee(employee_id, employee_data)
    if not updated_employee:
        raise HTTPException(status_code=400, detail="Failed to update employee")
    
    return updated_employee

@app.delete("/api/employees/{employee_id}")
async def delete_employee(employee_id: int):
    """Delete an employee"""
    if not employee_crud.employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    
    success = employee_crud.delete_employee(employee_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete employee")
    
    return {"message": "Employee deleted successfully"}

# Web UI Endpoints

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Main UI page"""
    employees = employee_crud.get_all_employees()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "employees": employees
    })

@app.post("/employees/create", response_class=HTMLResponse)
async def create_employee_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    department: str = Form(...),
    position: str = Form(...),
    salary: float = Form(...)
):
    """Create employee via form"""
    try:
        employee_data = EmployeeCreate(
            name=name,
            email=email,
            department=department,
            position=position,
            salary=salary
        )
        employee_crud.create_employee(employee_data)
        employees = employee_crud.get_all_employees()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "employees": employees,
            "success": "Employee created successfully!"
        })
    except Exception as e:
        employees = employee_crud.get_all_employees()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "employees": employees,
            "error": str(e)
        })

@app.post("/employees/{employee_id}/delete", response_class=HTMLResponse)
async def delete_employee_form(request: Request, employee_id: int):
    """Delete employee via form"""
    try:
        if not employee_crud.employee_exists(employee_id):
            raise Exception("Employee not found")
        
        employee_crud.delete_employee(employee_id)
        employees = employee_crud.get_all_employees()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "employees": employees,
            "success": "Employee deleted successfully!"
        })
    except Exception as e:
        employees = employee_crud.get_all_employees()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "employees": employees,
            "error": str(e)
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)