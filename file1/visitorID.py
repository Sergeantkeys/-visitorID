from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['registration_db']  # Create or use an existing database
collection = db['users']  # Create or use an existing collection

@app.route('/')
def index():
    return render_template('visitorID.html')

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
    return 'Registration Successful!'

if __name__ == '__main__':
    app.run(debug=True)
