from flask import Blueprint,json,jsonify
import os

from . import bp

@bp.route('/test/')
def index():
    return "/"

@bp.route('/test/json')
def rjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "../static/data", "strings.json")
    with open(json_url) as json_data:
        d = json.load(json_data)
        return jsonify(d)

