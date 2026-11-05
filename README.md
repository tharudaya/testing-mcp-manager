# Task Manager

A simple full-stack task manager. You can add, list, update and delete tasks.

- **Client:** React 19 + TypeScript + Vite + Tailwind CSS (`client/`)
- **Server:** FastAPI + SQLAlchemy + MySQL (`server/`)

## Project structure

```
task-manager/
├── client/              # React frontend
│   └── src/
│       ├── api/         # fetch helpers for the API
│       └── components/  # UI components
└── server/              # FastAPI backend
    ├── main.py          # API routes
    ├── models.py        # SQLAlchemy models
    ├── schemas.py       # Pydantic schemas
    └── database.py      # DB connection
```

## Prerequisites

- Node.js 20+
- Python 3.10+
- MySQL server

## Getting started

### 1. Database

Create the database in MySQL:

```sql
CREATE DATABASE task_manager_new;
```

Database credentials are read from `server/.env`, which is not committed to git. Copy the example file and fill in your own values:

```bash
cd server
cp .env.example .env
```

```
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=task_manager_new
```

The `tasks` table is created automatically when the server starts.

### 2. Server

```bash
cd server
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at http://127.0.0.1:8000. Interactive docs are at http://127.0.0.1:8000/docs.

### 3. Client

```bash
cd client
npm install
npm run dev
```

The app runs at http://localhost:5173.

## API endpoints

| Method | Endpoint           | Description       | Body                                   |
| ------ | ------------------ | ----------------- | -------------------------------------- |
| GET    | `/`                | Health check      | –                                      |
| GET    | `/tasks`           | List all tasks    | –                                      |
| POST   | `/tasks`           | Create a task     | `{ "text": "..." }`                    |
| PUT    | `/tasks/{task_id}` | Update a task     | `{ "text": "...", "completed": true }` |
| DELETE | `/tasks/{task_id}` | Delete a task     | –                                      |
