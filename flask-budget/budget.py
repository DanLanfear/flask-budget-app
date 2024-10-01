from datetime import datetime
import os   
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CategoryForm

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '1da3698b08a11964197e690e97054059'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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
    amount = db.Column(db.Integer, nullable=False)
    # uses table name
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"Transaction('{self.name}, {self.date}, {self.amount}')"

transactions = [
    {
        'date': 'September 29, 2024',
        'name': 'kroger',
        'amount': 109.84,
    },
    {
        'date': 'September 30, 2024',
        'name': 'gas',
        'amount': 30.67,
    }
]



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/transactions")
def manage_transactions():
    return render_template('transactions.html', transactions=transactions)

@app.route("/categories")
def manage_categories():
    form = CategoryForm()
    return render_template('categories.html',title='Categories', form=form)

if __name__ == '__main__':
    app.run(debug=True)