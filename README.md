# Flask SQLite Student Database

A simple Flask web application that uses SQLAlchemy to manage student information in a SQLite database.

## Setup and Installation

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Seed the database with sample data (optional):
```bash
python seed_db.py
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and visit: http://127.0.0.1:5000

## Database

The application uses SQLite database (students.db) which will be automatically created when you run the application for the first time. The database contains a single table 'student' with the following fields:
- id (Primary Key)
- first_name
- last_name
- email (unique, nullable)

## Sample Data
The seed script (`seed_db.py`) will populate the database with 10 sample students. You can run this script once to initialize the database with sample data. The script includes a check to prevent duplicate seeding.

## Database Migrations

This project uses Alembic for database migrations. Here's how to work with migrations:

1. Initialize migrations (already done):
```bash
alembic init migrations
```

2. Create a new migration:
```bash
alembic revision --autogenerate -m "Description of the change"
```

3. Apply migrations:
```bash
alembic upgrade head
```

4. Rollback migrations:
```bash
alembic downgrade -1  # Rollback one step
alembic downgrade base  # Rollback all migrations
```

5. View migration history:
```bash
alembic history
```

Note: When making changes to the database schema, always use migrations rather than modifying the models directly. This ensures that your database changes are tracked and can be rolled back if needed.
