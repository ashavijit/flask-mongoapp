from flask import Response, request
from database.model import Student
from flask_restful import Resource

class StudentsApi(Resource):
    def get(self):
        students = Student.objects().to_json()
        return Response(students, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        student = Student(**body).save()
        id = student.id
        return {'id': str(id)}, 200
    
class StudentApi(Resource):
    def put(self, id):
        body = request.get_json()
        Student.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        Student.objects.get(id=id).delete()
        return '', 200
    
    def get(self, id):
        students = Student.objects.get(id=id).to_json()
        return Response(students, mimetype="application/json", status=200)
