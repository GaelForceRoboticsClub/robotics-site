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

def check_email():
	while True:
		g = gmail.login(GMAIL_USER, GMAIL_PASS)
		inbox = g.inbox().mail(unread=True, fr=EMAIL_JUSTIN) # justin
		if inbox:
			inbox[0].fetch()
			subject = inbox[0].subject
			print subject
			body = inbox[0].body
			print body
			body = body.replace('\r', '<br/>').replace('\n', '<br/>')
			json = { "title": subject, "body": body }
			db.posts.insert_one(json)
			inbox[0].read()
		inbox = g.inbox().mail(unread=True, fr=EMAIL_TIM) # tim
		if inbox:
			inbox[0].fetch()
			subject = inbox[0].subject
			print subject
			body = inbox[0].body
			print body
			body = body.replace('\r', '<br/>').replace('\n', '<br/>')
			json = { "title": subject, "body": body }
			db.posts.insert_one(json)
			inbox[0].read()
		g.logout()
		time.sleep(600) # wait 10 minutes; you dont want all the server resources gone in the next minute

task = threading.Thread(target = check_email)
task.start()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/blog')
def blog():
	posts = db.posts.find({})
	return render_template('blog.html', posts=posts)

@app.route('/blog/posts/<post_id>')
def posts(post_id):
	post_id = ObjectId(post_id)
	post = db.posts.find_one({"_id": post_id })
	return render_template('post.html', post=post)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)