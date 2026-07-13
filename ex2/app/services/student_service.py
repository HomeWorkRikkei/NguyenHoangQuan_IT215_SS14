from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

def get_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student_data: StudentCreate):
    db_student = Student(**student_data.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student_data: StudentUpdate):
    db_student = get_student_by_id(db, student_id)
    if db_student:
        for key, value in student_data.model_dump().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student_by_id(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student