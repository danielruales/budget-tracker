from config import get_db
db = get_db()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_category = db.Column(db.String(50), nullable=False)
    expense_sub_category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Expense('{self.expense_category}', '{self.expense_sub_category}', '{self.description}', '{self.amount}', '{self.country}', '{self.city}', '{self.start_date}', '{self.end_date}')"

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    budget_category = db.Column(db.String(50), nullable=False)
    expense_category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Budget('{self.budget_category}', '{self.expense_category}', '{self.description}', '{self.amount}')"