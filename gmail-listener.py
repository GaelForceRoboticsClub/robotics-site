import sys
import time
import gmail
from secrets import *
import threading
from pymongo import MongoClient
from bson.objectid import ObjectId

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
# this should be an external script
task = threading.Thread(target = check_email)
task.start()
