# Name : Rey Bar
# Date : 23/02/2026
# Program to record and display student details in Python & text doc


import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("900x500")

        # Data storage
        self.student_list = []

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        # --- Input Frame ---
        input_frame = tk.LabelFrame(self.root, text="Student Details", padx=10, pady=10)
        input_frame.pack(side="left", fill="y", padx=20, pady=20)

        fields = [("Student ID:", "id"), ("First Name:", "fname"), 
                  ("Last Name:", "lname"), ("Courses:", "course"), ("Phone:", "phone")]
        
        self.entries = {}
        for i, (label_text, key) in enumerate(fields):
            tk.Label(input_frame, text=label_text).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[key] = entry

        # Buttons
        tk.Button(input_frame, text="Add Student", command=self.add_student, bg="#4CAF50", fg="white").grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")
        tk.Button(input_frame, text="Export to Text", command=self.export_to_txt, bg="#2196F3", fg="white").grid(row=7, column=0, columnspan=2, pady=5, sticky="ew")
        tk.Button(input_frame, text="Clear Fields", command=self.clear_entries).grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")

        # --- Display Frame ---
        display_frame = tk.Frame(self.root)
        display_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Treeview for table display
        columns = ("ID", "First Name", "Last Name", "Courses", "Phone")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True)

    def add_student(self):
        # Gather data
        data = {k: v.get() for k, v in self.entries.items()}
        
        # Simple validation
        if not all(data.values()):
            messagebox.showwarning("Input Error", "Please fill in all fields!")
            return

        # Add to internal list and UI
        self.student_list.append(data)
        self.tree.insert("", "end", values=(data['id'], data['fname'], data['lname'], data['course'], data['phone']))
        
        self.clear_entries()
        messagebox.showinfo("Success", "Student added successfully!")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def export_to_txt(self):
        if not self.student_list:
            messagebox.showwarning("Export Error", "The student list is empty!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write(f"{'ID':<10} | {'First Name':<15} | {'Last Name':<15} | {'Course':<20} | {'Phone':<15}\n")
                    f.write("-" * 80 + "\n")
                    for s in self.student_list:
                        f.write(f"{s['id']:<10} | {s['fname']:<15} | {s['lname']:<15} | {s['course']:<20} | {s['phone']:<15}\n")
                
                messagebox.showinfo("Export Successful", f"Data saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()