import smtplib
import json

with open("config.json","r") as c:
     msg = json.load(c)["email_cont"]

def send_mail(code,first_name,reciever_mail,verifie_=False):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("yourgamil","yourpassword")
        if verifie_:
          print("Verification mail sent")
          server.sendmail("yourgmail",reciever_mail,msg="Subject:Verification Code\n\n"+msg['emailmsg'].format(first_name,code))
        else:
          print("Reset mail sent")
          server.sendmail("yourgmail",reciever_mail,msg="Subject:Password Reset\n\n"+msg['resetmsg'].format(first_name,code))
        print("Mail sent")
