### Description

The new and updated robotics website running on Python Flask, MongoDB, and Javascript. Features a simple CMS through email system where you can email x to post on the site (admins only).

### Dependencies

* Python 2.7
* Flask
* MongoDB
* PyMongo
* ObjectId BSON

### Running

1. Make sure you have the dependencies
2. Setting up Mongo: run `mongod`
3. Setting up the server: make file `secrets.py` with variables `GMAIL_USER` and `GMAIL_PASS` and fill with listener gmail account credentials. Also fill EMAIL_JUSTIN and EMAIL_TIM with an email each
4. Run the server! `python server.py`

### If you're admin

Sending an email to the listener email account will cause a Python thread to create a new post and save it into the MongoDB database. Simple! But only if you're admin and that the message is unread.

Initial email: kthanksforlettingmeknow@gmail.com
