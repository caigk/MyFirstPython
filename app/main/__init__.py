from flask import Blueprint,json,render_template
from flask_bootstrap import Bootstrap
import os

bootstrap = Bootstrap()

bp = Blueprint('main',__name__)

@bp.route('/')
def index():
    return render_template("index.html",name=__name__)


@bp.route('/json')
def rjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "../static/data", "strings.json")
    with open(json_url) as json_data:
        d = json.load(json_data)
        return json.dumps(d)
