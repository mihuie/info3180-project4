"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import db
from app import app

from app import login_man
from flask.ext.login import login_user, logout_user, current_user, login_required

from flask import render_template, request, redirect, url_for, flash
from app.models import Profiles
from forms import CreateUserForm, LoginForm
from flask import jsonify
from flask import session


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
  
@login_man.user_loader
def load_user(id):
    return Profiles.query.get(id)

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        db_user = Profiles.query.filter(Profiles.username == form.username.data).first()
        if (db_user is None):
          flash("username and password doesn't match")
          return render_template("login.html", form=form)
        
        if not(db_user.password == form.password.data):
          flash("username and password doesn't match")
          return render_template("login.html", form=form)
        
        user = load_user(db_user.id)
        login_user(user)
        return redirect(request.args.get("next") or url_for("home"))
    return render_template("login.html", form=form)
 
@app.route('/signup/', methods=['POST','GET'])
def signup():
    form = CreateUserForm()
    if request.method == 'POST' and form.validate():
        user = Profiles((form.first_name.data).title(), (form.last_name.data).title(), form.username.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', form=form)   
 
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
