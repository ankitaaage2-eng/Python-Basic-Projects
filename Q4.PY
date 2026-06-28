# Q4: Student Class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if 0 <= mark <= 100:
                self.marks_list.append(mark)
                print(f"Mark {mark} added successfully")
            else:
                print("Invalid mark! Should be 0-100")
        except ValueError:
            print("Invalid input! Enter numeric value")
    
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    
    def display_info(self):
        print(f"\n--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks_list}")
        print(f"Average: {self.get_average():.2f}")

# User input gheun demo
name = input("Enter student name: ")
roll = input("Enter roll no: ")
s1 = Student(name, roll)

n = int(input("How many marks to add? "))
for i in range(n):
    mark = input(f"Enter mark {i+1}: ")
    s1.add_mark(mark)

s1.display_info()