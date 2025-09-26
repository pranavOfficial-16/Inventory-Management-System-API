# Inventory Management System API

A FastAPI-based backend API to track products in a warehouse.

## 1. Tech Stack & Libraries

### Backend Framework
- **FastAPI** - Modern, fast web framework for building APIs with Python
- **Uvicorn** - ASGI server for running FastAPI applications

### Database & ORM
- **SQLite** - Lightweight disk-based database, perfect for development and small applications
- **SQLAlchemy** - Python SQL toolkit and Object-Relational Mapping (ORM) library

### Data Validation
- **Pydantic** - Data validation and settings management using Python type annotations

## 2. Core Features

### Product Management
- List all products
- Create Products
- Get specific product
- Update product
- Delete product
- Increase Stock
- Decrease Stock (with validation)
- Low stock threshold products

## 3. Design Choices & Architecture

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

## 4. Setup & Installation

### Clone the repository

git clone https://github.com/your-username/inventory-management-system-api.git
cd inventory-management-system-api

### Create & activate a virtual environment

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate
