""" 3. Classroom Performance Tracker
Scenario:A teacher wants to track student performance. Write a program to calculate the **average marks** of students and identify the **top performer**.
Requirements:
- Use a function to calculate the average marks.
- Identify the student with the highest average.
- Optional: Implement a `Student` class to handle this logic.
Input Example:
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
Expected Output:
Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}
Top Performer: "Alice"
"""
def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def find_top_performer(students):
    averages = {student: calculate_average(marks) for student, marks in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, top_performer = find_top_performer(students)

print(f"Average Marks: {averages}")
print(f"Top Performer: {top_performer}")
