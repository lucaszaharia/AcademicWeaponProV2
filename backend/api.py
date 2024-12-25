from flask import Flask
from flask_cors import CORS
from db import create_assignment, get_all_assignments, update_assignment_grade, delete_assignment

app = Flask(__name__)
CORS(app)


@app.route('/getall')
def get_assignments():
    result = get_all_assignments()
    return {"all_assignments": result}

@app.route('/delete/<assignment_name>', methods=['DELETE'])
def delete_an_assignment(assignment_name):
    delete_assignment(assignment_name)
    return 'assignment deleted'

@app.route('/create/<assignment_name>/<course>', methods=['POST'])
def create_an_assignment(assignment_name, course):
    create_assignment(assignment_name, course)
    return 'assignment created'

@app.route('/update/<assignment_name>/<new_grade>', methods=['PUT'])
def update_an_assignment_grade(assignment_name, new_grade):
    update_assignment_grade(assignment_name, new_grade)
    return 'assignment grade updated'
