# School_Records_Management_System
The School Records Management System is a Python application that allows users to manage school records. The application uses SQLAlchemy to interact with a SQLite database, which allows users to store data in a single file without the need for a database server. Here are some additional details about the application:

    The application includes a menu with options to create, view, update, or delete student records, add or view classes, and add or view staff members.
    The application uses a while True loop to continuously display the menu and prompt the user for input.
    To create a new student record, the user must enter the student's details, including first name, last name, gender, email, phone number, class ID, and staff ID.
    To view student records, the application displays a table of all student records, including the student's ID, enrollment date, first name, last name, gender, email, phone number, class ID, and staff ID.
    To update a student record, the user must enter the ID of the student to update and the updated details.
    To delete a student record, the user must enter the ID of the student to delete.
    To add a new class, the user must enter the class name and course. If the class name already exists in the database, the application displays an error message.
    To view all classes, the application displays a table of all classes, including the class ID, class name, and course.
    To add a new staff member, the user must enter the staff member's name, role, and phone number.
    To view all staff members, the application displays a table of all staff members, including the staff ID, name, role, and phone number.

The School Records Management System is a useful tool for managing school records and can be easily customized to fit the needs of any educational institution.
# INSTALLATION
1. Clone the repository: [REPOSITORY LINK](https://github.com/jankimutai/School_Records_Management_System)
2. Install the required dependencies:
``` 
   $ pipenv install
```
# Usage
To run the application, navigate to the project directory and run the following command: 
``` 
   $ python3 lib/models.py
```
This will start the application and display the main menu:

```
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
```

Use the menu options to create, view, update, or delete student records, add or view classes, and add or view staff members.
The application uses a while True loop to continuously display the menu and prompt the user for input. Here's how to use the menu options:
  1. To create a new student record, enter 1 and follow the prompts to enter the student's details.
  2. To view student records, enter 2 and a table of all student records will be displayed.
  3. To update a student record, enter 3 and follow the prompts to enter the ID of the student to update the updated details.
  4. To delete a student record, enter 4 and follow the prompts to enter the ID of the student to delete.
  5. To add a new class, enter 5 and follow the prompts to enter the class details.
  6. To view all classes, enter 6 and a table of all classes will be displayed.
  7. To add a new staff member, enter 7 and follow the prompts to enter the staff member's details.
  8. To view all staff members, enter 8 and a table of all staff members will be displayed.
  9. To exit the application, enter 9.

# License
This project is licensed under the MIT License 
