from .mongo import db 

class Student(db.Document):
    name = db.StringField(required=True)
    age = db.IntField(required=True)
    email = db.EmailField(required=True)
    college = db.StringField(required=True)
    