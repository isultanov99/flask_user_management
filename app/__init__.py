from flask import Flask


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '345fe1722edfee6c073b94e01d1e6310e2b4c199'
from app import routes

