class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StudentEnrollment:
    def __init__(self, student_id, course_id, marks):
        self.student_id = student_id
        self.course_id = course_id
        self.marks = marks

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            id = int(input("Enter student id: "))
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.students.append(student)

    def add_course(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            id = int(input("Enter course id: "))
            name = input("Enter course name: ")
            course = Course(id, name)
            self.courses.append(course)

    def add_marks(self):
        course_id = int(input("Enter course id: "))
        for student in self.students:
            student_id = student.id
            marks = int(input(f"Enter marks for student id {student_id}: "))
            enrollment = StudentEnrollment(student_id, course_id, marks)
            self.enrollments.append(enrollment)

    def list_courses(self):
        for course in self.courses:
            print(f"Course id: {course.id}, Course name: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"Student id: {student.id}, Student name: {student.name}, Date of birth: {student.dob}")

    def show_marks(self):
        course_id = int(input("Enter course id: "))
        for enrollment in self.enrollments:
            if enrollment.course_id == course_id:
                print(f"Student id: {enrollment.student_id}, Marks: {enrollment.marks}")

school = School()
school.add_student()
school.add_course()
school.add_marks()
school.list_courses()
school.list_students()
school.show_marks()


