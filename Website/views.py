from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        info = request.form.get('info')
        subject = request.form.get('subject')
        absents = request.form.get('absents')
        raisedby = request.form.get('raisedby')
        actions = request.form.get('actions')
        tobea = request.form.get('tobea')
        subsequent = request.form.get('subsequent')
        completion = request.form.get('completion')




        if len(info) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=info, user_id=current_user.id, subject=subject, absents=absents, raisedby=raisedby, actions=actions, tobea=tobea, subsequent=subsequent, completion=completion)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})