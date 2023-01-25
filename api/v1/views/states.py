#!/usr/bin/python3
"""
handles all default RESTFul API actions
"""
from flask import abort, jsonify, request
from models.state import State
from api.v1.views import app_views


state = State()


@app_views.route('/api/v1/states',
                 methods = ['GET', 'POST'])
def all_state():
    """get all states and create new state"""
    if request.method == 'GET':
        return (state.to_dict())

    elif request.method == 'POST':
        if not request.get_json():
            return make_response(jsonify({'error': 'Not a JSON'}), 400)
        
        data = request.get_json()
        if 'name' not in data:
            return make_response(jsonify({'error': 'Missing name'}), 400)
    
        tmp = State(**data)
        tmp.save()
        return make_response(jsonify(tmp.to_dict()), 201)


@app_views.route('/api/v1/states/<string:state_id>',
                 methods = ['DELETE', 'GET'])
def state_id(state_id):
    """Delete and get state"""
    if state_id is not None:
        objs = state.to_dict()
        if request.method == 'GET':
            for obj in objs:
                if objs[obj] == state_id:
                    return (jsonify(objs[obj]))
        if request.method == 'DELETE':
            for obj in objs:
                if objs[obj] == state_id:
                    objs[obj].delete()
                    return (jsonify({}))    
    abort(404)
