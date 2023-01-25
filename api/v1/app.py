#!/usr/bin/python3
"""first endpoint (route) will be to return the status of your API
"""


from models import storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """method to handle @app.teardown_appcontext"""
    storage.close()


@simple_page.errorhandler(404)
def page_not_found(error):
    """handler for 404 errors """
    return make_response(jsonify({'error': 'Not found'}), 404)


host = '0.0.0.0'
port = 5000

if getenv('HBNB_API_HOST'):
    host = getenv('HBNB_API_HOST')
if getenv('HBNB_API_PORT'):
    port = getenv('HBNB_API_PORT')


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
