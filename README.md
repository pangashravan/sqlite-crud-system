# SQLite CRUD Management System

A Python CLI application demonstrating core database engineering concepts — schema design, full CRUD operations, parameterised queries, exception handling, and OOP-based architecture.

## Features

- Full CRUD: Create, Read, Update, Delete student records
- Parameterised SQL queries (prevents SQL injection)
- Input validation with descriptive error messages
- Summary statistics (total, average age, course distribution)
- OOP design: separate Database, Student, and main layers
- Automatic sample data seeding on first run

## Tech Stack

- Python 3.x
- SQLite (built-in — no installation needed)
- Python DB-API (sqlite3)
- OOP / Modular Architecture

## Setup & Run

```bash
# Clone the repo
git clone https://github.com/pangashravan/sqlite-crud-system.git
cd sqlite-crud-system

# Run directly — no dependencies needed
python3 main.py
```

## Menu Options

```
1. Add New Student
2. View All Students
3. Search Student by ID
4. Search Students by Course
5. Update Student Details
6. Delete Student
7. View Summary Statistics
0. Exit
```

## Project Structure

```
sqlite-crud-system/
├── main.py         # CLI menu and app entry point
├── database.py     # Database class — all SQLite operations
├── student.py      # Student model with validation
└── README.md
```

## Key Concepts Demonstrated

- `CREATE TABLE` with constraints (NOT NULL, UNIQUE, CHECK)
- `INSERT`, `SELECT`, `UPDATE`, `DELETE` with parameterised queries
- Aggregate queries: `COUNT`, `AVG`, `MIN`, `MAX`, `GROUP BY`
- Exception handling for `IntegrityError` and `sqlite3.Error`
- OOP: class-based database layer with clean method separation

## Author

**Panga Shravan Yadav** — Python Developer | Backend Engineer  
[LinkedIn](https://www.linkedin.com/in/pangashravan) | [GitHub](https://github.com/pangashravan)
