# Simple-Task-Manager
Internship Entrance Challenge: Simple Task Manager; for Kuraz Tech
# 🧠 Task Manager API (FastAPI)

A simple RESTful API for managing tasks using **FastAPI** and **JSON file storage**.


## API Endpoints

- `GET /api/tasks` – Get all tasks
- `POST /api/tasks` – Add a new task
- `PUT /api/tasks/{id}` – Mark a task as completed
- `DELETE /api/tasks/{id}` – Delete a task
- `GET /` – "API is running" confirmation route

## 🧰 Tech Stack

- **Python 3.11**
- **FastAPI** – Web framework
- **Uvicorn** – ASGI server
- **JSON** – Lightweight local data store

---

## 📁 Project Structure
``` bash
Backend/
├── main.py # Main FastAPI app
├── tasks.json # Stores task data
└── requirements.txt # Dependencie
```


## Installation

1. **Clone the repo**:

```bash
git clone https://github.com/Zahir-Seid/Simple-Task-Manager
cd Simple-Task-Manager
cd Backend
```

2. **Create a virtual environment (optional but recommended) and install dependencies**:

```bash
python -m venv .venv
source .venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

```

3. **Run it**

```bash
uvicorn main:app --reload
```

## License

MIT License