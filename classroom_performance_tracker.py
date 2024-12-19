class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

def calculate_average_marks(students):
    averages = {}
    for name, marks in students.items():
        student = Student(name, marks)
        averages[name] = round(student.calculate_average(), 2)
    return averages

def identify_top_performer(averages):
    return max(averages, key=averages.get)

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

average_marks = calculate_average_marks(students)
print("Average Marks:", average_marks)
top_performer = identify_top_performer(average_marks)
print("Top Performer:", top_performer)
