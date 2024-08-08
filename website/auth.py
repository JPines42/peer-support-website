# Import modules and database
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from .forms import RegistrationForm

auth = Blueprint("auth", __name__)

# Login page route


# When URL is '/login' and allowance for data submittion
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Get email and password from database
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            # Check if password is correct
            if check_password_hash(user.password, password):
                flash('Logged in successsfully!', category='success')
                login_user(user, remember=True)
                # If everything is correct return to Home page
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            # Check if email exists
            flash('Email does not exist.', category='error')

    # Return to Login page
    return render_template("login.html", user=current_user)

# Signup page route


# When URL is '/signup' and allowance for data submittion
@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        # If user already logged in return to Home page
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            (form.password.data), method='scrypt:32768:8:1')  # Make password encrypted
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()  # Adds new user to database with all information submitted
        flash('Account created!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.home'))  # Returns to Home page
    # Return to Signup page
    return render_template('signup.html', form=form, user=current_user)

# Logout page route


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')  # Log user out
    return redirect(url_for('views.home'))  # Return to Home page
