#!/usr/bin/python3
"""first endpoint (route) will be to return the status of your API
"""

from api.v1.views import app_views


@app_views.route('/status')
def status():
    """return ok if everything works
    """
    return ({'status': 'OK'})
