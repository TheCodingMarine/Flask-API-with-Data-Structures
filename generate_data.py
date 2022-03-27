from random import randrange
from  sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from faker import Faker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import User, BlogPost
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" +os.path.join(basedir,
                                        "flask-api-ds-tutorial.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@event.listens_for(Engine, 'connect')
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON;')
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()

faker = Faker()

for i in range(200):
    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'
    new_user = User(name=name, address=address, phone=phone, 
        email=email)
    db.session.add(new_user)
    db.session.commit()

for i in range(200):
    title = faker.sentence(5)
    body = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 200)

    new_blog_post = BlogPost(
        title=title, body=body, date=date, user_id=user_id
    )
    db.session.add(new_blog_post)
    db.session.commit()
