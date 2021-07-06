from flask_mongoengine import MongoEngine
from mongoengine.fields import DateTimeField, IntField, StringField, URLField, ReferenceField
from datetime import datetime

db = MongoEngine()


class User(db.Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    password = StringField(required=True)

class Post(db.Document):
    ''' Class for defining structure of reddit-top-posts collection
    '''
    date = DateTimeField(required=True, default=datetime.now())
    title = StringField(max_length=300, required=True) # title can be 300 chars
    content= StringField(max_length=10000, required=True)

    author = ReferenceField(User, dbref = False)

  

   
