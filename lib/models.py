#!usr/bin/ env python3
from datetime import datetime
from sqlalchemy import create_engine,Column,Integer,String,Float,DateTime,Table,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from prettytable import PrettyTable

Base = declarative_base()

class_staff = Table(
    "class_staff",
    Base.metadata,
    Column('class_id', Integer(), ForeignKey('class.id')),
    Column("staff_id", Integer(), ForeignKey("staff.id")),
    extend_existing=True
)

class Student(Base):
    __tablename__ = 'student_detail'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    email = Column(String(), unique=True)
    phone_number = Column(Integer())
    class_id = Column(Integer, ForeignKey('class.id'))
    class_data = relationship("Class", back_populates="students")
    staff_id = Column(Integer, ForeignKey('staff.id'))
    staff = relationship("Staff", back_populates="students")
    enrolled_on = Column(DateTime,default=datetime.now())

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String())
    students = relationship("Student", back_populates="class_data")
    staffs = relationship("Staff", secondary=class_staff, back_populates="classes")

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    role = Column(String())
    contact = Column(Integer())
    classes = relationship('Class', secondary=class_staff, back_populates="staffs")
    students = relationship('Student', back_populates="staff")


if __name__ == "__main__":
    engine = create_engine('sqlite:///school.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session =Session()
    #menu items
    menu = '''
========================================================
    SCHOOL RECORDS MANAGEMENT SYSTEM
========================================================

    1: CREATE STUDENT RECORD                          
    2: VIEW STUDENT RECORDS
    3: UPDATE STUDENT RECORDS
    4: DELETE STUDENT RECORDS
    5: ADD NEW CLASS
    6: VIEW CLASSES
    7: ADD STAFF
    8: VIEW STAFF
    9: EXIT
========================================================
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
        new_student.class_id = input('Enter CLASS ID: ')
        new_student.staff_id = input('Enter STAFF ID: ')
        new_student.enrolled_on = datetime.now()

        class_exists= session.query(Class).filter_by(id = new_student.class_id).first()
        staff_exists= session.query(Staff).filter_by(id = new_student.staff_id).first()

        if staff_exists and class_exists:
            session.add(new_student)
            session.commit()
            print('Student details saved successfully')   
        else:
            print('Invalid CLASS ID or STAFF ID entered')

    elif user_choice == "2":
        # View student records
        students = session.query(Student).all()
        # Create a table object
        table = PrettyTable()
        table.field_names = ['ID','Enrolled_On', 'First Name', 'Last Name', 'Gender', 'Email', 'Phone Number','Class ID','Staff Id']
       
        for student in students:
            date_object = student.enrolled_on
            date_string = date_object.strftime('%Y-%m-%d')
            table.add_row([student.id,date_string, student.first_name, student.last_name, student.gender, student.email, student.phone_number,student.class_id,student.staff_id])
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
            student.class_id = input('Enter CLASS ID: ')
            student.staff_id = input('Enter STAFF ID: ')
            student.enrolled_on = datetime.now()

            class_exists= session.query(Class).filter_by(id = student.class_id).first()
            staff_exists= session.query(Staff).filter_by(id = student.staff_id).first()
            if class_exists and staff_exists:
                print('Invalid CLASS ID or STAFF ID entered')
            else:
                session.commit()
                print(f'Student with ID {student_id} enrolled successfully')

            
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
        # Add new class
        print("------------------------------------------------")
        new_class = Class()
        new_class.name = input('Enter class name: ')
        new_class.course = input('Enter Course Name: ')

        name_exists = session.query(Class).filter_by(name = new_class.name).first()
        if name_exists:
            print("Class Aleady exists")
            
        else:
            session.add(new_class)
            session.commit()
            print("Class Added Successfully")
    elif user_choice == "6":
        #view class
        class_data = session.query(Class).all()
        table = PrettyTable()
        table.field_names = ["CLASS ID" , "CLASS NAME","COURSE"]
        for class_instance in class_data:
            table.add_row([class_instance.id,class_instance.name,class_instance.course])
       
        print(table)
    elif user_choice == "7":
       #add staff
       staff_record = Staff()
       staff_record.name = input("ENTER Name: ")
       staff_record.role = input('Enter Role: ')
       staff_record.contact = input('Enter Phone Number: ')

       session.add(staff_record)
       session.commit()

    elif user_choice == "8":
        #view staff
        staff_data = session.query(Staff).all()
        table = PrettyTable()
        table.field_names = [" STAFF ID" , "NAME", "ROLE"," PHONE NUMBER"]

        for staff in staff_data:
            table.add_row([staff.id,staff.name,staff.role,staff.contact])
        print(table)
    elif user_choice == "9":
        #exiting the program
        print('Exiting the program...')
        break
    else:
        print('Invalid choice. Please try again.')



        


    

 



    




    