"""
from flask import Flask, render_template, request
from flask_mail import Mail, Message
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=456
app.config['MAIL_USERNAME']='samhitavoudattou95@gmail.com'
app.config['MAIL_PASSWORD']=''
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = body

    mail.send(msg)
    
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = body

    mail.send(msg)
    
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        msg=Message("yo soy el metal", sender='noreply@demo.com', recipients='samhitavoudattou95@gmail.com')
        msg.body="jerghuwrkhgukerhguehfu ahahhahahahha"
        mail.send(msg)
    return "sent email :3"
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
    """


from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'samhitavoudattou95@gmail.com'
app.config['MAIL_PASSWORD'] = 'cpjc yezs tlel hlzb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('visitorID.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = body

    mail.send(msg)
    
    return 'Email sent successfully!'

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = Message("Test email", sender='noreply@demo.com', recipients=['samhitavoudattou95@gmail.com'])
        msg.body = "This is a test email."
        mail.send(msg)
        return "Sent email."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['POST'])
def root_post(): 
    return "Received POST request at root URL"
# Handle POST requests to the root URL here