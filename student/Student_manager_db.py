import sqlite3

conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    brach TEXT NOT NULL,
    roll_number TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

def list_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("The Database is Empty.")
        return
    else:
        for row in rows:
            print("-" * 30)
            print(f" ID: {row[0]}\n Name: {row[1]}\n Branch: {row[2]}\n Roll Number: {row[3]}\n Phone: {row[4]}\n Email: {row[5]}")
        print("-" * 30)
        
def add_student():
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    brach = input("Enter student branch: ")
    roll_number = input("Enter student roll number: ")
    phone_number = input("Enter student phone number: ")
    email = input("Enter student email: ")

    cursor.execute("INSERT INTO students (id, name, brach, roll_number, phone_number, email) VALUES (?, ?, ?, ?, ?, ?)", (id, name, brach, roll_number, phone_number, email))
    conn.commit()
    print(f"Student '{name}' added successfully.")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter student's new name: ")
    brach = input("Enter student's new branch: ")
    roll_number = input("Enter student's new roll number: ")
    phone_number = input("Enter student's new phone number: ")
    email = input("Enter student's new email: ")

    cursor.execute("UPDATE students SET name = ?, brach = ?, roll_number = ?, phone_number = ?, email = ? WHERE id = ?", (name, brach, roll_number, phone_number, email, student_id))
    conn.commit()
    print(f"Student ID {student_id} updated successfully.")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student ID {student_id} deleted successfully.")

def main():
    while True:
        print("\nStudent manager app with DB")
        print("1. List students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")

    conn.close()

if __name__ == "__main__":
    main()
