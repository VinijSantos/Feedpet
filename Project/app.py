from flask import Flask
from routes.landing import landing_route
from routes.user import user_route

app = Flask(__name__)

app.register_blueprint(landing_route)
app.register_blueprint(user_route, url_prefix='/user')

app.run(debug=True)
