student = {}
courses = {}
student_marks_list = {}

def add_student():
    num_student = int(input("Enter the number of student in the class: "))
    for i in range(num_student):
        student_id = int(input("Enter student id: "))
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student.append((student_id, student_name, student_dob))


def add_course():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id = int(input("Enter course id: "))
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))


def add_marks():
    course_id = int(input("Enter course id: "))
    student_id = student[0]
    marks = int(input("Enter marks for student id {}: ".format(student_id)))
    student_marks = (student_id, course_id, marks)
    student_marks_list.append(student_marks)

# Listing functions
def list_courses():
    for course in courses:
        course_id = course[0]
        course_name = course[1]
    print("Course id: {}, Course name: {}".format(course_id, course_name))


def list_student():
    for student in student:
        student_id = student[0]
        student_name = student[1]
        student_dob = student[2]
        print("Student id: {}, Student name: {}, Date of birth: {}".format(student_id, student_name, student_dob))


def show_marks():
    course_id = int(input("Enter course id: "))
    for student_mark in student_marks_list:
        student_id = student_mark[0]
        mark_course_id = student_mark[1]
        mark = student_mark[2]
        if mark_course_id == course_id:
            print("Student id: {}, Marks: {}".format(student_id, mark))
add_student()
add_marks()
add_course()
list_courses()
list_student()
show_marks()