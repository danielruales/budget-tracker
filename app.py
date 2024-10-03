from flask import Flask, render_template, request, redirect, url_for
from config import get_app, get_db
from datetime import datetime, date

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
    expense_category = request.form.get('expense_category')
    expense_sub_category = request.form.get('expense_sub_category')
    description = request.form.get('description')
    amount = request.form.get('amount')
    country = request.form.get('country')
    city = request.form.get('city')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    new_expense = Expense(expense_category=expense_category, expense_sub_category=expense_sub_category, description=description,
                          amount=amount, country=country, city=city, start_date=start_date_obj, end_date=end_date_obj)
    db.session.add(new_expense)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
