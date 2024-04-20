"""from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('visitorID.html')

@app.route('/visitorID.html', methods=['POST'])
def register():
    name = request.form.get('Name')
    email = request.form.get('email')
    contact = request.form.get('contact')

    users = mongo.db.users
    users.insert_one({'Name': name, 'email': email, 'contact': contact})
    
    return redirect(url_for('successpage'))
@app.route('/successpage.html')
def success():
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True , port=2000)"""
from flask import Flask, render_template, request, redirect, url_for, send_file
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['registration_db']  # Create or use an existing database
collection = db['users']  # Create or use an existing collection

@app.route('/')
def index():
    return send_file("visitorID.html")

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
     
    # Insert registration data into MongoDB
    user_data = {'name': name, 'email': email, 'password': password}
    collection.insert_one(user_data)
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return '<h1>Registration Successful!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
