from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class StudentGrades(Base):
    __tablename__ = 'student_grades'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    english = Column(Integer)
    hindi = Column(Integer)
    maths = Column(Integer)
    added_on = Column(DateTime, default=datetime.now())


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    father_name = Column(String(25))
    mother_name = Column(String(25))
    roll_no = Column(String(25),unique=True)
    klass = Column(String(15))
    section = Column(String(5))

if __name__ == '__main__':
    engine = create_engine('sqlite:///student.db', echo=True)
    Base.metadata.create_all(engine)
