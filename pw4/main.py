import math
import numpy as np
from domains.student import Student
from domains.course import Course
from domains.enrollment import StudentEnrollment
from input import *
from output import *


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_students(self):
        num_students = get_num_students()
        for i in range(num_students):
            id, name, dob = get_student_info()
            student = Student(id, name, dob)
            self.students.append(student)

    def add_courses(self):
        num_courses = get_num_courses()
        for i in range(num_courses):
            id, name, credit_numbers = get_course_info()
            course = Course(id, name, credit_numbers)
            self.courses.append(course)

    def add_marks(self):
        marks = get_marks(self.students)
        self.enrollments += marks

    def list_courses(self):
        show_courses(self.courses)

    def list_students(self):
        show_students(self.students)

    def show_marks(self):
        show_marks(self.enrollments)

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


if __name__ == "__main__":
    school = School()
    school.add_students()
    school.add_courses()
    school.add_marks()
    sorted_students = school.sort_students_by_gpa()
    show_sorted_students(sorted_students, school)
