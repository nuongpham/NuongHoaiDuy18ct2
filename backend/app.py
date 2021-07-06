from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from models import db, Post, User
import json
app = Flask(__name__)

# connect to db
app.config["MONGODB_HOST"] = "mongodb://localhost:27017/myDatabase"
app.debug = True

# initalize app with database
db.init_app(app)

CORS(app)

@app.route("/user/", methods= ["GET","POST"])
def get_post_user_api():
    if request.method == "GET":
        return jsonify(User.objects)
    if request.method == "POST":
        try:
            new_user = User(email=request.json["email"], first_name=request.json["first_name"], last_name=request.json["last_name"], password=request.json["password"]).save()
            return jsonify(new_user)
        except:
            return jsonify({ "message": "please input full field" })

@app.route("/user/<id>", methods= ["DELETE", "PUT"])
def del_user_api(id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return jsonify({ "message": "deleted" })
        except:
            return jsonify({ "message": "user is not in db" })
    
    elif request.method == "PUT":
        try:

            user = User.objects.get(id=id)
            json_data = request.json
            
            for data in json_data:
                user[data] = json_data[data] if json_data[data] != "" else user[data]
            user.save()

            return jsonify({ "message": "updated" })
        except:
            return jsonify({ "message": "user is not in db" })




@app.route("/post/", methods= ["GET", "POST"])
def get_post_post_api():
    if request.method == "GET":
        response = list()
        for post in Post.objects:
            response.append({"id":str(ObjectId(post.id)), "author":  post['author'].first_name + " " + post['author'].last_name ,"content": post.content, "title": post.title, "date": post.date })
        return jsonify(response)
    elif request.method == "POST":
        try:
            author = User.objects.get(id=request.json['id_author'])
            new_post = Post(title=request.json["title"], content=request.json["content"], author=author).save()
            return jsonify(new_post)
        except:
            return jsonify({ "message": "please input full field or not valid id_author" })


@app.route('/post/<id>', methods=["DELETE", "PUT", "GET"])
def del_post_api(id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=id)
            return jsonify({"id":str(ObjectId(post.id)), "author":  post['author'].first_name + " " + post['author'].last_name ,"content": post.content, "title": post.title, "date": post.date }) 
        except:
            return jsonify({ "message": "post is not in db" })

    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return jsonify({ "message": "deleted" }) 
        except:
            return jsonify({ "message": "post is not in db" })

    elif request.method == "PUT":
        try:

            post = Post.objects.get(id=id)
            json_data = request.json
            for data in json_data:
                post[data] = json_data[data] if json_data[data] != "" else post[data]
            post.save()

            return jsonify({ "message": "updated" })
        except:
            return jsonify({ "message": "user is not in db" })

