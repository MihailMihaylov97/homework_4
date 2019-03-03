from flask_restful import Resource
from flask import jsonify

event_list = [
    {"id": 1, "event": "rock concert"},
    {"id": 2, "event": "free banichki"},
    {"id": 3, "event": "coffe time"}
]

class Event_one(Resource):
    
                   
    def post(self, event_id, event):
        id_exist = False
        for i in range(len(event_list)):
            if event_list[i-1]['id'] == event_id:
                id_exist = True
        
        if id_exist == False:
            event_list.append(dict({'id': event_id, 'event': event}))
            return jsonify(event_list)
        else:
            return "ID already exist"

    def put(self, event_id, event):

        for a in event_list:
            if a["id"] == event_id:
                a.update({'event': event})
                return jsonify(a)

        event_list.append(dict({'id': event_id, 'event': event}))
        return jsonify(event_list)

    
class Event_two(Resource):
    
    def get(self, event_id):
        flag = False
        for event in event_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID not Found!"

    def delete(self, event_id):
        flag = False
        for i in range(len(event_list)): 
            if event_list[i]['id'] == event_id: 
                del event_list[i] 
                flag = True
                return "Event deleted!"

        if flag == False:
            return "ID not Found!"
    

class All_events(Resource):
    def get(self):
        return jsonify(event_list)