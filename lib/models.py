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
    duration = Column(Float())
