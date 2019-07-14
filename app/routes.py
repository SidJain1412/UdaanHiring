from app import app
from flask import url_for, redirect, render_template, flash, request, jsonify
from .views import *
import requests


# Homepage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Add asset form page
@app.route('/add_asset_form')
def add_asset():
    return render_template('add_asset_form.html')


# Add asset API
# Takes asset name and count as input (form-data)
# Returns add asset page (add_asset)
# Tested working using Postman
@app.route('/add_asset', methods=['POST'])
def add_asset_data():
    data = request.form
    name = data['name']
    count = data['count']
    try:
        count = int(count)
    except Exception as e:
        print(str(e))
        flash('Please enter a positive integer in asset count!')
        return redirect(url_for('add_asset'))
    if count < 1:
        flash('Please enter a positive integer in asset count!')
        return redirect(url_for('add_asset'))
    message = insert_asset(name, count)
    print(name)
    print(count)
    flash(message)
    return redirect(url_for('add_asset'))


# API for returning all assets.
# This API is being used in the 'view_assets' html page
# If no assets, then returning error. Checking for this in HTML using Jinja
@app.route('/assets/all', methods=['GET'])
def all_assets():
    assets = Asset.query.all()
    try:
        foo = assets.count()
    except:
        foo = len(assets)
    if(foo > 0):
        res = []
        for a in assets:
            x = {}
            x['name'] = a.name
            x['count'] = a.count
            res.append(x)
        return jsonify(res)
    return jsonify({'error': 'No assets'})


# Rendering all assets through the '/assets/all' API
@app.route('/view_assets', methods=['GET'])
def view_assets():
    url = "http://127.0.0.1:5000/assets/all"
    assets = requests.get(url)
    print(assets.text)
    return render_template("all_assets.html", assets=eval(assets.text))


# API to get tasks for a certain worker
# If no tasks then return error.
@app.route('/get_tasks_for_worker/<int:workerId>', methods=["GET"])
def get_tasks_for_worker(workerId):
    tasks = Task.query.filter_by(workerId=workerId)
    try:
        foo = tasks.count()
    except:
        foo = len(tasks)
    if(foo > 0):
        res = []
        for t in tasks:
            x = {}
            x['TaskName'] = t.name
            x['TaskId'] = t.id
            res.append(x)
        return jsonify(res)
    return jsonify({'error': 'No Tasks assigned to this user'})


# Add task form page
@app.route('/add_task_form')
def add_task_form():
    return render_template('add_task_form.html')


# Post API to add a task
# Pass 'name' and 'freq' to this API in 'form-data'
# Acceptable frequencies are: 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly'
@app.route('/add_task', methods=["POST"])
def add_task():
    data = request.form
    name = data['name']
    freq = data['freq']
    acceptable_frequencies = ['Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly']

    if freq not in acceptable_frequencies:
        flash({'error': 'Unacceptable frequency! Select from allowed please.'})
        return redirect(url_for('add_task_form'))
    message = insert_task(name, freq)
    print(name)
    print(freq)
    flash(message)
    return redirect(url_for('add_task_form'))


# Add worker form page
@app.route('/add_worker_form')
def add_worker_form():
    return render_template('add_worker_form.html')


# Post API to add a worker
# Pass 'name', 'email' and 'number' to this API in 'form-data'
# Email will be validated
@app.route('/add_worker', methods=["POST"])
def add_worker():
    data = request.form
    name = data['name']
    email = data['email']
    number = data['number']

    message = insert_worker(name, email, number)
    print(name)
    print(email)
    print(number)
    flash(message)
    return redirect(url_for('add_worker_form'))


# Allocate Task form page
@app.route('/allocate_task_form')
def allocate_task_form():
    return render_template('allocate_task_form.html')


# Allocate Task API
@app.route('/allocate_task', methods=["POST"])
def allocate_task():
    data = request.form
    assetId = data['assetId']
    taskId = data['taskId']
    workerId = data['workerId']
    taskToBePerformedBy = data['taskToBePerformedBy']

    message = assign_task(assetId, taskId, workerId, taskToBePerformedBy)
    flash(message)
    return redirect(url_for('allocate_task_form'))