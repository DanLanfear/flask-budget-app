from flask import Flask, render_template, url_for
from forms import CategoryForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1da3698b08a11964197e690e97054059'

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