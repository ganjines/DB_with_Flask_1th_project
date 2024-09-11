from flask import render_template, request, jsonify
from app import app, db

@app.route('/')
def index():
    return "Hello, Flask!"

@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    # Example of adding data to the database
    # Assuming you have a model named 'Employee'
    # employee = Employee(name=data['name'], age=data['age'])
    # db.session.add(employee)
    # db.session.commit()
    return jsonify({'status': 'success'}), 200

