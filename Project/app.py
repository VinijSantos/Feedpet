from flask import Flask
from config import config_all

app = Flask(__name__)

config_all(app)

app.run(debug=True)
