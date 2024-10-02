from datetime import datetime
from flaskbudget import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), unique=True, nullable=False)
    # uses actual class
    transactions = db.relationship('Transaction', backref='spending_category', lazy=True)

    def __repr__(self):
        return f"Category('{self.id}, {self.category}')"
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default = datetime.now)
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    # uses table name
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"Transaction('{self.name}, {self.date}, {self.amount}')"
