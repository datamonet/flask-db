from app import app, db, Student

def seed_database():
    # Sample student data
    students = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Michael', 'last_name': 'Johnson'},
        {'first_name': 'Emily', 'last_name': 'Brown'},
        {'first_name': 'David', 'last_name': 'Wilson'},
        {'first_name': 'Sarah', 'last_name': 'Davis'},
        {'first_name': 'James', 'last_name': 'Miller'},
        {'first_name': 'Emma', 'last_name': 'Taylor'},
        {'first_name': 'William', 'last_name': 'Anderson'},
        {'first_name': 'Olivia', 'last_name': 'Thomas'}
    ]

    # Create all tables
    with app.app_context():
        db.create_all()
        
        # Check if database is already populated
        if Student.query.first() is None:
            # Add students to the database
            for student_data in students:
                student = Student(**student_data)
                db.session.add(student)
            
            # Commit the changes
            db.session.commit()
            print("Database seeded successfully!")
        else:
            print("Database already contains data. Skipping seed.")

if __name__ == '__main__':
    seed_database()
