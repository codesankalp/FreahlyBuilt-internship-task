
# importing libraries 
from flask import Flask,render_template 
from flask_mail import Mail, Message
import sys 
   
app = Flask(__name__) 
mail = Mail(app)
# mail.init_app(app)

admin_mail = 'sankalp123427@gmail.com'
password = 'Lalitasankalp'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = admin_mail
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# mail.init_app(app)


enquirer = sys.argv[1]
subject = sys.argv[2]
message_to_send = sys.argv[3]
  
# message object mapped to a particular URL ‘/’ 
@app.route("/") 
def index(): 
   msg = Message( 
                subject, 
                sender = enquirer, 
                recipients = [admin_mail] 
               ) 
   msg.body = message_to_send
   mail.send(msg) 
   return render_template('thanks.html')
   
if __name__ == '__main__': 
   app.run(debug = True) 