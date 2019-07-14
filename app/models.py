from app import db
from datetime import datetime


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), index=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    count = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Asset {}>'.format(self.name)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), index=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    freq = db.Column(db.Integer, index=True)
    timeofalloc = db.Column(db.DateTime, index=True, default=None)
    taskToBePerformedBy = db.Column(db.DateTime, index=True, default=None)
    workerId = db.Column(db.Integer, db.ForeignKey('worker.id'), default=None)
    assetId = db.Column(db.Integer, db.ForeignKey('asset.id'), default=None)
    
    def __repr__(self):
        return '<Task {}>'.format(self.name)


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), index=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    email = db.Column(db.String(96), index=True)
    phonenum = db.Column(db.String(96), index=True)
    tasks = db.relationship('Task', backref='AssignedWorker', lazy='dynamic')

    def __repr__(self):
        return '<Worked {}>'.format(self.name)
