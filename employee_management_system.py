#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from customtkinter import*
from PIL import Image


root=CTk()
root.geometry("740x430")
root.resizable(0,0)
root.title("login page")
image=CTkImage(Image.open('cover.jpg.jpeg'),size=(740,478))


root.mainloop()


# In[ ]:


pip install pillow


# In[ ]:


import tkinter as tk
from tkinter import ttk, messagebox
import uuid

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1250x600")
        self.root.config(bg="#f4f4f9")

        # Employee Data
        self.employees = []

        # GUI Setup
        self.setup_ui()

    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Employee Management System", font=("Helvetica", 24), bg="#344955",
                         fg="#f9aa33")
        title.pack(pady=20)

        # Frame for Form
        form_frame = tk.Frame(self.root, bg="#f4f4f9")
        form_frame.pack(pady=20)

        # Labels and Entries for Employee Data
        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.dept_var = tk.StringVar()
        self.salary_var = tk.StringVar()  # Changed to StringVar for validation
        self.email_var = tk.StringVar()
        self.position_var = tk.StringVar()

        tk.Label(form_frame, text="Name:", bg="#f4f4f9").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.name_var, width=25).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Age:", bg="#f4f4f9").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.age_var, width=25).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Department:", bg="#f4f4f9").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.dept_var, width=25).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Salary:", bg="#f4f4f9").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.salary_var, width=25).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Email:", bg="#f4f4f9").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.email_var, width=25).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Position:", bg="#f4f4f9").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(form_frame, textvariable=self.position_var, width=25).grid(row=5, column=1, padx=10, pady=5)

        # Buttons for CRUD Operations
        tk.Button(form_frame, text="Add Employee", command=self.add_employee, bg="#344955", fg="#ffffff").grid(row=6,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10)
        tk.Button(form_frame, text="Update Employee", command=self.update_employee, bg="#344955", fg="#ffffff").grid(
            row=6, column=1, padx=10, pady=10)
        tk.Button(form_frame, text="Delete Employee", command=self.delete_employee, bg="#344955", fg="#ffffff").grid(
            row=6, column=2, padx=10, pady=10)

        # Treeview for Displaying Employees
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Department", "Salary", "Email", "Position"),
                                 show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Salary", text="Salary")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Position", text="Position")
        self.tree.column("ID", width=0, stretch=tk.NO)  # Hide the ID column
        self.tree.pack(pady=20)

        self.tree.bind("<ButtonRelease-1>", self.select_employee)

    def add_employee(self):
        name = self.name_var.get()
        age = self.age_var.get()
        dept = self.dept_var.get()
        salary = self.salary_var.get()
        email = self.email_var.get()
        position = self.position_var.get()

        if name and age and dept and self.validate_salary(salary) and email and position:
            emp_id = str(uuid.uuid4())
            self.employees.append({
                "ID": emp_id,
                "Name": name,
                "Age": age,
                "Department": dept,
                "Salary": float(salary),
                "Email": email,
                "Position": position
            })
            self.update_treeview()
            self.clear_form()
        else:
            messagebox.showwarning("Input Error", "All fields are required and must be valid")

    def update_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            values = self.tree.item(selected_item, "values")
            name = self.name_var.get()
            age = self.age_var.get()
            dept = self.dept_var.get()
            salary = self.salary_var.get()
            email = self.email_var.get()
            position = self.position_var.get()

            if name and age and dept and self.validate_salary(salary) and email and position:
                for employee in self.employees:
                    if employee["ID"] == values[0]:
                        employee["Name"] = name
                        employee["Age"] = age
                        employee["Department"] = dept
                        employee["Salary"] = float(salary)
                        employee["Email"] = email
                        employee["Position"] = position
                self.update_treeview()
                self.clear_form()
            else:
                messagebox.showwarning("Input Error", "All fields are required and must be valid")
        else:
            messagebox.showwarning("Selection Error", "No employee selected")

    def delete_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            values = self.tree.item(selected_item, "values")
            self.employees = [emp for emp in self.employees if emp["ID"] != values[0]]
            self.update_treeview()
            self.clear_form()
        else:
            messagebox.showwarning("Selection Error", "No employee selected")

    def select_employee(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            values = self.tree.item(selected_item, "values")
            self.name_var.set(values[1])
            self.age_var.set(values[2])
            self.dept_var.set(values[3])
            self.salary_var.set(values[4])
            self.email_var.set(values[5])
            self.position_var.set(values[6])

    def update_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for emp in self.employees:
            self.tree.insert("", "end", values=(
            emp["ID"], emp["Name"], emp["Age"], emp["Department"], emp["Salary"], emp["Email"], emp["Position"]))

    def clear_form(self):
        self.name_var.set("")
        self.age_var.set(0)
        self.dept_var.set("")
        self.salary_var.set("")
        self.email_var.set("")
        self.position_var.set("")

    def validate_salary(self, salary):
        try:
            float(salary)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    app = EmployeeManagementSystem(root)
    root.mainloop()


# In[ ]:




