import sys
import time
import gmail
import flask
from secrets import *
import threading
from flask import Flask, url_for, render_template, redirect, session, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, static_url_path='/static')
mongo = MongoClient()

db = mongo.blog

'''def check_email():
	while True:
		g = gmail.login(GMAIL_USER, GMAIL_PASS)
		inbox = g.inbox().mail(unread=True, fr="devinmui@yahoo.com") # change email later
		if inbox:
			print inbox[0].fetch()
			sys.stdout.flush()
			inbox[0].read()
		else:
			print None
		g.logout()
		#time.sleep(300) # wait 5 minutes; you dont want all the server resources gone in the next minute

task = threading.Thread(target = check_email)
task.start()'''

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)