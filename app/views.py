from app import db
from .models import *
import re


def insert_asset(name, count):
    existing = Asset.query.filter_by(name=name)
    print(existing.count())
    if(existing.count() > 0):
        asset = existing.first()
        asset.count += count
        flashmsg = "Count added to existing asset with same name!"
    else:
        asset = Asset(name=name, count=count)
        db.session.add(asset)
        flashmsg = "New asset created successfully!"
    db.session.commit()
    return flashmsg


def insert_task(name, freq):
    existing = Task.query.filter_by(name=name)
    print(existing.count())
    if(existing.count() > 0):
        flashmsg = "This task already exists! Try again!"
    else:
        task = Task(name=name, freq=freq)
        db.session.add(task)
        db.session.commit()
        flashmsg = "New task created successfully!"
    return flashmsg


def insert_worker(name, email, number):
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match is None:
        flashmsg = "Invalid email! Try again!"
        return flashmsg
    existing = Worker.query.filter_by(name=name)
    print(existing.count())
    if(existing.count() > 0):
        flashmsg = "This worker already exists! Try again!"
    else:
        worker = Worker(name=name, email=email, phonenum=number)
        db.session.add(worker)
        db.session.commit()
        flashmsg = "New worker added successfully!"
    return flashmsg
