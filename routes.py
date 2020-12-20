from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from init import app, db
from forms import LoginForm, RegisterForm
from models import User, Post

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user.username
    posts = [
        {
            'author': {'username': 'Kate'},
            'title': 'Lorem Ipsum',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur iaculis mi sit amet ornare rutrum. Nunc nec justo viverra, pellentesque massa quis, sodales ante. Duis lobortis tortor justo, id aliquam neque efficitur eget. Fusce dictum metus sit amet sem pulvinar, ut molestie urna pulvinar. Sed quam tellus, placerat a bibendum vel, volutpat id augue.'
        }
    ]
    return render_template('articles.html', posts = posts, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

app.run()