from flask import Blueprint, render_template, redirect, url_for, flash, request
from application.database import User, db
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data  # (Important: in real apps, hash passwords!)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for('authentication.dashboard'))
    
    return render_template('registration.html', form=form)
