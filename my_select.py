from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from models import Student, Group, Teacher, Subject, Grade, engine
from sqlalchemy import desc


Session = sessionmaker(bind=engine)
session = Session()




def select_1():
    result = session.query(Student.name, func.avg(Grade.grade).label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2(subject_id):
    subject_name = session.query(Subject.name).filter(Subject.id == subject_id).scalar()
    result = session.query(Student.name, func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade')).first()    
    if result:
        student_name, avg_grade = result
        return student_name, avg_grade, subject_name
    return None, None, subject_name

def select_3(subject_id):
    subject_name = session.query(Subject.name).filter(Subject.id == subject_id).scalar()
    result = session.query(Group.name, func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Group, Student.group_id == Group.id)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id).all()
    return subject_name, result

def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    return result

def select_5(teacher_id):
    teacher_name = session.query(Teacher.name).filter(Teacher.id == teacher_id).scalar()
    result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return teacher_name, result

def select_6(group_id):
    group_name = session.query(Group.name).filter(Group.id == group_id).scalar()
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return group_name, result

def select_7(group_id, subject_id):
    group_name = session.query(Group.name).filter(Group.id == group_id).scalar()
    subject_name = session.query(Subject.name).filter(Subject.id == subject_id).scalar()
    result = session.query(Student.name, Grade.grade)\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    return group_name, subject_name, result

def select_8(teacher_id):
    teacher_name = session.query(Teacher.name).filter(Teacher.id == teacher_id).scalar()

    result = session.query(func.avg(Grade.grade))\
        .select_from(Grade)\
        .join(Subject, Grade.subject_id == Subject.id)\
        .filter(Subject.teacher_id == teacher_id).scalar()
    
    return teacher_name, result

def select_9(student_id):
    result = session.query(Student.name, Subject.name)\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Subject, Grade.subject_id == Subject.id)\
        .filter(Grade.student_id == student_id).distinct().all()
    return result

def select_10(student_id, teacher_id):

    student_name = session.query(Student.name).filter(Student.id == student_id).scalar()
    teacher_name = session.query(Teacher.name).filter(Teacher.id == teacher_id).scalar()
    
    courses = session.query(Subject.name)\
        .select_from(Grade)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Subject, Grade.subject_id == Subject.id)\
        .join(Teacher, Subject.teacher_id == Teacher.id)\
        .filter(Student.id == student_id, Teacher.id == teacher_id)\
        .distinct()\
        .all()
    
    return student_name, teacher_name, [course[0] for course in courses]



