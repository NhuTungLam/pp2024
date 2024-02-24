def show_courses(courses):
    for course in courses:
        print("Course id: {}, Course name: {}, Credit numbers: {}".format(course.id, course.name, course.credit_numbers))


def show_students(students):
    for student in students:
        print("Student id: {}, Student name: {}, Date of birth: {}".format(student.id, student.name, student.dob))


def show_marks(enrollments):
    course_id = int(input("Enter course id: "))
    for enrollment in enrollments:
        if enrollment.course_id == course_id:
            print("Student id: {}, Marks: {}".format(enrollment.student_id, enrollment.marks))


def show_sorted_students(sorted_students, school):
    print("\nStudents sorted by GPA (descending):")
    for student in sorted_students:
        print("Student id: {}, Name: {}, GPA: {:.2f}".format(student.id, student.name, school.calculate_gpa(student.id)))