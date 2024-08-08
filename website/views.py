# Import modules and database
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Faq
from . import db
import json

views = Blueprint("views", __name__)

# Home page route


@views.route("/")  # When URL is '/'
@views.route("/home")  # When URL is '/home'
def home():
    # Return to Home page
    return render_template("home.html", user=current_user)

# Sing and Dance page route


@views.route("/singdanceoff")  # When URL is '/singdanceoff'
def singdanceoff():
    # Return to Sing and Dance page
    return render_template("singdanceoff.html", user=current_user)

# Meet the Leaders page route


@views.route("/leaders")  # When URL is '/leaders'
def leaders():
    # Return to Meet the Leaders page
    return render_template("leaders.html", user=current_user)

# FAQ page route


# When URL is '/faq' and allowance for data submittion
@views.route("/faq", methods=['GET', 'POST'])
def faq():
    if request.method == 'POST':
        faq = request.form.get('faq')
        email = request.form.get('email')
        if len(email) < 1:
            # Flash error if email is less than 1 character
            flash('Email is invalid!', category='error')
        else:
            if len(faq) < 1:
                # Flash error if message is less than 1 character
                flash('Message is too short!', category='error')
            else:
                new_faq = Faq(data=faq, email=email)
                db.session.add(new_faq)
                db.session.commit()
                # Flash success if message is submitted
                flash('Message submitted!', category='success')

    return render_template("faq.html", user=current_user)  # Return to FAQ page

# Note page route


# When URL is '/notes' and allowance for data submittion
@views.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            # Flash error if note is less than 1 character
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            # Flash success if note is submitted
            flash('Note added!', category='success')

    # Return to Notes page
    return render_template("notes.html", user=current_user)

# Note deletion


@views.route('/delete-note', methods=['POST'])  # Allowance for data removal
def delete_note():
    note = json.loads(request.data)  # Grab note data from database
    noteId = note['noteId']
    note = Note.query.get(noteId)  # Link to existing note ID
    if note:
        if note.user_id == current_user.id:  # Check if note is connected to User's account
            db.session.delete(note)
            db.session.commit()
            # Flash success if note is deleted
            flash('Note deleted!', category='success')
    return jsonify({})

# Calendar page route


@views.route("/calendar")  # When URL is '/calendar'
@login_required
def calendar():
    # Return to Calendar page
    return render_template("calendar.html", user=current_user)
