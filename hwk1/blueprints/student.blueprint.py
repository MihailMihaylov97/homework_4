from flask import Blueprint, request, render_template
from flask import jsonify

students_list = [
    {"id": 1, "name": "Ivancho"},
    {"id": 2, "name": "Dragancho"},
    {"id": 3, "name": "Petkancho"}
]    

student_bluep = Blueprint('student_bluep', __name__, template_folder='templates')
    
@student_bluep.route("/<int:student_id>/<name>", methods=['POST', 'PUT'])               
def student_put_post(student_id,name):
    id_exist = False
    if request.method == 'POST':
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
                
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exist"
    else:             
        for a in students_list:
            if a["id"] == student_id:
                a.update({'name': name})
                return jsonify(a)

        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)



@student_bluep.route("/<int:student_id>", methods=['GET', 'DELETE'])
def student_get_delete(student_id):
    if request.method == 'GET':               
       
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID not Found!"
    else:
        
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True 
                return "Student deleted!"

        if flag == False:
            return "ID not Found!"


@student_bluep.route("/all", methods=['GET'])
def get_all():
    return render_template('student.html', students=students_list)
