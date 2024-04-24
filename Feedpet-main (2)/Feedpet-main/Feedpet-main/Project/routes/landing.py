from flask import Blueprint, render_template, url_for

landing_route = Blueprint('landing', __name__)


@landing_route.route('/')
def landing_page():
    return render_template('index.html')
