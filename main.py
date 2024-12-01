import sqlite3
import os

# Create an SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a database table for students with student_number as the primary key
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_number TEXT PRIMARY KEY,
                    name TEXT,
                    contact TEXT,
                    ssn TEXT,
                    image_path TEXT
                )''')

# Create a database table for grades
cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id TEXT,
                    course TEXT,
                    grade TEXT,
                    FOREIGN KEY (student_id) REFERENCES students (student_number)
                )''')

# Create a database table for users and passwords
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT
                )''')

# Add a default username and password (note that this is just an example)
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "password"))
conn.commit()

# Create a directory for storing images
if not os.path.exists("images"):
    os.mkdir("images")

# Function for login
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            print("Login successful.")
            break
        else:
            print("Incorrect username or password. Please try again.")

# Function to add a student
def add_student():
    student_number = input("Enter student number: ")
    name = input("Enter student name: ")
    contact = input("Enter student contact information: ")
    ssn = input("Enter student SSN: ")
    
    image_path = input("Enter the image file name (e.g., student_card.png, press Enter to skip): ")
    if image_path:
        image_path = os.path.join("images", image_path)
        if not os.path.exists(image_path):
            print("Image file not found. Student added without an image.")
            image_path = None
    
    cursor.execute("INSERT INTO students (student_number, name, contact, ssn, image_path) VALUES (?, ?, ?, ?, ?)",
               (student_number, name, contact, ssn, image_path))
    conn.commit()
    print("Student added to the database.")

# Function to add grades for a student
def add_grades():
    student_number = input("Enter the student number of the student to add grades for: ")
    course = input("Enter course name: ")
    grade = input("Enter the grade: ")
    
    cursor.execute("SELECT student_number FROM students WHERE student_number = ?", (student_number,))
    student_id = cursor.fetchone()
    
    if student_id:
        cursor.execute("INSERT INTO grades (student_id, course, grade) VALUES (?, ?, ?)",
                       (student_number, course, grade))
        conn.commit()
        print("Grade added successfully.")
    else:
        print("Student not found.")

# Function to search for a student by student number
def search_student():
    student_number = input("Enter the student number of the student to search for: ")
    
    cursor.execute("SELECT * FROM students WHERE student_number = ?", (student_number,))
    student = cursor.fetchone()
    
    if student:
        print("Student found:")
        print(f"Student Number: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Contact: {student[2]}")
        print(f"SSN: {student[3]}")
        print(f"Image Path: {student[4]}")
    else:
        print("Student not found.")

# Function to display all students
def display_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if students:
        print("All students:")
        for student in students:
            print(f"Student Number: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Contact: {student[2]}")
            print(f"SSN: {student[3]}")
            print(f"Image Path: {student[4]}")
            print()
    else:
        print("No students in the database.")

# Function to upload an image
def upload_image():
    student_number = input("Enter the student number (image will be associated with this student): ")
    image_file = input("Enter the image file name (e.g., student_card.png): ")
    
    image_path = os.path.join("images", image_file)
    
    if os.path.exists(image_path):
        cursor.execute("UPDATE students SET image_path = ? WHERE student_number = ?", (image_path, student_number))
        conn.commit()
        print("Image uploaded and associated with the student.")
    else:
        print("Image file not found.")

# Function to download a student's image
def download_student_image():
    student_number = input("Enter the student number of the student whose image you want to download: ")
    
    cursor.execute("SELECT image_path FROM students WHERE student_number = ?", (student_number,))
    image_path = cursor.fetchone()
    
    if image_path:
        image_path = image_path[0]
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                image_data = f.read()
            new_image_name = input("Enter a new file name for the image (e.g., downloaded_image.png): ")
            with open(new_image_name, "wb") as f:
                f.write(image_data)
            print(f"Image downloaded as '{new_image_name}'.")
        else:
            print("Image not found on the server.")
    else:
        print("Student not found.")

# Main method
def main():
    login()  # Login
    while True:
        print("\nSelect an action:")
        print("1. Add a student")
        print("2. Add grades for a student")
        print("3. Search for a student by student number")
        print("4. Display all students")
        print("5. Upload an image for a student")
        print("6. Download a student's image")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            upload_image()
        elif choice == "6":
            download_student_image()
        elif choice == "7":
            break

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
