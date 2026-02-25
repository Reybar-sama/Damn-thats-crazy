import tkinter as tk
from tkinter import messagebox, filedialog

def save_to_file():
    """Appends student data to a local text file."""
    s_id = entry_id.get()
    f_name = entry_first.get()
    l_name = entry_last.get()
    course = entry_course.get()
    phone = entry_phone.get()

    if not (s_id and f_name and l_name and course and phone):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    record = f"ID: {s_id} | Name: {f_name} {l_name} | Course: {course} | Phone: {phone}\n"
    
    try:
        with open("students_list.txt", "a") as file:
            file.write(record)
        messagebox.showinfo("Success", "Student data saved successfully!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")

def export_as_txt():
    """Allows user to choose a location to save the full list."""
    try:
        with open("students_list.txt", "r") as file:
            content = file.read()
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as export_file:
                export_file.write(content)
            messagebox.showinfo("Exported", "Student list exported successfully!")
    except FileNotFoundError:
        messagebox.showwarning("No Data", "No student records found to export.")

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Root Window Setup
root = tk.Tk()
root.title("School Management System")
root.geometry("450x350")
root.config(padx=20, pady=20)

# UI Elements
labels = ["Student ID:", "First Name:", "Last Name:", "Course:", "Phone Number:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, pady=5, padx=10)
    entries.append(entry)

# Mapping entries for easy access
entry_id, entry_first, entry_last, entry_course, entry_phone = entries

# Buttons
btn_frame = tk.Frame(root)
btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

tk.Button(btn_frame, text="Add Student", command=save_to_file, bg="#4CAF50", fg="white", width=15).pack(side="left", padx=5)
tk.Button(btn_frame, text="Export List", command=export_as_txt, bg="#2196F3", fg="white", width=15).pack(side="left", padx=5)

root.mainloop()