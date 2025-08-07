from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
import crud
from models import Employee, EmployeeCreate, EmployeeUpdate

# Initialize FastAPI app
app = FastAPI(
    title="Employee Management API",
    description="A simple and efficient employee management system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Error handler for validation errors
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": "Invalid data", "details": str(exc)}
    )

@app.get("/", summary="Root endpoint")
async def root():
    """Welcome message and API information"""
    return {
        "message": "Welcome to Employee Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "GET /employees": "Get all employees",
            "GET /employees/{id}": "Get employee by ID",
            "POST /employees": "Create new employee",
            "PUT /employees/{id}": "Update employee",
            "DELETE /employees/{id}": "Delete employee"
        }
    }

@app.post("/employees", 
          response_model=Employee, 
          status_code=status.HTTP_201_CREATED,
          summary="Create new employee")
async def create_employee(employee: EmployeeCreate):
    """
    Create a new employee with the following information:
    - **name**: Employee full name
    - **email**: Employee email (must be unique)
    - **department**: Department name
    - **position**: Job position
    - **salary**: Employee salary (must be positive)
    """
    # Check if email already exists
    if crud.check_email_exists(employee.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    return crud.create_employee(employee)

@app.get("/employees", 
         response_model=List[Employee],
         summary="Get all employees")
async def get_all_employees():
    """
    Retrieve all employees in the system.
    Returns a list of all employee records.
    """
    employees = crud.get_all_employees()
    return employees

@app.get("/employees/{employee_id}", 
         response_model=Employee,
         summary="Get employee by ID")
async def get_employee(employee_id: int):
    """
    Retrieve a specific employee by their ID.
    - **employee_id**: The ID of the employee to retrieve
    """
    employee = crud.get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee

@app.put("/employees/{employee_id}", 
         response_model=Employee,
         summary="Update employee")
async def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    """
    Update an existing employee's information.
    - **employee_id**: The ID of the employee to update
    - You can update any combination of: name, email, department, position, salary
    """
    # Check if employee exists
    existing_employee = crud.get_employee_by_id(employee_id)
    if not existing_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    # Check email uniqueness if email is being updated
    if employee_data.email and crud.check_email_exists(employee_data.email, employee_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    updated_employee = crud.update_employee(employee_id, employee_data)
    return updated_employee

@app.delete("/employees/{employee_id}",
           status_code=status.HTTP_204_NO_CONTENT,
           summary="Delete employee")
async def delete_employee(employee_id: int):
    """
    Delete an employee from the system.
    - **employee_id**: The ID of the employee to delete
    """
    success = crud.delete_employee(employee_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return None

# Health check endpoint
@app.get("/health", summary="Health check")
async def health_check():
    """Check if the API is running properly"""
    return {"status": "healthy", "employees_count": len(crud.get_all_employees())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
