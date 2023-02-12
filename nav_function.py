from init_file import app,db,param
from databases import Contacts,Users,Liketable,Post,Photos
import sendmail
import random
from datetime import datetime
from base64 import b64encode
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,session,redirect,Response

@app.route("/about")
def about():
     photo= None
     if 'user' in session:
          photo=Photos.query.filter_by(email=session['email']).first()
     image="photo"
     if photo is not None:
          image = b64encode(photo.file).decode("utf-8")
     return render_template("about.html",para=param,image=image)

@app.route("/contact", methods=['GET','POST'])
def contact():
     photo=None
     if 'user' in session:
          photo=Photos.query.filter_by(email=session['email']).first()
     image="photo"
     if photo is not None:
          image = b64encode(photo.file).decode("utf-8")
     if(request.method == 'GET'):
          return render_template("contact.html",para=param,image=image)
     if(request.method =='POST'):
          name=request.form.get("name")
          _email=request.form.get("email")
          phone=request.form.get("phone")
          messag=request.form.get("msg")
          entry=Contacts(name=name,phone_num=phone,msg=messag,date=datetime.now(),email=_email)
          db.session.add(entry)
          db.session.commit()
          return render_template("thankyou.html",para=param)