from flask import render_template, url_for, flash, redirect
from flaskbudget import app, db
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

@app.route("/categories", methods=['GET', 'POST'])
def manage_categories():
    form = CategoryForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash(f'Category {form.name.data} created', 'success')
        return redirect(url_for('manage_categories'))
    return render_template('categories.html',title='Categories', form=form, categories=categories)

@app.route("/categories/<category_id>", methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash(f'Category {category.name} deleted', 'success')
    return redirect(url_for('manage_categories'))