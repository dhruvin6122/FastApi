# ✅ Task Manager API

A simple and efficient **Task Manager REST API** built with **FastAPI**.  
It allows users to create, read, update, and delete tasks with a clean, modern API design.  
The project uses **in-memory data storage** (Python list) for simplicity and demonstration purposes.

---

## ⚙️ Tech Stack

- **Framework:** FastAPI  
- **Language:** Python 3.10+  
- **Server:** Uvicorn  
- **Data Model & Validation:** Pydantic  
- **ID Generation:** UUID  
- **Datetime Handling:** Python `datetime` module  

---

## 🧱 Features

- Full **CRUD (Create, Read, Update, Delete)** functionality  
- **Partial updates (PATCH)** supported  
- Input validation and type checking with **Pydantic**  
- **Structured JSON responses**  
- **Error handling** using FastAPI’s `HTTPException`  
- **Interactive API documentation** via Swagger UI (`/docs`) and ReDoc (`/redoc`)  

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/tasks/` | Create a new task |
| `GET` | `/tasks/` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Retrieve a specific task by ID |
| `PUT` | `/tasks/{id}` | Update/replace an existing task |
| `PATCH` | `/tasks/{id}` | Partially update an existing task |
| `DELETE` | `/tasks/{id}` | Delete a task by ID |

---

## 📦 Example Request & Response

### ➕ **Create Task**
**POST /tasks/**
```json
{
  "title": "Learn FastAPI",
  "description": "Build a CRUD Task Manager API",
  "completed": false
}
