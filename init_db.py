from config import get_app, get_db
app = get_app()
db = get_db()

# Create all database tables
with app.app_context():
    db.create_all()
    print("Database initialized successfully.")
