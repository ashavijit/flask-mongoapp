from flask import Flask, request, render_template
from flask_restful import Api
from database.mongo import initialize_db
from database.model import Student
from helpers.duplicatecheck import StudentDuplicates

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://avijitsenme:NwSMaIPYB4rTl3dU@cluster0.jkk56o8.mongodb.net/?retryWrites=true&w=majority'
}

initialize_db(app)

with app.app_context():
    from mongoengine import connect
    from mongoengine.connection import get_connection
    try:
        connect(host='mongodb+srv://avijitsenme:NwSMaIPYB4rTl3dU@cluster0.jkk56o8.mongodb.net/?retryWrites=true&w=majority')
        connection = get_connection()
        if connection is not None:
            print("Connected to MongoDB Atlas!" + str(connection))
    except Exception as e:
        print(e) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        college = request.form['college']

        # Check for duplicates
        duplicate_response = StudentDuplicates(name, email)
        if duplicate_response:
            return duplicate_response

        student = Student(name=name, age=age, email=email, college=college)
        student.save()
        return 'Student added successfully!' + str(student.id)
    
    return render_template('index.html')

from routes.route import initialize_routes
initialize_routes(api)

if __name__ == '__main__':
    app.run()
