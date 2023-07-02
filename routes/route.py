from controllers.student import StudentApi , StudentsApi


def initialize_routes(api):
    api.add_resource(StudentApi, '/api')
    api.add_resource(StudentsApi, '/api/students')