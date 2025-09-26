# Inventory Management System API

A robust FastAPI-based backend API for warehouse inventory management with real-time stock tracking and low-stock alerts.
A FastAPI-based backend API to track products in a warehouse.

## Tech Stack & Libraries

### Backend Framework

- **FastAPI** - Modern, fast web framework for building APIs with Python
- **Uvicorn** - ASGI server for running FastAPI applications

### Database & ORM
- **SQLite** - Lightweight disk-based database, perfect for development and small applications
- **SQLAlchemy** - Python SQL toolkit and Object-Relational Mapping (ORM) library

### Data Validation
- **Pydantic** - Data validation and settings management using Python type annotations

## Core Features

### Product Management
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

**On Windows (PowerShell):**

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
