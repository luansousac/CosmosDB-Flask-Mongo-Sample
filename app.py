from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "TODO with Flask"
heading = "ToDo Reminder"

client = MongoClient(os.getenv("MONGOURL"))
db = client['SigaData']
db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))
todos = db['User']

@app.route("/")
def tasks():
	return 'Teste'

wsgi_app = app.wsgi_app

if __name__ == "__main__":
    app.run()