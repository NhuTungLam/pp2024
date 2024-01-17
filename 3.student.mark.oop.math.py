import math 
import numpy as np
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name, credit_numbers):
        self.id = id
        self.name = name
        self.credit_numbers = credit_numbers

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
            credit_numbers = int(input("Enter credit numbers for {}: ".format(name)))
            course = Course(id, name, credit_numbers)
            self.courses.append(course)

    def add_marks(self):
        course_id = int(input("Enter course id: "))
        for student in self.students:
            student_id = student.id
            raw_marks = float(input("Enter marks for student id {}: ".format(student_id)))
            # round down to 1 decimal place
            marks = math.floor(raw_marks*10)/10
            enrollment = StudentEnrollment(student_id, course_id, marks)
            self.enrollments.append(enrollment)

    def list_courses(self):
        for course in self.courses:
            print("Course id: {}, Course name: {}, Credit numbers: {}".format(course.id, course.name, course.credit_numbers))

    def list_students(self):
        for student in self.students:
            print("Student id: {}, Student name: {}, Date of birth: {}".format(student.id, student.name, student.dob))

    def show_marks(self):
        course_id = int(input("Enter course id: "))
        for enrollment in self.enrollments:
            if enrollment.course_id == course_id:
                print("Student id: {}, Marks: {}".format(enrollment.student_id, enrollment.marks))

    def calculate_gpa(self, student_id):
        student_enrollments = [e for e in self.enrollments if e.student_id == student_id]
        credits = np.array([c.credit_numbers for c in self.courses])
        marks = np.array([e.marks for e in student_enrollments])
        gpa = np.sum(credits*marks)/np.sum(credits)
        return gpa

    def sort_students_by_gpa(self):
        gpas = [self.calculate_gpa(student.id) for student in self.students]
        sorted_students = [student for _, student in sorted(zip(gpas,self.students), reverse=True)]
        return sorted_students

school = School()
school.add_student()
school.add_course()
school.add_marks()
sorted_students = school.sort_students_by_gpa()
print("\nStudents sorted by GPA (descending):")
for student in sorted_students:
    print("Student id: {}, Name: {}, GPA: {:.2f}".format(student.id, student.name, school.calculate_gpa(student.id)))
