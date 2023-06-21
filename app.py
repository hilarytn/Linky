#!/usr/bin/python3
from flask import Flask, jsonify, render_template, url_for, request, redirect
from models.contact import Contact
from models import storage
import copy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/") 
def hello():
    contacts = storage.all()
    contacts_data = [{'id': details.id, 'name': details.first_name, 'skill':details.specialization,
        'employer': details.employer, 'location': details.location} 
            for contact, details in contacts.items()]
    k = contacts_data
    return render_template("home.html", k = k)

@app.route('/contact', strict_slashes=False, methods=['POST'])
def all_contacts():
    contacts = storage.all()
    contacts_data = [{'id': details.id, 'name': details.first_name, 'skill':details.specialization,
        'employer': details.employer, 'location': details.location} 
            for contact, details in contacts.items()]
    k = contacts_data
    return render_template("form.html", k=k)

@app.route('/create-contact', methods=['POST'], strict_slashes=False)
def create_contact():
    if request.method == 'POST':
        first_name = request.form.get('name')
        location = request.form.get('description')
        specialization = request.form.get('price')
        employer = request.form.get('category')
        picture = request.files['picture']
        

    if first_name and location and specialization and employer and picture:
        new_contact = Contact(first_name=first_name, location=location, specialization=specialization, employer=employer)#, image_url=picture_data)
        filename = new_contact.id + '.jpg'
        picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        storage.new(new_contact)
        storage.save()
	
        return redirect(url_for('hello'))
    else:
        return "Please provide all the required information for creating a contact. Don't forget to upload a jpg picture format"


@app.route('/delete-contact/<contact_id>', methods=['POST', 'GET'], strict_slashes=False)
def delete_contact(contact_id):
    # Helper method to delete a contact
    contact = storage.get("Contact", contact_id)
    storage.delete(contact)
    storage.save()
    if contact:
        # Perform the delete operation
        
        return redirect(url_for('hello'))

@app.route('/update-contact/<contact_id>', methods=['GET', 'POST'], strict_slashes=False)
def update_contact(contact_id):
    contact = storage.get("Contact", contact_id)
    if request.method == 'GET':
        return render_template("form.html", contact=contact)

    if request.method == 'POST':
        # Handle form submission and update the contact
        # Retrieve form data and update the contact object
        first_name_form = request.form.get('name')
        location_form = request.form.get('description')
        specialization_form = request.form.get('price')
        employer_form = request.form.get('category')
        picture = request.files['picture']
        #employer = request.form.get('category')

        if contact.id == contact_id:
            if first_name_form:
                contact.first_name = first_name_form
            else:
                contact.first_name = contact.first_name
            if location_form:
                contact.location = location_form
            else:
                contact.location = contact.location
            if specialization_form:
                contact.specialization = specialization_form
            else:
                contact.specialization = contact.specialization
            if employer_form:
                contact.employer = employer_form
            else:
                contact.employer = contact.employer
            if picture:
                filename = contact.id + '.jpg'
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            storage.save()

            return redirect(url_for('hello'))
        else:
            print("Not found")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)

