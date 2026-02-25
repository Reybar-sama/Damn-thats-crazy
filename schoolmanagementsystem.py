#name:triza mwaura
#date: 24/02/2026
#program to manage school system

import pandas as pd
import os

FILE_NAME = "students.xlsx"

# Initialize Excel file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["ID", "Name", "Course", "Contact"])
        df.to_excel(FILE_NAME, index=False)

# Load file safely
def load_data():
    return pd.read_excel(FILE_NAME, dtype={"ID": str, "Contact": str})

# Save file safely
def save_data(df):
    df.to_excel(FILE_NAME, index=False)

# Register new student
def register_student():
    df = load_data()

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    contact = input("Enter Contact: ").strip()

    if student_id in df["ID"].values:
        print("❌ Student ID already exists!")
        return

    new_row = {
        "ID": student_id,
        "Name": name,
        "Course": course,
        "Contact": contact
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)

    print("✅ Student registered successfully!")

# Display students
def display_students():
    df = load_data()

    if df.empty:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        print(df.to_string(index=False))

# Assign new course
def assign_course():
    df = load_data()

    student_id = input("Enter Student ID to update course: ").strip()

    if student_id not in df["ID"].values:
        print("❌ Student ID not found.")
        return

    new_course = input("Enter New Course: ").strip()
    df.loc[df["ID"] == student_id, "Course"] = new_course

    save_data(df)
    print("✅ Course updated successfully!")

# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== School Management System =====")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Assign New Course")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            assign_course()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()