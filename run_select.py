from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from seed import Student, Group, Teacher, Subject, Grade


subject_id = 1
teacher_id = 1
group_id = 1
student_id = 1


print("\n1. Топ 5 студентів за середнім балом:")
for student_name, avg_grade in select_1():
    print(f"{student_name}: {avg_grade:.2f}")


student_name, avg_grade, subject_name = select_2(subject_id=5)
print(f"\n2. Студент із найвищим середнім балом з предмета {subject_name}:")
print(f"{student_name} ({avg_grade:.2f})")


subject_name, avg_grades = select_3(subject_id=6)
print(f"\n3. Середній бал у групах з предмета {subject_name}:")
for group_name, avg_grade in avg_grades:
    print(f"{group_name}: {avg_grade:.2f}")


print("\n4. Середній бал на потоці:")
print(f"{select_4():.2f}")


teacher_name, subjects = select_5(teacher_id=2)
print(f"\n5. Курси, які читає викладач {teacher_name}:")
for subject_name, in subjects:
    print(subject_name)


group_name, students = select_6(group_id=group_id)
print(f"\n6. Список студентів у групі {group_name}:")
for student_name, in students:
    print(student_name)


group_name, subject_name, grades = select_7(group_id=3, subject_id=5)
print(f"\n7. Оцінки студентів у групі {group_name} з предмета {subject_name}:")
for student_name, grade in grades:
    print(f"{student_name}: {grade:.0f}")


teacher_name, avg_grade = select_8(teacher_id=teacher_id)
print(f"\n8. Середній бал, який ставить викладач {teacher_name}:")
print(f"{avg_grade:.2f}")


print(f"\n9. Список курсів, які відвідує студент:")
for student_name, subject_name in select_9(student_id=student_id):
    print(f"{student_name} відвідує курс {subject_name}")


student_name, teacher_name, courses = select_10(student_id=student_id, teacher_id=3)
print(f"\n10. Список курсів, які студенту {student_name} читає викладач {teacher_name}:")
for course in courses:
    print(course)