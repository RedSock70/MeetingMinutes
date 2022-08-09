from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 Characters.', category='error')
        elif len(FirstName) < 2:
            flash('First name must be greater than 1 Characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 7 Characters.', category='error')
        else:
            flash('Account Created!', category='success')
            
            # add user to database 
            return render_template("sign_up.html")