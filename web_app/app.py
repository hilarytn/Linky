#!/usr/bin/python3
from flask import Flask
from models.contact import Contact
from models import storage


app = Flask(__name__)

@app.route("/") 
def hello():
    return "Hello World!";

@app.route('/contact', strict_slashes=False)
def all_contacts():
    objects = storage.all(Contact)
    return objects
    
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
