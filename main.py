
import email
from email.mime import image
from enum import unique
from importlib.metadata import requires
import mimetypes
from flask import Flask, render_template,request,session,redirect,Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import random
import sendmail
import math
from html.parser import HTMLParser
import os
from base64 import b64encode
from werkzeug.utils import secure_filename
from init_file import app,db,param
from authlib.integrations.flask_client import OAuth
from databases import Contacts,Users,Liketable,Post,Photos
import login_activity
import nav_function
import verification
import profile_functions
import post_view_functions
import dashboard_functions


prev=""
next=""
image="photo"

@app.route("/", methods=['GET','POST'])
def home():
     searched =[]
     post=Post.query.filter_by().all()
     post.reverse()
     photo=None
     if 'user' in session:
          photo=Photos.query.filter_by(email=session['email']).first()
     image="photo"
     if photo is not None:
          image = b64encode(photo.file).decode("utf-8")

     if request.method =='POST':
          search_key = request.form.get("searchid")
          post_included_key =[]
          for pst in post:
               if search_key in pst.title or search_key in pst.subtitle:
                    post_included_key.append(pst)
          post =post_included_key
          searched=[search_key]
     
     
     last = math.floor(len(post)/int(param['no_of_posts_per_page']))
     page = request.args.get("page")
     
     print(page)
     if not str(page).isnumeric() or page is None:
          page =0
     page=int(page)
     post = post[page*param['no_of_posts_per_page']:page*param['no_of_posts_per_page']+param['no_of_posts_per_page']]
     if(page == 0):
          prev = "#"
          if page ==last:
               next="#"
          else:
               next = "/?page="+str(page+1)    
         
     elif page ==last:
          next = "#"
          prev = "/?page="+str(page-1)
     else:
          prev = "/?page="+str(page-1)
          next = "/?page="+str(page+1)
          
    


     return render_template("index.html",para=param,post=post,userinfo=session,prev=prev,next=next,image=image,searched=searched)

@app.route("/clearsession")
def clearsession():
     session.clear()
     return redirect("/login")




app.run(debug=True)