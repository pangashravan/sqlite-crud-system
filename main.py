"""
SQLite CRUD Management System
A Python CLI app demonstrating database fundamentals:
- Schema design & table creation
- Full CRUD operations
- Parameterised queries (SQL injection prevention)
- Exception handling
- OOP-based design
"""

from database import Database
from student import Student


def print_menu():
    print("\n" + "="*45)
    print("   Student Record Management System")
    print("="*45)
    print("  1. Add New Student")
    print("  2. View All Students")
    print("  3. Search Student by ID")
    print("  4. Search Students by Course")
    print("  5. Update Student Details")
    print("  6. Delete Student")
    print("  7. View Summary Statistics")
    print("  0. Exit")
    print("="*45)


def main():
    db = Database("students.db")
    db.create_table()
    db.seed_data()  # Add sample data on first run

    print("Welcome to Student Record Management System")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\n--- Add New Student ---")
            name = input("Enter name: ").strip()
            age = input("Enter age: ").strip()
            course = input("Enter course: ").strip()
            email = input("Enter email: ").strip()

            student = Student(name, age, course, email)
            error = student.validate()
            if error:
                print(f"Error: {error}")
                continue

            db.insert_student(student)
            print(f"Student '{name}' added successfully!")

        elif choice == '2':
            print("\n--- All Students ---")
            students = db.get_all_students()
            if not students:
                print("No students found.")
            else:
                print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Course':<20} {'Email':<25}")
                print("-" * 75)
                for s in students:
                    print(f"{s[0]:<5} {s[1]:<20} {s[2]:<5} {s[3]:<20} {s[4]:<25}")
                print(f"\nTotal: {len(students)} student(s)")

        elif choice == '3':
            print("\n--- Search by ID ---")
            sid = input("Enter Student ID: ").strip()
            try:
                student = db.get_student_by_id(int(sid))
                if student:
                    print(f"\nID:     {student[0]}")
                    print(f"Name:   {student[1]}")
                    print(f"Age:    {student[2]}")
                    print(f"Course: {student[3]}")
                    print(f"Email:  {student[4]}")
                else:
                    print("Student not found.")
            except ValueError:
                print("Error: ID must be a number.")

        elif choice == '4':
            print("\n--- Search by Course ---")
            course = input("Enter course name: ").strip()
            students = db.get_students_by_course(course)
            if not students:
                print(f"No students found in course '{course}'.")
            else:
                print(f"\nStudents in '{course}':")
                for s in students:
                    print(f"  [{s[0]}] {s[1]} — {s[4]}")

        elif choice == '5':
            print("\n--- Update Student ---")
            sid = input("Enter Student ID to update: ").strip()
            try:
                student = db.get_student_by_id(int(sid))
                if not student:
                    print("Student not found.")
                    continue
                print(f"Current details: {student[1]}, Age {student[2]}, {student[3]}")
                name = input(f"New name (press Enter to keep '{student[1]}'): ").strip() or student[1]
                age = input(f"New age (press Enter to keep '{student[2]}'): ").strip() or student[2]
                course = input(f"New course (press Enter to keep '{student[3]}'): ").strip() or student[3]
                db.update_student(int(sid), name, age, course)
                print("Student updated successfully!")
            except ValueError:
                print("Error: ID must be a number.")

        elif choice == '6':
            print("\n--- Delete Student ---")
            sid = input("Enter Student ID to delete: ").strip()
            try:
                student = db.get_student_by_id(int(sid))
                if not student:
                    print("Student not found.")
                    continue
                confirm = input(f"Delete '{student[1]}'? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    db.delete_student(int(sid))
                    print("Student deleted successfully.")
                else:
                    print("Cancelled.")
            except ValueError:
                print("Error: ID must be a number.")

        elif choice == '7':
            print("\n--- Summary Statistics ---")
            stats = db.get_stats()
            print(f"Total Students:    {stats['total']}")
            print(f"Average Age:       {stats['avg_age']}")
            print(f"Youngest Student:  {stats['min_age']}")
            print(f"Oldest Student:    {stats['max_age']}")
            print(f"\nStudents per Course:")
            for course, count in stats['courses'].items():
                print(f"  {course:<25} {count} student(s)")

        elif choice == '0':
            print("\nGoodbye!")
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
