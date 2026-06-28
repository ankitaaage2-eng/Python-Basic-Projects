# Q8: Employee Class
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary) # Tuple
    
    def show_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.details[0]}, Salary: {self.details[1]}")

# Dictionary banav - key: emp_id, value: Employee object
employees = {}

# 3 employees add kar
employees["E101"] = Employee("E101", "Rahul", "IT", 50000)
employees["E102"] = Employee("E102", "Priya", "HR", 45000)
employees["E103"] = Employee("E103", "Amit", "Finance", 60000)

# Sagle display kar loop ne
print("--- All Employee Details ---")
for emp_id, emp_obj in employees.items():
    emp_obj.show_details()