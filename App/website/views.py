from flask import Blueprint, render_template, session

views = Blueprint('views', __name__)

@views.route('/')
def store():
    return render_template("store.html", logged=("user" in session))


@views.route('/about_us')
def about_us():
    return render_template("about_us.html", logged=("user" in session))