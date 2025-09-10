from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from website.samples import *

auth = Blueprint('auth', __name__)


def create_session():
    session.permanent = True
    user = request.form["email"]
    session["user"] = user

    return redirect(url_for('auth.account'))


# login
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        valid, message = valid_login(email, password)

        if valid:
            create_session()
            return redirect(url_for('auth.account'))
        else:
            flash(message)

    return render_template("login.html")


# sign up
@auth.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")

        valid, message = valid_data([name, surname, email, password])

        if valid:
            create_user(name, surname, email, password)
            return create_session()
        else:
            flash(message)

    return render_template("sign_up.html")


# logout
@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop("user", None)

    return redirect(url_for('views.store'))


# account page
@auth.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        date = request.form.get("invest_date")
        cash = int(request.form.get("amount"))

        if check_valid_date(date):
            update_bank(session['user'], cash)
        else:
            flash("Invalid Date")

    return render_template("account.html", user_data=retrive_data(session['user']))