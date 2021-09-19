#!/usr/bin/python3
from flask import make_response, jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State


@app_views.route('/status')
def index():
    """
        Returns a JSON:"status": "OK"
    """
    return make_response(jsonify({'status': 'OK'}), 200)


@app_views.route('/stats')
def stats():
    """
    Endpoint that retrieves the number of each
    objects by type.
    """
    return make_response(jsonify({
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User),
    }), 200)
