import sys
import time
import gmail
import flask
from secrets import *
import threading
from flask import Flask, url_for, render_template, redirect, session, request, Markup
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, static_url_path='/static')
mongo = MongoClient()

db = mongo.blog

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/checkin')
def checkin():
	return render_template('checkin.html')

@app.route('/blog')
def blog():
	posts = db.posts.find({})
	return render_template('blog.html', posts=posts)

@app.route('/blog/posts/<post_id>')
def posts(post_id):
	post_id = ObjectId(post_id)
	post = db.posts.find_one({"_id": post_id })
	return render_template('post.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
	app.run(host="0.0.0.0")
