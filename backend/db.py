from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from samplekeys import uri

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.schoolwork0

def create_assignment(
        assignment_name: str,
        course: str,
        ) -> bool:
    """

    Function for adding an assignment to the db, with grade initially set to 0

    Args:
        assignment_name (str): name of assignment to be created
        course (str): course code for assignment to be created

    Returns:
        bool: True if assignment was added successfully

    """
    assignment_doc = {
        'assignment_name': assignment_name,
        'course_code': course,
        'grade': 0
    }
    return db.assignments.insert_one(assignment_doc).acknowledged

def get_all_assignments() -> list[dict]:
    """

    Retrieves all assignments from the DB

    Returns:
        list[dict]: list of assignment documents in the db, each stored as dictionaries

    """
    cursor = db.assignments.find()
    results = []
    for x in cursor:
        x.pop('_id')
        results.append(x)
    return results

def update_assignment_grade(assignment_name: str, new_grade: float) -> bool:
    """
    
    Updates grade value of assignment with provided name in db

    Args:
        assignment_name (str): name of assignment to modify
        new_grade (float): new grade to set

    Returns:
        bool: True if 1 assignment was modified, False otherwise
    
    """
    assignment_filter = {'assignment_name': assignment_name}
    updated_vals = {"$set": {'grade': new_grade}}
    if db.assignments.update_one(assignment_filter, updated_vals).raw_result['n'] == 1:
        return True
    
    return False

def delete_assignment(assignment_name: str) -> bool:
    """

    Deletes an assignment with the given name from the DB

    Args:
        assignment_name (str): name of assignment to be deleted

    Returns:
        bool: True if an assignment was deleted, False otherwise
        
    """
    if db.assignments.delete_one({'assignment_name': assignment_name}).raw_result['n'] == 1:
        return True
    return False

x=4