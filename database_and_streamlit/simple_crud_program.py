from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from student_database import Student, StudentGrades
import os
Session = sessionmaker(bind=create_engine('sqlite:///student.db'))

# database menu for user
def database_menu():
    os.system('cls') # clears previous output
    print("""
    1. Add a student
    2. View all students
    3. Add a student's grades
    4. View a student's grades
    5. Update a student's grades
    6. Delete a student
    7. Exit
    """)
    choice = input("Enter your choice: ")
    return choice

def add_student():
    global Session  # make a outer variable accessible inside a function

    print("ENTER DETAIL OF STUDENT")
    name = input("👨‍🎓 name:")
    fname = input("👨‍🎓 father's name:")
    mname = input("👨‍🎓 mother's name:")
    rollno = input("👨‍🎓 roll num:")
    klass = input("👨‍🎓 class:")
    section = input("👨‍🎓 section:")

    if name and fname and mname and rollno and klass and section:
        std = Student(name=name, father_name=fname, 
                      mother_name=mname,roll_no =rollno,
                      klass = klass, section=section)           # 1. create object
        db = Session()                                          # 2. open database
        db.add(std)                                             # 3. add object to db
        db.commit()                                             # 4. save database
        db.close()                                              # 5. close database
        print('👨‍🎓 Student added successfully ✔')
    else:
        print('invalid details')
        print('name:',name)
        print('father:',fname)
        print('mother:',mname)
        print('rollno:',rollno)
        print('class and section:',klass,section)

def view_all_students():
    global Session
    db = Session()
    results = db.query(Student).all()
    for std  in results:
        print(std.roll_no,std.name)
    input('press enter to continue ☑')

def delete_student():
    global Session
    roll_num = input("👨‍🎓students roll no:")
    if roll_num:
        db = Session()
        student = db.query(Student).filter(Student.roll_no.like(roll_num))
        db.delete(student[0]) # the first result
        db.commit()
        db.close()
        print("👨‍🎓STUDENT REMOVED FROM DATABASE")
    else:
        print('invalid value passed as roll no')
    input('press enter to continue')

# main loop
while True:
    ch = database_menu()
    if ch == '1':
        add_student()
    elif ch == '2':
        view_all_students()
    elif ch == '3':
        add_student_grades()
    elif ch == '4':
        view_student_grades()
    elif ch == '5':
        update_student_grades()
    elif ch == '6':
        delete_student()
    elif ch == '7':
        print('closing program.🏃‍♂️🚶‍♂️🏃‍♂️')
        break
    else:
        print('wrong choice')