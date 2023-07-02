from database.model import Student


def StudentDuplicates(name, email):
    existing_student = Student.objects(name=name, email=email).first()
    if existing_student:
        return f"Student with name '{name}' and email '{email}' already exists."
    return None
