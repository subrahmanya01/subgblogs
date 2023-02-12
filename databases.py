from init_file import db

class Photos(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False)
    file = db.Column(db.Text, unique=False)
    filename= db.Column(db.String(120), unique=False)
    mimetype = db.Column(db.String(120), unique=False)

class Contacts(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    phone_num = db.Column(db.String(120), unique=False)
    msg = db.Column(db.String(120), unique=False)
    date = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), unique=False)


class Post(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=False)
    title = db.Column(db.String(120), unique=False)
    subtitle = db.Column(db.String(120), unique=False)
    content = db.Column(db.String(1200), unique=False)
    date = db.Column(db.String(120), unique=False)
    addedby= db.Column(db.String(120), unique=False)
    tileimg= db.Column(db.String(120), unique=False)
    

class Users(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False)
    lastname = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(1200), unique=False)
    password = db.Column(db.String(120), unique=False)
    quote = db.Column(db.String(120), unique=False)
    address = db.Column(db.String(120), unique=False)
    gender = db.Column(db.String(120), unique=False)
    mobile = db.Column(db.Integer, unique=True)
    nationality = db.Column(db.String(120), unique=False)
    country = db.Column(db.String(120), unique=False)
    state = db.Column(db.String(120), unique=False)
    education = db.Column(db.String(120), unique=False)

class Liketable(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    likedby = db.Column(db.String(80), unique=False)
    postsr = db.Column(db.Integer, unique=False)

class Follow(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    candidate = db.Column(db.Integer, unique=False)
    following = db.Column(db.Integer, unique=False)

