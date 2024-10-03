from flask import Flask, render_template, request, redirect, url_for
from config import get_app, get_db
# from flask_sqlalchemy import SQLAlchemy
import os

# Import models after initializing db
from models import Expense

app = get_app()
db = get_db()

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form.get('name')
    amount = request.form.get('amount')
    category = request.form.get('category')
    
    new_expense = Expense(name=name, amount=amount, category=category)
    db.session.add(new_expense)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
