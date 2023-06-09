#!/usr/bin/python3
from flask import Flask, jsonify, render_template
from models.contact import Contact
from models import storage


app = Flask(__name__)

@app.route("/") 
def hello():
    contacts = storage.all()
    contacts_data = [{'id': details.id, 'name': details.first_name, 'skill':details.specialization,
        'employer': details.employer, 'location': details.location} 
            for contact, details in contacts.items()]
    k = contacts_data
    return render_template("home.html", k = k)

@app.route('/contact', strict_slashes=False)
def all_contacts():
    contacts = storage.all()
    contacts_data = [{'id': details.id, 'name': details.first_name, 'skill':details.specialization} for contact, details in contacts.items()]
    return jsonify(contacts_data)

@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
