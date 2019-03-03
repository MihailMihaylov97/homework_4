from flask_restful import Resource
from flask import jsonify

course_list = [
    {"id": 1, "name": "BUS"},
    {"id": 2, "name": "INF"},
    {"id": 3, "name": "ECO"}
]

class Course_one(Resource):
               
    def post(self,course_id,name):

        id_exist = False
        for i in range(len(course_list)):
            if course_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            course_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(course_list)
        else:
            return "ID already exist"
            
    def put(self,course_id,name):

        for a in course_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        course_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(course_list)
    

class Course_two(Resource):

    def get(self, course_id):
        flag = False
        for course in course_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"

     
    def delete(self, course_id):
        flag = False
        for i in range(len(course_list)): 
            if course_list[i]['id'] == course_id: 
                del course_list[i]
                flag = True
                return "Course deleted!"

        if flag == False:
            return "ID not Found!"


class All_courses(Resource):
    def get(self):
        return jsonify(course_list)