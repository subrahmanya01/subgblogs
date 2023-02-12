from init_file import app,db,param
from databases import Contacts,Users,Liketable,Post,Photos
import sendmail
import random
from authlib.integrations.flask_client import OAuth

from flask import Flask, render_template,request,session,redirect,Response,url_for,jsonify


oauth = OAuth(app)

app.config["GOOGLE_CLIENT_ID"]="335956238089-gmk0bcuffhrutie3ek6kkujm0l0i6ejf.apps.googleusercontent.com"
app.config["GOOGLE_CLIENT_SECRET"]= "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"
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

google = oauth.register(
    name='google',  # This is only needed if using openId to fetch user info
    server_metadata_url=CONF_URL,
    client_kwargs = {'scope': 'openid email profile'},
)
@app.route("/login/google")
def loginwithgoogle():
    redirect_uri = url_for('googleauthorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/login/google/authorize")
def googleauthorize():
    token = oauth.google.authorize_access_token()
    session['google_sign'] = token['userinfo']
    
    return jsonify(session['google_sign'])


@app.route("/login", methods=['GET','POST'])
def login():
     if request.method == 'POST':
          user_name = request.form.get("email")
          passward = request.form.get("password")
          new_user = Users.query.filter_by(email=user_name).first()
          if new_user is None:
               return redirect("/login")

          if(passward == new_user.password):
               session['email']=user_name
               user_name=Users.query.filter_by(email=user_name).first()
               session["user"]=user_name.lastname
               session['email']=user_name.email
               session['first_name']=user_name.firstname
               current_user = user_name
               return redirect("/")
          else:
               return redirect("/login")
     if "user" not in session:
          return render_template("login.html",para=param)
     else:
          return redirect("/")

@app.route("/signup",methods=['GET','POST'])
def signup():
     if 'user' not in session:
          if request.method == 'POST':
               session['first_name']=request.form.get("firstname")
               session['last_name']=request.form.get("lastname")
               session['email']=request.form.get("email")
               session['password']=request.form.get("password")
               session['verification']=random.randint(1000,999999)
               session['gotoverifie']=True
               sendmail.send_mail(session['verification'],session['first_name'],session['email'],verifie_=True)
               print(session['verification'])
               return render_template("verifie.html",para=param,mail=session['email'])
               
          else:
               return render_template("register.html",para=param)
     else:
          return redirect("/login")

@app.route("/logout")
def logout():
     del session['user']
     return redirect("/login")


@app.route("/forgot", methods=['GET','POST'])
def forgot():
     if 'user' not in session:
          if request.method == 'POST':
               e_mail=session['email']=request.form.get("email")
               session['password']=request.form.get("password")
               user_ =Users.query.filter_by(email=e_mail).first()
               session['first_name']=user_.firstname
               session['verification']=random.randint(1000,999999)
               session['gotoverifie']=True
               session['forgot']=True
               sendmail.send_mail(session['verification'],session['first_name'],session['email'])
               return redirect("/verifie")
          else:
               return render_template("forgot_password.html",para=param)