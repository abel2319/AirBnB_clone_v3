#!/usr/bin/python3
"""first endpoint (route) will be to return the status of your API
"""


from flask import Blueprint, render_template, abort

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.state import *
