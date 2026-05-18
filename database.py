"""
Database layer — handles all SQLite operations
Uses parameterised queries to prevent SQL injection
"""

import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    name    TEXT    NOT NULL,
                    age     INTEGER NOT NULL CHECK(age > 0 AND age < 120),
                    course  TEXT    NOT NULL,
                    email   TEXT    NOT NULL UNIQUE
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Table creation error: {e}")

    def seed_data(self):
        """Insert sample data only if table is empty"""
        self.cursor.execute("SELECT COUNT(*) FROM students")
        count = self.cursor.fetchone()[0]
        if count == 0:
            sample = [
                ("Shravan Yadav",   22, "B.Tech IT",           "shravan@example.com"),
                ("Priya Sharma",    21, "B.Tech CSE",          "priya@example.com"),
                ("Ravi Kumar",      23, "B.Tech ECE",          "ravi@example.com"),
                ("Anjali Singh",    22, "B.Tech IT",           "anjali@example.com"),
                ("Mohammed Arif",   24, "MCA",                 "arif@example.com"),
            ]
            self.cursor.executemany(
                "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
                sample
            )
            self.conn.commit()

    def insert_student(self, student):
        try:
            self.cursor.execute(
                "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
                (student.name, student.age, student.course, student.email)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Email '{student.email}' already exists.")
        except sqlite3.Error as e:
            print(f"Insert error: {e}")

    def get_all_students(self):
        try:
            self.cursor.execute("SELECT * FROM students ORDER BY id")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Query error: {e}")
            return []

    def get_student_by_id(self, student_id):
        try:
            self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Query error: {e}")
            return None

    def get_students_by_course(self, course):
        try:
            self.cursor.execute(
                "SELECT * FROM students WHERE LOWER(course) LIKE LOWER(?)",
                (f"%{course}%",)
            )
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Query error: {e}")
            return []

    def update_student(self, student_id, name, age, course):
        try:
            self.cursor.execute(
                "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
                (name, age, course, student_id)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Update error: {e}")

    def delete_student(self, student_id):
        try:
            self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Delete error: {e}")

    def get_stats(self):
        try:
            self.cursor.execute("""
                SELECT
                    COUNT(*) as total,
                    ROUND(AVG(age), 1) as avg_age,
                    MIN(age) as min_age,
                    MAX(age) as max_age
                FROM students
            """)
            row = self.cursor.fetchone()

            self.cursor.execute("""
                SELECT course, COUNT(*) as count
                FROM students
                GROUP BY course
                ORDER BY count DESC
            """)
            courses = {r[0]: r[1] for r in self.cursor.fetchall()}

            return {
                "total": row[0],
                "avg_age": row[1],
                "min_age": row[2],
                "max_age": row[3],
                "courses": courses
            }
        except sqlite3.Error as e:
            print(f"Stats error: {e}")
            return {}

    def close(self):
        if self.conn:
            self.conn.close()
