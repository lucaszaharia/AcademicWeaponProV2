from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from keys import uri

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.schoolwork0

def create_assignment(
        assignment_name: str,
        course: str,
        ):
    assignment_doc = {
        'assignment_name': assignment_name,
        'course_code': course,
        'grade': 0
    }
    return db.assignments.insert_one(assignment_doc)

def get_all_assignments():
    cursor = db.assignments.find()
    results = []
    for x in cursor:
        x.pop('_id')
        results.append(x)
    return results

def update_assignment_grade(assignment_name: str, new_grade: float):
    assignment_filter = {'assignment_name': assignment_name}
    updated_vals = {"$set": {'grade': new_grade}}
    return db.assignments.update_one(assignment_filter, updated_vals)

def delete_assignment(assignment_name:str):
    return db.assignments.delete_one({'assignment_name': assignment_name})
