from flask import Flask
from flask_cors import CORS

from app.db import create_tables
from flask import jsonify
from flask_cors import CORS


create_tables.create_tables()
create_tables.create_super_admin()
app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    '''404 Error function'''
    return (jsonify({'error': str(error)}), 404)


@app.errorhandler(400)
def bad_request(error):
    '''400 Error function'''
    return (jsonify({'error': str(error)}), 400)


@app.errorhandler(405)
def method_not_allowed(error):
    '''405 Error function'''
    return (jsonify({'error': str(error)}), 405)


@app.errorhandler(500)
def server_error(error):
    '''405 Error function'''
    return (jsonify({'error': str(error)}), 500)

app.url_map.strict_slashes = False

from app.api.v2.views import users, incident, api

app.register_blueprint(api, url_prefix='/api/v2')
