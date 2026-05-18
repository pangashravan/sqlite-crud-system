"""Student model with validation"""


class Student:
    def __init__(self, name, age, course, email):
        self.name = name.strip()
        self.age = age
        self.course = course.strip()
        self.email = email.strip().lower()

    def validate(self):
        """Returns error string or None if valid"""
        if not self.name:
            return "Name cannot be empty"
        try:
            self.age = int(self.age)
            if self.age <= 0 or self.age > 120:
                return "Age must be between 1 and 120"
        except (ValueError, TypeError):
            return "Age must be a valid number"
        if not self.course:
            return "Course cannot be empty"
        if not self.email or '@' not in self.email:
            return "Email must be a valid email address"
        return None

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, course={self.course})"
