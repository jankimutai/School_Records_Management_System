# School_Records_Management_System
This is a Python application for managing school records. It uses SQLAlchemy to interact with an SQLite database.

# INSTALLATION
1. Clone the repository:(REPO LINK)[https://github.com/jankimutai/School_Records_Management_System]
2. Install the required dependencies:
``` console
   $ pipenv install
```
# Usage
To run the application, navigate to the project directory and run the following command: 
``` console
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
