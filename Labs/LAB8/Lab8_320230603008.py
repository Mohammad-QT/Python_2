# Task 1
student = {
    "name": "Ahmad",
    "id": "2024001",
    "major": "Artificial Intelligence",
    "grade": 85
}

print("Student Name:", student["name"])
print("Student ID:", student["id"])
print("Major:", student["major"])
print("Grade:", student["grade"])
print()

# Task 2
if student["grade"] >= 60:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print(student)
print()

# Task 3
new_grade = int(input("Enter new grade: "))
student["grade"] = new_grade

if student["grade"] >= 60:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print(student)
print()

# Task 4
def get_status(grade):
    if grade >= 60:
        return "Pass"
    else:
        return "Fail"

print(get_status(85))
print(get_status(45))
print()

# Task 5
def print_student_info(std):
    print("Name:", std["name"])
    print("ID:", std["id"])
    print("Major:", std["major"])
    print("Grade:", std["grade"])
    print("Status:", std["status"])

print_student_info(student)
print()

# Task 6
def update_grade(std, new_grade):
    std["grade"] = new_grade
    std["status"] = get_status(new_grade)
    return std

student = update_grade(student, 92)
print(student)
print()

# Task 7
def create_student(name, std_id, major, grade):
    return {
        "name": name,
        "id": std_id,
        "major": major,
        "grade": grade,
        "status": get_status(grade)
    }

s1 = create_student("Omar", "2024005", "Data Science", 75)
s2 = create_student("Laila", "2024006", "Computer Science", 88)

# Task 8
def create_student_kwargs(**kwargs):
    return kwargs

student2 = create_student_kwargs(name="Sara", id="2024002", major="Computer Science", grade=92)
student2["status"] = get_status(student2["grade"])

# Task 9
students = {
    "2024001": student,
    "2024002": student2
}

for key in students:
    print(students[key])
print()

# Task 10
def find_student(students_dict, std_id):
    if std_id in students_dict:
        return students_dict[std_id]
    else:
        return "Student not found"

print(find_student(students, "2024001"))
print(find_student(students, "2024999"))