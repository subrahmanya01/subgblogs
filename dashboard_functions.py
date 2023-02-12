from init_file import app,db,param
from databases import Contacts,Users,Liketable,Post,Photos
import sendmail
import random
from datetime import datetime
from base64 import b64encode
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,session,redirect,Response


@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
          if "user" in session :
               post=Post.query.filter_by(addedby=session['email']).all()
               photo=Photos.query.filter_by(email=session['email']).first()
               image="photo"
               if photo is not None:
                    image = b64encode(photo.file).decode("utf-8")
               print(post)
               if len(post)==0:
                    return render_template("dashboard.html",para=param,post='None',userinfo=session,image=image)
               else:
                    return render_template("dashboard.html",para=param,post=post,userinfo=session,image=image)
          else:
               return redirect("/login")

@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
     if 'user' in session:
          post=Post.query.filter_by(sr=sno).first()
          liked = Liketable.query.filter_by(postsr=sno).all()
          for row in liked:
               db.session.delete(row)
               db.session.commit()
          db.session.delete(post)
          db.session.commit()
          return redirect("/dashboard")
     else:
          return "<h1> Not Authorized</h1>"


@app.route("/edit/<string:sno>", methods=['GET','POST'])
def edit(sno):
     if 'user' in session:
          photo=Photos.query.filter_by(email=session['email']).first()
          image="photo"
          if photo is not None:
               image = b64encode(photo.file).decode("utf-8")

          if request.method =='POST':
               slg=request.form.get("slug")
               ttl=request.form.get("Title")
               subttl=request.form.get("subtitle")
               tileimg=request.files["Tileimage"]
               cont=request.form.get("content")

               if(tileimg is None):
                    tileimg.filename = "__.png"
                    tileimg="temp"
               
               if sno=='0':
                    post=Post(slug=slg,title=ttl,subtitle=subttl,content=cont,date=datetime.now(),addedby=session['email'],tileimg=tileimg.filename)
                    if(tileimg.filename != "__.png") and tileimg=="temp":
                         tileimg.save('./static/uploads/'+secure_filename(tileimg.filename))
                    db.session.add(post)
                    db.session.commit()
               else:
                    post = Post.query.filter_by(sr=sno).first()
                    post.slug =slg
                    post.title = ttl  
                    post.subtitle= subttl
                    post.content = cont
                    post.tileimg = tileimg.filename
                    if tileimg.filename != "__.png":
                         tileimg.save('./static/uploads/'+secure_filename(tileimg.filename))
                    db.session.commit()
               return redirect("/dashboard")
          else:
               if sno == '0':
                    post=Post.query.filter_by(sr=sno).first()
                    return render_template("addpost.html", para=param,post=post,userinfo=session,image=image)
               else:
                    post=Post.query.filter_by(sr=sno).first()
                    if post is not None:
                         if post.addedby == session['email']:
                              return render_template("edit.html", para=param,post=post,userinfo=session,image=image)
                         else:
                              return "Not authorized"
                    else: 
                         return redirect("/dashboard")
                    
     else:
          return redirect('/login')