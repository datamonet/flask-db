from app import app, db, Student

def seed_database():
    # Sample student data
    students = [
        {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'},
        {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com'},
        {'first_name': 'Michael', 'last_name': 'Johnson', 'email': 'michael.johnson@example.com'},
        {'first_name': 'Emily', 'last_name': 'Brown', 'email': 'emily.brown@example.com'},
        {'first_name': 'David', 'last_name': 'Wilson', 'email': 'david.wilson@example.com'},
        {'first_name': 'Sarah', 'last_name': 'Davis', 'email': 'sarah.davis@example.com'},
        {'first_name': 'James', 'last_name': 'Miller', 'email': 'james.miller@example.com'},
        {'first_name': 'Emma', 'last_name': 'Taylor', 'email': 'emma.taylor@example.com'},
        {'first_name': 'William', 'last_name': 'Anderson', 'email': 'william.anderson@example.com'},
        {'first_name': 'Olivia', 'last_name': 'Thomas', 'email': 'olivia.thomas@example.com'}
    ]

    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Add all students
        for student_data in students:
            student = Student(**student_data)
            db.session.add(student)
        
        # Commit the changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
