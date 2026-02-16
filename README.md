# tkinter_student_management

# Student Management System

A simple desktop application built with Python and Tkinter for managing student records. This application provides a user-friendly interface to perform CRUD (Create, Read, Update, Delete) operations on student data stored in a SQLite database.

## Features

- **Add Student** - Add new student records with name, age, email, and grade
- **View All Students** - Display all students in a tabular format
- **Search Students** - Search for students by name or email
- **Update Student** - Modify existing student information using email as identifier
- **Delete Student** - Remove a student record using email as identifier
- **Input Validation** - Ensures all fields are filled and prevents duplicate email entries
- **Auto-refresh** - Table automatically updates after each operation

## Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- SQLite3 (comes pre-installed with Python)

No additional packages need to be installed as the application uses only Python's standard library.


git clone https://github.com/yourusername/student-management-system.git

Usage
Add a Student: Fill in all the fields (Name, Age, Email, Grade) and click "Add"

View All Students: Click "View all" to display all records

Search: Enter a name or email in either field and click "Search"

Update: Enter the student's email and modify the desired fields, then click "Update"

Delete: Enter the student's email and click "Delete"

Clear Fields: Fields are automatically cleared after Add, Update, and Delete operations

Application Interface
The interface consists of:

Input fields for student information (Name, Age, Email, Grade)

Control buttons for operations (Search, Add, Delete, View all, Update)

A table view displaying all student records

Error Handling
Shows warning if required fields are empty

Prevents duplicate email entries

Notifies if no matching records are found for search/update/delete operations
