# Task Management System - Project Report

## **Overview**

The Task Management System is a backend project developed using FastAPI and PostgreSQL. It allows users to register, log in, and manage tasks with features such as task categorization, priority levels, due dates, and user-specific filters. The system also implements token-based authentication to ensure secure user access.

---

## **Features**

1. **User Management**

   - User registration and login.
   - Password hashing using bcrypt.
   - Token-based authentication using JSON Web Tokens (JWT).

2. **Task Management**

   - Create, update, delete, and retrieve tasks.
   - Filters for tasks based on category, priority, and due date.
   - Tasks are associated with specific users.

3. **Database Integration**

   - Asynchronous interaction with PostgreSQL using SQLAlchemy.
   - User and task data persistence.

4. **Security**

   - Secure password storage with hashing.
   - Token-based user authentication with expiration.

---

## **Project Structure**

```
app/
|-- database.py      # Database configuration and session management
|-- models.py        # SQLAlchemy models for User and Task
|-- schemas.py       # Pydantic models for request/response validation
|-- routes/
    |-- auth.py      # Authentication routes (register, login)
    |-- tasks.py     # Task management routes (CRUD operations)
|-- utils/
    |-- auth.py      # Utility functions for hashing passwords and creating JWTs
main.py              # Application entry point
```

---

## **Database Models**

### **User Model**

- Fields:
  - `id`: Primary key
  - `username`: Unique username
  - `hashed_password`: Securely stored password

### **Task Model**

- Fields:
  - `id`: Primary key
  - `title`: Task title
  - `description`: Optional description
  - `due_date`: Optional due date
  - `priority`: Optional priority level
  - `category`: Optional category
  - `user_id`: Foreign key linking to User

---

## **Authentication**

### **Endpoints**

1. **Register User**

   - Endpoint: `POST /auth/register`
   - Request Body:
     ```json
     {
       "username": "testuser",
       "password": "securepassword"
     }
     ```

2. **Login User**

   - Endpoint: `POST /auth/login`
   - Request Body:
     ```json
     {
       "username": "testuser",
       "password": "securepassword"
     }
     ```
   - Response:
     ```json
     {
       "access_token": "your-access-token",
       "token_type": "bearer"
     }
     ```

### **Implementation**

- Password hashing with bcrypt using Passlib.
- Token generation using PyJWT.

---

## **Task Management**

### **Endpoints**

1. **Create Task**

   - Endpoint: `POST /tasks/`
   - Authorization: Bearer Token
   - Request Body:
     ```json
     {
       "title": "Finish project",
       "description": "Complete the backend for task manager",
       "due_date": "2024-12-31T23:59:59",
       "priority": 1,
       "category": "Work"
     }
     ```

2. **Get Tasks with Filters**

   - Endpoint: `GET /tasks/`
   - Authorization: Bearer Token
   - Query Parameters:
     - `category`: Filter by category
     - `priority`: Filter by priority
     - `due_date`: Filter by due date

3. **Update Task**

   - Endpoint: `PUT /tasks/{task_id}`
   - Authorization: Bearer Token
   - Request Body:
     ```json
     {
       "title": "Updated title",
       "description": "Updated description"
     }
     ```

4. **Delete Task**

   - Endpoint: `DELETE /tasks/{task_id}`
   - Authorization: Bearer Token

---

## **Technologies Used**

1. **Backend Framework**: FastAPI
2. **Database**: PostgreSQL
3. **ORM**: SQLAlchemy (asynchronous support)
4. **Authentication**: JWT
5. **Password Hashing**: bcrypt (Passlib)

---

## **Setup and Execution**

### **Prerequisites**

- Python 3.13.0
- PostgreSQL

### **Steps to Run the Project**

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update `DATABASE_URL` in `database.py` with your PostgreSQL credentials.
4. Run the application:
   ```bash
   u
   ```
5. uvicorn main\:app --reloadAccess the application at `http://localhost:8000`.

---

## **Future Enhancements**

1. Add user roles (admin, standard user).
2. Implement task reminders.
3. Add support for file attachments in tasks.
4. Enhance filtering with complex queries.
5. Deploy the application to a cloud platform.

---

## **Conclusion**

The Task Management System provides a robust foundation for managing tasks with user authentication and authorization. Its modular architecture ensures scalability and maintainability, making it a valuable project for task management use cases.

