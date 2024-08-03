from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import date, timedelta
from models import Group, Student, Teacher, Subject, Grade, engine, Base

# Очистка бази даних перед заповненням
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()



named_of_group = ['A', 'B', 'C']
groups = [Group(name=f'Group {i}') for i in named_of_group]
session.add_all(groups)
session.commit()


teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()


subjects_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Geography', 'Art']

subjects = [Subject(name=name, teacher=random.choice(teachers)) for name in subjects_names]
session.add_all(subjects)
session.commit()


students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()


grades = []
for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                date=fake.date_between(start_date='-1y', end_date='today'),
                grade=random.uniform(60, 100)
            )
            grades.append(grade)
session.add_all(grades)
session.commit()

print("Database seeded successfully!")