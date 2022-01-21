from flask import render_template, redirect, url_for, request
from app import app
from app import db
from flask_login import current_user, login_user, logout_user
from app.models import User


#   The app redirects straight to the login page if user did not log in.
@app.route('/')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        with db.session() as cursor:
            result = cursor.execute("SELECT * FROM \"public\".\"user\"").fetchall()
        return render_template('list.html', title='Users — User Management', user=current_user,
                               result=result)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/add-user", methods=['GET', 'POST'])
def add_user():
    error = None
    if request.method == 'POST':
        check = False
        if request.form.getlist('checkbox'):
            check = True
        if not request.form['username'].isalnum():
            error = 'Username must contain letters and/or digits only.'
            return render_template('add_user.html', title='Add User — User Management', error=error, user=current_user)
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None:
            user = User(username=request.form['username'], is_superuser=check)
            user.set_password(request.form['password'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            error = 'Username must be unique.'
            return render_template('add_user.html', title='Add User — User Management', error=error, user=current_user)
    if current_user.is_superuser:
        return render_template('add_user.html', title='Add User — User Management', error=error, user=current_user)
    else:
        return redirect(url_for('home'))


@app.route('/delete/<username>')
def delete(username):
    if current_user.is_superuser:
        with db.session() as cursor:
            cursor.execute(f"DELETE FROM \"public\".\"user\" WHERE username='{username}'")
            cursor.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/edit/<username>', methods=['GET', 'POST'])
def edit(username):
    if current_user.is_superuser:
        if request.method == 'POST':
            user = User.query.filter_by(username=username).first()
            if request.form.getlist('namecheck'):
                user.username = request.form['username']
            if request.form.getlist('passwordcheck'):
                user.set_password(request.form['password'])
            if request.form.getlist('checkbox'):
                user.is_superuser = True
            else:
                user.is_superuser = False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('edit_user.html', title='Edit User — User Management', username=username, user=current_user)
    else:
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', title='Login — User Management', error=error)
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', title='Login — User Management', error=error)
