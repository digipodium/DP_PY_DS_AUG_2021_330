from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from student_database import Student, Base, StudentGrades

Session = sessionmaker(bind=create_engine('sqlite:///student.db'))

# database menu for user
def database_menu():
    print("""
    1. Add a student
    2. View all students
    3. View a student's grades
    4. Update a student's grades
    5. Delete a student
    6. Exit
    """)
    choice = input("Enter your choice: ")
    return choice

