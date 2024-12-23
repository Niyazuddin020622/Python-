class Student:
    def __init__(self, name, roll_no, marks):
       
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
       
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Niyazu", 101, 89)
student2 = Student("Rani", 102, 95)

# Display the details of the students
student1.display_details()
print("-" * 20)  # Separator for clarity
student2.display_details()
