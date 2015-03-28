from . import db  


class Profiles(db.Model):         
    id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80)) 
    username = db.Column(db.String(80), unique=True) 
    password = db.Column(db.String(16))
    
    def __init__(self, first_name, last_name, username, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Profiles %r>' % (self.username)