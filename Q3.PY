# Q3: manage_marks() function
def manage_marks():
    marks_list = []
    print("Enter marks for 5 subjects:")
    
    # 5 subjects che marks ghe
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Subject {i+1} mark: "))
                marks_list.append(mark)
                break
            except ValueError:
                print("Invalid input! Please enter numeric value.")
    
    # Average, highest, lowest calculate kar
    average = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)
    
    print(f"\nMarks List: {marks_list}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    
    # Descending order madhe sort kar
    marks_list.sort(reverse=True)
    print(f"Sorted Marks (Descending): {marks_list}")

# Function call kar
manage_marks()