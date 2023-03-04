from database.models import CoreBodyPart, SubBodyPart, Exercise
from database.data import db




def get_core_body_parts():
    return db.query(CoreBodyPart).all()


def get_sub_body_parts():
    return db.query(SubBodyPart).all()
    


def get_exercises():
    return db.query(Exercise).all()