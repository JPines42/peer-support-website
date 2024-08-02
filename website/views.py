from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Faq
from . import db
import json

views = Blueprint("views", __name__)

#Home page route
@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", user=current_user)

#Sing and Dance page route
@views.route("/singdanceoff")
def singdanceoff():
    return render_template("singdanceoff.html", user=current_user)

#Meet the Leaders page route
@views.route("/leaders")
def leaders():
    return render_template("leaders.html", user=current_user)

#FAQ page route
@views.route("/faq", methods=['GET', 'POST'])
def faq():
    if request.method == 'POST':
        faq = request.form.get('faq')
        email = request.form.get('email')
        if len(faq) < 1:
            flash('Message is too short!', category='error')
        else:
            new_faq = Faq(data=faq, email=email)
            db.session.add(new_faq)
            db.session.commit()
            flash('Message submitted!', category='success')

    return render_template("faq.html", user=current_user)

#Note page route
@views.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)

#Note deletion
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!', category='success')
    return jsonify({})

#Calendar page route
@views.route("/calendar")
@login_required
def calendar():
    return render_template("calendar.html", user=current_user)
