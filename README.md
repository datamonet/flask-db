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

## Sample Data
The seed script (`seed_db.py`) will populate the database with 10 sample students. You can run this script once to initialize the database with sample data. The script includes a check to prevent duplicate seeding.
