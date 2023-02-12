import email
from multiprocessing.util import info
from tabnanny import check
from init_file import app,db,param
from databases import Contacts, Follow,Users,Liketable,Post,Photos
import sendmail
import random
from datetime import datetime
from base64 import b64encode
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,session,redirect,Response

@app.route("/upload",methods=['GET','POST'])
def upload():
     if 'user' in session:
          if request.method=='POST':
               pic=request.files['pic']
               filename=secure_filename(pic.filename)
               mimetype=pic.mimetype
               check_exist_or_not=Photos.query.filter_by(email=session['email']).first()
               print(check_exist_or_not)
               if check_exist_or_not is None:
                    new_photo=Photos(email=session['email'],file=pic.read(),filename=filename,mimetype=mimetype)
                    db.session.add(new_photo)
                    db.session.commit()
               else:
                    check_exist_or_not.file=pic.read()
                    check_exist_or_not.filename=filename
                    check_exist_or_not.mimetype=mimetype
                    db.session.commit()

               return redirect("/profile")
          else:
               return render_template("profile.html")


@app.route("/profile/",methods=['GET','POST'])
def profile():
     if 'user' in session:
          edit_mode=request.args.get('editmode')
          if request.method=='POST':
               firstname=request.form.get('firstname')
               lastname=request.form.get('lastname')
               mobile=request.form.get('mobile')
               quote=request.form.get('quote')
               address=request.form.get('address')
               gender=request.form.get('gender')
               nationality=request.form.get('nationality')
               education=request.form.get('education')
               country=request.form.get('country')
               state=request.form.get('state')
               update_entry=Users.query.filter_by(email=session['email']).first()
               update_entry.firstname=firstname 
               update_entry.lastname=lastname
               
               if mobile !='None':
                    update_entry.mobile=mobile
               if quote !='None':
                    update_entry.quote=quote
               
               if address !='None':
                    update_entry.address=address
               if gender !='None':
                    update_entry.gender=gender
               if nationality !='None':
                    update_entry.nationality=nationality
               if education !='None':
                    update_entry.education=education
               if country !='None':
                    update_entry.country=country
               if state !='None':
                    update_entry.state=state
               db.session.commit()
               return redirect("/dummy")
          else:
               liked = Liketable.query.filter_by(likedby=session['email']).all()
               liked_post=[]
               for liked_sr in liked:
                    post = Post.query.filter_by(sr=liked_sr.postsr).first()
                    liked_post.append(post)

               photo=Photos.query.filter_by(email=session['email']).first()
               image="photo"
               if photo is not None:
                    image = b64encode(photo.file).decode("utf-8")
               user=Users.query.filter_by(email=session['email']).first()
               post=Post.query.filter_by(addedby=session['email']).all()
               following = Follow.query.filter_by(candidate=user.sr).all()
               followers = Follow.query.filter_by(following=user.sr).all()
               total_likes=0
               for pst in post:
                    total_likes+=len(Liketable.query.filter_by(postsr=pst.sr).all())
               info_dict={'total_likes':total_likes,'post':len(post),'following':following,'followers':followers}
               return render_template("profile.html",para=param,userinfo=session,liked=liked_post,session=session,image=image,user=user,edit_mode=edit_mode,info_dict=info_dict)
     else:
          return "<h1>Unauthorized<h1>"

@app.route("/dummy")
def dummy():
     return redirect("/profile")

@app.route("/profile/<string:user_>/")
def userprofile(user_):
     if 'user' in session:
          if user_==session['email']:
               return redirect("/profile/")
     photo=Photos.query.filter_by(email=user_).first()
     image="photo"
     if photo is not None:
          image = b64encode(photo.file).decode("utf-8")
     user=Users.query.filter_by(email=user_).first()
     post=Post.query.filter_by(addedby=user_).all()
     following = Follow.query.filter_by(candidate=user.sr).all()
     followers = Follow.query.filter_by(following=user.sr).all()
     followed_by ='None'
     if 'user' in session:
          check_follow =Follow.query.filter_by(candidate=Users.query.filter_by(email=session['email']).first().sr,following=user.sr).first()
          if check_follow is not None:
               followed_by="already_following"
          else:
               followed_by=session['email']
          
     total_likes=0
     for pst in post:
          total_likes+=len(Liketable.query.filter_by(postsr=pst.sr).all())
     info_dict={'total_likes':total_likes,'post':len(post),'following':following,'followers':followers,'followed_by':followed_by,'email':session['email']}

     return render_template('user_profile.html',para=param,image=image,user=user,info_dict=info_dict,post=post)

@app.route("/follow/<string:user_>/",methods=['GET','POST'])
def follow(user_):
     if 'user' in session:
          follow_email=request.args.get('follow')
          user_sr=Users.query.filter_by(email=user_).first().sr
          follow_sr=Users.query.filter_by(email=follow_email).first().sr
          exist=Follow.query.filter_by(candidate=user_sr,following=follow_sr).first()
          if exist is None:
               new_entry = Follow(candidate=user_sr,following = follow_sr)
               db.session.add(new_entry)
               db.session.commit()
          else:
               db.session.delete(exist)
               db.session.commit()

          return redirect("/profile/"+follow_email)
     else:
          return redirect("/login")