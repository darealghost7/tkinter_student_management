from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ===================== DATABASE SETUP =====================
# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the students table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE,
    grade TEXT
)
""")
conn.commit()


# ===================== FUNCTIONS =====================

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    grade = grade_entry.get()

    if name == "" or age == "" or email == "" or grade == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO students (name, age, email, grade) VALUES (?, ?, ?, ?)",
                       (name, age, email, grade))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        View_student()  # Refresh table
        clear_entries()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")


def View_student():
    # Clear the Treeview first
    for row in treedis.get_children():
        treedis.delete(row)

    cursor.execute("SELECT name, age, email, grade FROM students")
    rows = cursor.fetchall()
    for row in rows:
        treedis.insert("", "end", values=row)


def search_student():
    keyword = name_entry.get() or email_entry.get()

    for row in treedis.get_children():
        treedis.delete(row)

    cursor.execute("SELECT name, age, email, grade FROM students WHERE name LIKE ? OR email LIKE ?",
                   (f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            treedis.insert("", "end", values=row)
    else:
        messagebox.showinfo("Not Found", "No matching student found.")


def delete_student():
    email = email_entry.get()

    if email == "":
        messagebox.showwarning("Input Error", "Enter the email of the student to delete.")
        return

    cursor.execute("DELETE FROM students WHERE email=?", (email,))
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Student deleted successfully!")
        View_student()
        clear_entries()
    else:
        messagebox.showinfo("Not Found", "No student found with that email.")


def Update_student():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    grade = grade_entry.get()

    if email == "":
        messagebox.showwarning("Input Error", "Enter the email of the student to update.")
        return

    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE email=?",
                   (name, age, grade, email))
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Student updated successfully!")
        View_student()
        clear_entries()
    else:
        messagebox.showinfo("Not Found", "No student found with that email.")


def clear_entries():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    grade_entry.delete(0, END)


# ===================== GUI SETUP =====================
root = Tk()
root.title("Student Management System")
root.geometry("500x500")

name_label = Label(root, text="Enter your name")
name_entry = Entry(root)

age_label = Label(root, text="Enter your age")
age_entry = Entry(root)

email_label = Label(root, text="Enter your email")
email_entry = Entry(root)

grade_label = Label(root, text="Enter your grade")
grade_entry = Entry(root)

Search_Button = Button(root, text="Search", command=search_student)
Add_Button = Button(root, text="Add", command=add_student)
Delete_Button = Button(root, text="Delete", command=delete_student)
ViewAll_Button = Button(root, text="View all", command=View_student)
Update_Button = Button(root, text="Update", command=Update_student)

name_label.grid(row=0, column=0, pady=10)
name_entry.grid(row=0, column=1, pady=10)

age_label.grid(row=1, column=0, pady=10)
age_entry.grid(row=1, column=1, pady=10)

email_label.grid(row=2, column=0, pady=10)
email_entry.grid(row=2, column=1, pady=10)

grade_label.grid(row=3, column=0, pady=10)
grade_entry.grid(row=3, column=1, pady=10)

Search_Button.grid(row=4, column=0, padx=5, pady=10)
Add_Button.grid(row=4, column=1, padx=5, pady=10)
Delete_Button.grid(row=5, column=0, padx=5, pady=10)
ViewAll_Button.grid(row=5, column=1, padx=5, pady=10)
Update_Button.grid(row=6, column=0, columnspan=2, pady=10)

# ===================== TREEVIEW =====================
treedis = ttk.Treeview(
    root,
    columns=("Name", "Age", "E-mail", "Grade"),
    show='headings',
    height=8
)
treedis.grid(row=7, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

treedis.heading("Name", text="Name")
treedis.heading("Age", text="Age")
treedis.heading("E-mail", text="E-mail")
treedis.heading("Grade", text="Grade")

treedis.column("Name", width=120)
treedis.column("Age", width=50, anchor='center')
treedis.column("E-mail", width=180)
treedis.column("Grade", width=70, anchor='center')

# Load data initially
View_student()

root.mainloop()

# Close DB when done
conn.close()
