class Person :
    def __init__(self, name , age) :
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"



class Student(Person) :
    def __init__(self, name, age, student_id, grades=None): 
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades if grades is not None else {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Grades: {self.grades})"        

class Teacher(Person) :
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def __str__(self):
        return f"Teacher(Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Subject: {self.subject})"
    
class School :
    def __init__(self,students,teachers,subjects):
        self.students = students if students is not None else []
        self.teachers = teachers if teachers is not None else []
        self.subjects = set(subjects) if subjects is not None else set() 
    def add_student(self, student):
        self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers.append(teacher)  
    def __str__(self):
        students_str = str(self.students[:])
        teachers_str = [str(teacher) for teacher in self.teachers]
        return f"School(Students: {students_str}, Teachers: {teachers_str}, Subjects: {self.subjects})"      
    

school = School([],[],["Math","Science","History"])
student1 = Student("Alice", 20, "S001")
student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student1.add_grade("History", 88)
print(student1)
print(f"Alice's Average Grade: {student1.get_average_grade()}")
teacher1 = Teacher("Mr. Smith", 40, "T001", "Math")
print(teacher1)
school.add_student(student1)
school.add_teacher(teacher1)
print(school)






