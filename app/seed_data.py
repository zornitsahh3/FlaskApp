#create sample data for the app

from app import create_app
from app.models import db,User,Post,Task,Product #this app.models is created from me
from datetime import datetime,imedata
import random

def seed_database():
    app=create_app()

    with app.app_context():
        print("clearing existing data")
        db.drop_all()
        db.create_all()

        print("Creating sample users:")
        users=[]
        for i in range(1,6):
            user=User(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password_hash=f'hashed_password_{i}'
            )
            users.append(user)
            db.session.add(user)
        
        db.session.commit()
        print("created the users")