# Q5: student_database() function
def student_database():
    students = {}
    
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                students.update({roll: {"name": name, "age": age, "city": city}})
                print("Student added successfully!")
                
            elif choice == 2:
                roll = input("Enter Roll Number to search: ")
                student = students.get(roll)
                if student:
                    print(f"Found: {student}")
                else:
                    print("Student not found!")
                    
            elif choice == 3:
                if students:
                    print("\nAll Students:")
                    for roll, data in students.items():
                        print(f"Roll {roll}: {data}")
                else:
                    print("Database is empty!")
                    
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Please enter valid number!")

student_database()