from flask import Blueprint, request, render_template
from flask import jsonify

event_list = [
    {"id": 1, "event": "rock concert"},
    {"id": 2, "event": "free banichki"},
    {"id": 3, "event": "coffe time"}
]

event_bluep = Blueprint('event_bluep', __name__, template_folder='templates')

    

@event_bluep.route("/<int:event_id>/<event>", methods=['POST', 'PUT'])                              
def event_put_post(event_id, event):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(event_list)):
            if event_list[i-1]['id'] == event_id:
                id_exist = True
        
        if id_exist == False:
            event_list.append(dict({'id': event_id, 'event': event}))
            return jsonify(event_list)
        else:
            return "ID already exist"

    else:
        for a in event_list:
            if a["id"] == event_id:
                a.update({'event': event})
                return jsonify(a)

        event_list.append(dict({'id': event_id, 'event': event}))
        return jsonify(event_list)

    
    

@event_bluep.route("/<int:event_id>", methods=['GET', 'DELETE'])
def event_delete_get(event_id):
    if request.method == 'GET':
        flag = False
        for event in event_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID not Found!"


    else:
        flag = False
        for i in range(len(event_list)): 
            if event_list[i]['id'] == event_id: 
                del event_list[i] 
                flag = True
                return "Event deleted!"

        if flag == False:
            return "ID not Found!"
    

@event_bluep.route("/all", methods=['GET'])
def get_all():
    return render_template('event.html', events=event_list)