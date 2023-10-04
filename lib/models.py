#!usr/bin/ env python3
from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.orm import declarative_base,sessionmaker
from prettytable import PrettyTable

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student_detail'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    email = Column(String(),unique=True)
    phone_number= Column(Integer())

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    
if __name__ == "__main__":
    engine = create_engine('sqlite:///school.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session =Session()

    print("---------SCHOOL RECORDS MANAGEMENT SYSTEM---------")
    menu = '''
1: CREATE STUDENT RECORD
2: VIEW STUDENT RECORDS
3: UPDATE STUDENT RECORDS
4: DELETE STUDENT RECORDS
5: ADD NEW COURSE
6: VIEW COURSES
7: UPDATE COURSE
8: DELETE COURSE
9: EXIT
'''

# Define the menu loop
while True:
    print(menu)
    user_choice = input('ENTER YOUR CHOICE: ')

    if user_choice == "1":
        # Enroll new student
        new_student = Student()
        new_student.first_name = input('Enter First Name: ')
        new_student.last_name = input('Enter Last Name: ')
        new_student.gender = input('Enter Gender: ')
        new_student.email = input('Enter Email: ')
        new_student.phone_number = input('Enter Phone Number: ')
        session.add(new_student)
        session.commit()
        print('Student details saved successfully')
    elif user_choice == "2":
        # View student records
        students = session.query(Student).all()
        # Create a table object
        table = PrettyTable()
        table.field_names = ['ID', 'First Name', 'Last Name', 'Gender', 'Email', 'Phone Number']
        for student in students:
            table.add_row([student.id, student.first_name, student.last_name, student.gender, student.email, student.phone_number])
        print(table)
    elif user_choice == "3":
        # Update student records
        print("-----------------------------------------------------")
        student_id = input('Enter the ID of the student to update: ')
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            student.first_name = input('Enter first name: ')
            student.last_name = input('Enter last name: ')
            student.gender = input('Enter Gender: ')
            student.email = input('Enter Email: ')
            student.phone_number = input('Enter Phone Number: ')
            session.commit()
            print(f'Student with ID {student_id} updated successfully')
    elif user_choice == "4":
        # Delete student records
        print("------------------------------------------------")
        student_id = input('Enter the ID of the student to delete: ')
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            #delete the student record
            session.delete(student)
            session.commit()
            print(f'Student with ID {student_id} deleted successfully')
        else:
            print(f'Student with ID {student_id} not found')
    elif user_choice == "5":
        # Add new course
        print("------------------------------------------------")
        new_course = Course(name=input('Enter New Course: '))
        session.add(new_course)
        session.commit()
        print('Course added successfully')
    elif user_choice == "6":
        #view courses
        course_data = session.query(Course).all()
        table = PrettyTable()
        table.field_names = ["COURSE ID" , "COURSE NAME"]
        for course in course_data:
            table.add_row([course.id,course.name])
       
        print(table)
    elif user_choice == "7":
        #Update Course
        print("------------------------------------------------")
        course_id = input('Enter the ID of the course to update: ')
        course = session.query(Course).filter_by(id=course_id).first()
        if course:
            course.name = input('Enter the new name of the course: ')
            session.commit()
            print(f'Course with ID {course_id} updated successfully')

    elif user_choice == "8":
        #delete course
        print("------------------------------------------------")
        course_id = input('Enter the ID of the course to delete: ')
        course = session.query(Course).filter_by(id=course_id).first()
        if course:
            # Delete the course
            session.delete(course)
            session.commit()
            print(f'Course with ID {course_id} deleted successfully')
        else:
            print(f'Course with ID {course_id} not found')
    elif user_choice == "9":
        #exiting the program
        print('Exiting the program...')
        break
    else:
        print('Invalid choice. Please try again.')



        


    

 



    




    