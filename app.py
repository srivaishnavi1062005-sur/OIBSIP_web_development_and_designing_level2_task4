from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for flash messages and session management
app.secret_key = 'your_secret_key'

# MongoDB connection setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/super_saverdb"
mongo = PyMongo(app)

# SignUp Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if mongo.db.users.find_one({"username": username}):
            flash("Username already exists, please choose a different one.")
            return redirect(url_for('signup'))

        # Hash the password before saving
        hashed_password = generate_password_hash(password, method='sha256')

        # Insert the new user into the MongoDB users collection
        mongo.db.users.insert_one({"username": username, "password": hashed_password})

        flash("You have successfully signed up!")
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Find the user by username
        user = mongo.db.users.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            flash("Login successful!")
            return redirect(url_for('index'))  # Redirect to home page (or wherever)

        flash("Invalid username or password")
        return redirect(url_for('login'))

    return render_template('login.html')

# Home Page (for logged-in users)
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
