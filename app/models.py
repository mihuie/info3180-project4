from . import db  


class Profiles(db.Model):         
    userid = db.Column(db.String(30), primary_key=True)
    first_name = db.Column(db.String(80), unique=False)     
    last_name = db.Column(db.String(80), unique=False) 
    username = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(10), unique=False)
    age = db.Column(db.Integer, unique=False)
    profile_add_on = db.Column(db.String(20), unique=False)    
    password = db.Column(db.String(16), unique=False)
    highscore1 = db.Column(db.Integer, unique=False)
    highscore2 = db.Column(db.Integer, unique=False)
    image = db.Column(db.String(40), unique=False)
    tdollars = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50), unique=True) 
    active = db.Column(db.Boolean, default=False) 
    code = db.Column(db.String(30), unique=False)
    initial = db.Column(db.Boolean, default=True) 
    
    def __init__(self, userid, password, email, profile_add_on, code, highscore1, highscore2, tdollars, image):
        self.userid = userid
        self.password = password
        self.profile_add_on = profile_add_on
        self.email = email
        self.code = code
        self.highscore1 = highscore1
        self.highscore2 = highscore2
        self.tdollars = tdollars
        self.image = image
     
    
    def is_initial(self):
        return self.initial
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<Profiles %r>' % (self.userid)