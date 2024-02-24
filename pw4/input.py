def get_num_students():
    return int(input("Enter the number of students in the class: "))
def get_student_info():
    id = int(input("Enter student id: "))
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return id, name, dob


def get_num_courses():
    return int(input("Enter the number of courses: "))


def get_course_info():
    id = int(input("Enter course id: "))
    name = input("Enter course name: ")
    credit_numbers = int(input("Enter credit numbers for {}: ".format(name)))
    return id, name, credit_numbers


def get_marks(students):
    course_id = int(input("Enter course id: "))
    for student in students:
        student_id = student.id
        raw_marks = float(input("Enter marks for student id {}: ".format(student_id)))
        # round down to 1 decimal place
        marks = math.floor(raw_marks*10)/10
        enrollment = StudentEnrollment(student_id, course_id, marks)
        yield enrollment