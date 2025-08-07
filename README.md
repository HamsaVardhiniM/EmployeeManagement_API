# Employee Management API

A simple and efficient Employee Management System built with Python FastAPI, featuring a modern web UI and comprehensive REST API endpoints.

## Features

- ✅ **Add new employee** - Create new employee records
- ✅ **Get all employees** - Retrieve all employee data
- ✅ **Get employee by ID** - Retrieve specific employee information
- ✅ **Update employee** - Modify existing employee data
- ✅ **Delete employee** - Remove employee records
- 🎨 **Modern Web UI** - Professional interface for seamless interaction
- 📚 **Interactive API Documentation** - Swagger UI for API testing
- 💾 **In-Memory Storage** - No database required, uses dictionaries/lists
- ✅ **Data Validation** - Pydantic models for request/response validation

## Project Structure

```
workspace/
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic data models
├── storage.py           # In-memory storage implementation
├── crud.py              # CRUD operations
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html      # Web UI template
└── README.md           # This file
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Access the Application

- **Web UI**: http://localhost:8000
- **API Documentation (Swagger)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### Base URL: `http://localhost:8000/api`

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/employees/` | Create new employee | EmployeeCreate |
| GET | `/employees/` | Get all employees | - |
| GET | `/employees/{id}` | Get employee by ID | - |
| PUT | `/employees/{id}` | Update employee | EmployeeUpdate |
| DELETE | `/employees/{id}` | Delete employee | - |

### Data Models

#### Employee
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering",
  "position": "Senior Developer",
  "salary": 85000.0,
  "hire_date": "2024-01-15T10:30:00"
}
```

#### EmployeeCreate (Request)
```json
{
  "name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering",
  "position": "Senior Developer",
  "salary": 85000.0
}
```

#### EmployeeUpdate (Request)
```json
{
  "name": "John Smith",
  "email": "john.smith@company.com",
  "department": "Engineering",
  "position": "Lead Developer",
  "salary": 95000.0
}
```

## API Usage Examples

### Using cURL

#### Create Employee
```bash
curl -X POST "http://localhost:8000/api/employees/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice.johnson@company.com",
    "department": "Design",
    "position": "UI/UX Designer",
    "salary": 70000.0
  }'
```

#### Get All Employees
```bash
curl -X GET "http://localhost:8000/api/employees/"
```

#### Get Employee by ID
```bash
curl -X GET "http://localhost:8000/api/employees/1"
```

#### Update Employee
```bash
curl -X PUT "http://localhost:8000/api/employees/1" \
  -H "Content-Type: application/json" \
  -d '{
    "salary": 90000.0,
    "position": "Senior UI/UX Designer"
  }'
```

#### Delete Employee
```bash
curl -X DELETE "http://localhost:8000/api/employees/1"
```

### Using Python Requests

```python
import requests

base_url = "http://localhost:8000/api"

# Create employee
new_employee = {
    "name": "Bob Wilson",
    "email": "bob.wilson@company.com",
    "department": "Sales",
    "position": "Sales Manager",
    "salary": 75000.0
}
response = requests.post(f"{base_url}/employees/", json=new_employee)
print(response.json())

# Get all employees
response = requests.get(f"{base_url}/employees/")
print(response.json())

# Update employee
update_data = {"salary": 80000.0}
response = requests.put(f"{base_url}/employees/1", json=update_data)
print(response.json())
```

## Web UI Features

The web interface provides:

- **Dashboard Overview**: Employee count, departments, average salary
- **Employee Directory**: Sortable table with all employee information
- **Add Employee**: Modal form for creating new employees
- **Edit Employee**: In-place editing with API integration
- **Delete Employee**: Confirmation dialog for safe deletion
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: Immediate UI updates after API operations

## Data Validation

The API includes comprehensive data validation:

- **Name**: 1-100 characters, required
- **Email**: Valid email format, required
- **Department**: 1-50 characters, required
- **Position**: 1-50 characters, required
- **Salary**: Positive number, required
- **Hire Date**: Automatically set to current datetime

## Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `404` - Not Found
- `422` - Unprocessable Entity (invalid data format)

## Testing

### Swagger UI Testing
1. Go to http://localhost:8000/docs
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the required parameters
5. Click "Execute" to test the API

### Postman Testing
Import the following collection or manually create requests:

```json
{
  "info": {
    "name": "Employee Management API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Create Employee",
      "request": {
        "method": "POST",
        "header": [{"key": "Content-Type", "value": "application/json"}],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"name\": \"Test Employee\",\n  \"email\": \"test@company.com\",\n  \"department\": \"IT\",\n  \"position\": \"Developer\",\n  \"salary\": 60000.0\n}"
        },
        "url": {
          "raw": "http://localhost:8000/api/employees/",
          "protocol": "http",
          "host": ["localhost"],
          "port": "8000",
          "path": ["api", "employees", ""]
        }
      }
    }
  ]
}
```

## Sample Data

The application starts with 3 sample employees:
- John Doe (Engineering, Senior Developer)
- Jane Smith (Marketing, Marketing Manager)  
- Bob Johnson (HR, HR Specialist)

## Architecture

- **FastAPI**: Modern Python web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Jinja2**: Template engine for rendering HTML
- **Bootstrap 5**: CSS framework for responsive UI
- **Font Awesome**: Icon library for UI elements

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.