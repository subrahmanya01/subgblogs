from init_file import app,db,param
from databases import Contacts,Users,Liketable,Post,Photos
import sendmail
import random
from datetime import datetime
from base64 import b64encode
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,session,redirect,Response,jsonify

@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
     photo=None
     if 'user' in session:
          photo=Photos.query.filter_by(email=session['email']).first()
     image="photo"
     if photo is not None:
          image = b64encode(photo.file).decode("utf-8")
     post=Post.query.filter_by(slug=post_slug).first()
     
     userinfo=Users.query.filter_by(email=post.addedby).first()
     check_query=Liketable.query.filter_by(postsr=post.sr,likedby=session['email']).first()
     liked=True
     if check_query is None:
          liked=False
     likes=len(Liketable.query.filter_by(postsr=post.sr).all())

     if 'user' not in session:
          liked=False
     return render_template("post.html",para=param,post=post,userinfo=userinfo,likes=likes,liked=liked,image=image)

@app.route("/liked", methods=['GET'])
def liked():
    if 'user' in session:
          sr=request.args.get('sr')
          sl=request.args.get('slug')
          check_query=Liketable.query.filter_by(postsr=sr,likedby=session['email']).first()
          liked=True
          if check_query is None:
               new_like = Liketable(likedby=session['email'],postsr=sr)
               db.session.add(new_like)
               db.session.commit()
          else:
               db.session.delete(check_query)
               db.session.commit()
               liked=False
          post=Post.query.filter_by(slug=sl).first()
          likecnt=len(Liketable.query.filter_by(postsr=post.sr).all())

          return jsonify({'liked':liked,'likecnt':likecnt})
          
          #return redirect("/post/"+sl)
    else:
          redirect_url ='/login'
          return jsonify({'redirect':redirect_url })