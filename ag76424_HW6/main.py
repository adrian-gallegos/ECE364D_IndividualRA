import os

from flask import Flask, jsonify, request

#app = Flask(__name__)
app = Flask(__name__, static_folder='./build', static_url_path='/')
app.secret_key = 'RL sucks'


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/checkin_hardware/<int:project_id>/<int:qty>/', methods=['POST', 'GET'])
def checkin_hardware(project_id, qty):
    # Process check-in logic here
    message = f"{qty} hardware checked in"
    return jsonify({'message': message})


@app.route('/checkout_hardware/<int:project_id>/<int:qty>/', methods=['POST', 'GET'])
def checkout_hardware(project_id, qty):
    # Process check-out logic here
    message = f"{qty} hardware checked out"
    return jsonify({'message': message})


@app.route('/join_project/<int:project_id>/', methods=['POST', 'GET'])
def join_project(project_id):
    # Process join project logic here
    message = f"Joined {project_id}"
    return jsonify({'message': message})


@app.route('/leave_project/<int:project_id>/', methods=['POST', 'GET'])
def leave_project(project_id):
    # Process leave project logic here
    message = f"Left {project_id}"
    return jsonify({'message': message})


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 3000))
