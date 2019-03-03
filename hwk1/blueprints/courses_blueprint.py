
    
from flask import Blueprint, request, render_template
from flask import jsonify

course_list = [
    {"id": 1, "name": "BUS"},
    {"id": 2, "name": "INF"},
    {"id": 3, "name": "ECO"}
]

course_bluep = Blueprint('course_bluep', __name__, template_folder='templates')
    

@course_bluep.route("/<int:course_id>/<name>", methods=['POST', 'PUT'])               
def course_put_post(course_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(course_list)):
            if course_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            course_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(course_list)
        else:
            return "ID already exist"

    else:
        for a in course_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        course_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(course_list)
    

@course_bluep.route("/<int:course_id>", methods=['GET', 'DELETE'])                              
def course_delete_get(course_id):
    if request.method == 'GET':
        flag = False
        for course in course_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"


    else:
        flag = False
        for i in range(len(course_list)): 
            if course_list[i]['id'] == course_id: 
                del course_list[i]
                flag = True
                return "Course deleted!"

        if flag == False:
            return "ID not Found!"




@course_bluep.route("/all", methods=['GET'])
def get_all():
    return render_template('course.html', courses=course_list)