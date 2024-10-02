from flask import render_template, url_for, flash, redirect
from flaskbudget import app
from flaskbudget.models import Transaction, Category
from flaskbudget.forms import CategoryForm



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
