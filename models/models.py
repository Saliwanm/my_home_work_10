from app import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    #
    # def __repr__(self):
    #     return '<Plant %r>' % self.id

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    type_of_work = db.Column(db.String(100), nullable=False)