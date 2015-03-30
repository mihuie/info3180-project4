from . import db  


class Profiles(db.Model):         
    userid = db.Column(db.String(30), primary_key=True)
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80)) 
    username = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(10), unique=False)
    age = db.Column(db.Integer, unique=False)
    profile_add_on = db.Column(db.String(20), unique=False)    
    password = db.Column(db.String(16))
    highscore = db.Column(db.Integer, unique=False)
    image = db.Column(db.String(40), unique=False)
    tdollars = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50)) 
    status = db.Column(db.String(15)) 
    code = db.Column(db.String(30))
    
    def __init__(self, userid, first_name, last_name, username, password, email, age, gender, image, profile_add_on, highscore, tdollars, status, code):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.profile_add_on = profile_add_on
        self.highscore = highscore
        self.tdollars = tdollars
        self.userid = userid
        self.gender = gender
        self.image = image
        self.email = email
        self.status = status
        self.code = code
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<Profiles %r>' % (self.userid)