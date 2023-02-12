from init_file import app,db,param
from databases import Contacts,Users,Liketable,Post,Photos
import sendmail
import random
from datetime import datetime
from base64 import b64encode
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,session,redirect,Response

@app.route("/verifie",methods=['GET','POST'])
def verifie():
     if 'gotoverifie' in session:
          if request.method =='POST':
               verification_code = request.form.get("verificationcode")
               if 'forgot' not in session:
                    if(str(session['verification'])==verification_code):
                         new_user = Users(firstname=session['first_name'],lastname=session['last_name'],email=session['email'],password=session['password'])
                         db.session.add(new_user)
                         db.session.commit()
                         del session['gotoverifie']
                         del session['verification']
                         del session['password']
                         return redirect("/login")
                    else:
                         return redirect("/verifie")
               else:
                    if(str(session['verification'])==verification_code):
                         user=Users.query.filter_by(email=session['email']).first()
                         user.password=session['password']
                         db.session.commit()
                         del session['gotoverifie']
                         del session['verification']
                         del session['password']
                         del session['forgot']
                         return redirect("/login")

          else:
               print(session['verification'])
               return render_template("verifie.html",para=param,mail=session['email'])
     else:
          return redirect("/login")
          