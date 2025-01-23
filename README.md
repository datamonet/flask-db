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

## How to Add a Phone Number Column

Follow these steps to add a phone number column to the students table:

1. Update the Student model in `app.py`:
```python
class Student(db.Model):
    # ... existing columns ...
    phone_number = db.Column(db.String(20), nullable=True)
```

2. Create a new migration:
```bash
alembic revision --autogenerate -m "Add phone number to Student model"
```

3. Review the generated migration file in `migrations/versions/` to ensure it uses batch operations for SQLite:
```python
def upgrade() -> None:
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=True))

def downgrade() -> None:
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('phone_number')
```

4. Apply the migration:
```bash
alembic upgrade head
```

5. Update the `seed_db.py` script to include phone numbers:
```python
students = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone_number': '123-456-7890'
    },
    # ... add phone numbers for other students ...
]
```

6. Update the template in `templates/index.html` to display phone numbers:
```html
<table>
    <thead>
        <tr>
            <!-- ... existing columns ... -->
            <th>Phone Number</th>
        </tr>
    </thead>
    <tbody>
        {% for student in students %}
        <tr>
            <!-- ... existing columns ... -->
            <td>{{ student.phone_number }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

7. Reseed the database:
```bash
python seed_db.py
```

8. Restart the Flask application and verify the changes at http://127.0.0.1:5000

Note: Make sure to follow these steps in order. The migration system will handle the database schema update without losing existing data. If you need to start fresh, you can use the seed script which will recreate the database with the new schema.
