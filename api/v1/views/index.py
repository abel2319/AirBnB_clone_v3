#!/usr/bin/python3
"""first endpoint (route) will be to return the status of your API
"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """return ok if everything works
    """
    return ({'status': 'OK'})


@app_views.route('/stats')
def stats():
    dict_stat = {
            "amenities": strorage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return (dict_stat)
