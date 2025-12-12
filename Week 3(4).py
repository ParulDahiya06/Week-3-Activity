class Student:
    def __init__(self, student_id, first_name, last_name, address, email):
        # Student attributes
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        # Courses the student enrolls in
        self.courses = []


class Professor:
    def __init__(self, professor_id, first_name, last_name, address, email):
        # Professor attributes
        self.professor_id = professor_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        # Courses the professor teaches
        self.courses = []


class Course:
    def __init__(self, course_id, duration, title, credits):
        # Course attributes
        self.course_id = course_id
        self.duration = duration
        self.title = title
        self.credits = credits
        # Lists to store students and teachers
        self.students = []
        self.professors = []

# Creating Objects From Classes
# Create Courses
MSE800 = Course("MSE800", "12 weeks", "Software Engineering", 15)
MSE801 = Course("MSE801", "12 weeks", "Quantum Computing", 15)

# Create Students
s1 = Student(1, "Neha", "Chhikara", "Auckland", "john@example.com")
s2 = Student(2, "Vansh", "Chhikara", "Manukau", "emma@example.com")
s3 = Student(3, "Raveena", "Khan", "Hamilton", "liam@example.com")

# Create Professors
p1 = Professor(101, "Dr", "Mohammad", "Auckland", "drmohammad@example.com")
p2 = Professor(102, "Arun", "Kumar", "Wellington", "arunkumar@example.com")
p3 = Professor(103, "Savita", "Bai", "Auckland", "savitabai@example.com")

# Enroll students in courses
# Students in MSE800
MSE800.students.extend([s1, s2])
# Students in MSE801
MSE801.students.extend([s2, s3])

# Assign professors to courses
# Teachers for MSE800
MSE800.professors.append(p1)

# Teachers for MSE801
MSE801.professors.extend([p2, p3])

# Add course mapping to students and professors
for stu in MSE800.students:
    stu.courses.append(MSE800)

for stu in MSE801.students:
    stu.courses.append(MSE801)

for prof in MSE800.professors:
    prof.courses.append(MSE800)

for prof in MSE801.professors:
    prof.courses.append(MSE801)


# 1. Count number of students in MSE800
num_students_MSE800 = len(MSE800.students)

# 2. List teachers teaching MSE801
teachers_MSE801 = [f"{p.first_name} {p.last_name}" for p in MSE801.professors]


print("Number of Students enrolled in MSE800:", num_students_MSE800)

print("Teachers teaching MSE801:")
for teacher in teachers_MSE801:
    print("-", teacher)
