# Inventory Management System API

A FastAPI-based backend API to track products in a warehouse.

## Tech Stack & Libraries

### Backend Framework

- **FastAPI** - Modern web framework for building high-performance APIs using Python
- **Uvicorn** - ASGI server for running FastAPI applications

### Database & ORM

- **SQLite** - Lightweight disk-based database, perfect for development and small applications
- **SQLAlchemy** - ORM (Object-Relational Mapper) for database operations

### Data Validation

- **Pydantic** - Data validation library for API inputs and outputs

## Core Features

- List all products
- Create Products
- Get specific product
- Update product
- Delete product
- Increase Stock
- Decrease Stock (with validation)
- Low stock threshold products

## Design Choices & Architecture

### Database Design

- **SQLite for Simplicity**: Chose SQLite for easy setup and development-friendly environment
- **ORM over Raw SQL**: Used SQLAlchemy ORM for better maintainability and type safety
- **Explicit Schema Definition**: Defined clear database models with proper constraints

### API Architecture

- **Separation of Concerns**: Separate files for models, schemas, database config, and routes
- **Dependency Injection**: Used FastAPI's dependency system for database sessions
- **RESTful Conventions**: Followed standard HTTP methods and status codes

### Validation Strategy

- **Pydantic Models**: Used for request validation
- **Proper Error Handling**: Meaningful HTTP status codes and error messages

### Business Logic Placement

- **Route-level Logic**: Kept business logic in endpoint handlers for clarity
- **Database Constraints**: Used application-level validation alongside database constraints
- **Atomic Operations**: Database commits happen after successful validation

## Setup & Installation

### 1. Clone the repository

```sh
git clone https://github.com/your-username/Inventory-Management-System-API.git
cd inventory-management-system-api
```

### 2. Create and activate a virtual environment

**On Windows:**

```sh
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the server

**From the project root directory:**

```sh
uvicorn src.main:app --reload
```

### Access the API

- Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to check if the API is running.
- To test and explore the API, open the interactive Swagger documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
