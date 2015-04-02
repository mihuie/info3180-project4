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
from forms import CreateUserForm, LoginForm, EditForm
from flask import jsonify
from flask import session
from werkzeug import secure_filename

import time
from mailscript import * 

UPLOAD_FOLDER = 'app/static/img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#my misc functions  
def timeinfo():
    return time.strftime("%a, %d %b %Y")
  
def createID():
    return time.strftime("%y%j%H%M%S")
  
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
 
@app.route('/signup/', methods=['POST','GET'])
def signup():
    form = CreateUserForm()
    if request.method == 'POST' and form.validate():
        #generate user id
        userid = createID()
        
        #gets today's date
        profile_add_on = timeinfo()
        
        #creating confirmaton code
        ccode = form.email.data[:3]+userid
        
        # Saving profile to database and setting to inactive
        user = Profiles(userid=userid, password=form.password.data, email=form.email.data, \
                        profile_add_on=profile_add_on, code=ccode, highscore=0, tdollars=0)
              
        db.session.add(user)
        db.session.commit()
        
        # sending confirmation email
        sendcode(form.email.data, ccode)
        
        flash('Please complete registration by verifying your email')
        return render_template('signup.html', form=form)
    else:
        return render_template('signup.html', form=form)
    
    
    
@app.route('/signup/confirm/<confirmcode>/', methods=['GET'])
def confirm(confirmcode):
    if (Profiles.query.filter_by(code = confirmcode).first() is None):
        return redirect(url_for('page_not_found'))
    else:
        user = Profiles.query.filter_by(code = confirmcode).first()
        user.active = True
        db.session.commit()
        return  render_template('confirm.html')


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        db_user = Profiles.query.filter(Profiles.email == form.email.data).first()
        if (db_user is None):
          flash("Email/Password combination not found")
          return render_template("login.html", form=form)
        if (not(db_user.is_active())):
          flash("Please confirm your email address")
          return render_template("login.html", form=form)        
        if not(db_user.password == form.password.data):
          flash("username and password doesn't match")
          return render_template("login.html", form=form)
        
        user = load_user(db_user.userid)
        login_user(user)
        
        if (db_user.is_initial()):
          return redirect(url_for("update"))
        else:
          return redirect(url_for("games"))
    return render_template("login.html", form=form)
  
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
  
@app.route('/profile/')
@login_required
def profile():
    user = Profiles.query.filter_by(userid=current_user.get_id()).first_or_404()
    if (user.is_initial()):
#       flash('Update your profile first')
      return redirect(url_for("update"))
    else:
      return render_template('profile.html', user=user, filename = user.image)
  
@app.route('/profile/update/', methods =['GET','POST'])
@login_required
def update():
    user = Profiles.query.filter_by(userid=current_user.get_id()).first_or_404()
    form = EditForm(obj=user)
    form.populate_obj(user)
    
    if request.method == "POST" and form.validate():
      
#       if form.image.data.filename:
      extn = (form.image.data.filename).rsplit('.', 1)[1]#grabbing file extension
      filename = secure_filename(user.userid +'.'+ extn)#renaming pic as user id
      form.image.data.save(UPLOAD_FOLDER + filename)
      
      user.image = 'img/' + filename
      user.username = form.username.data
      user.first_name = (form.first_name.data).title()
      user.last_name = (form.last_name.data).title()
      user.age = form.age.data
      user.gender = form.gender.data      
      user.initial = False
      db.session.commit()
      flash('Profile updated')
      return redirect(url_for('profile'))
    
    return render_template('update.html', form=form)
  
  
@app.route('/profiles/')
@login_required
def profiles():
  users = Profiles.query.all()
  return render_template('profiles.html', users=users)

@app.route('/games/')
def games():
    return render_template('games.html')

@app.route('/game/<gameid>', methods=['GET'])
@login_required
def game(gameid):
    if not (request.method == 'GET'):
        return render_template('404.html')
    if gameid == '1':
       return render_template('platformer.html')
    elif gameid == '2':
       return render_template('spaceinv.html')
      

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
