from flask import Flask, render_template, url_for, request, jsonify
from models.models import db, User, verify_user  # Import the db and User model

app = Flask(__name__)

ENV = 'dev'

# configure the database
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postregress.$15/07/1998@localhost/geomic_tours'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postregress.$15/07/1998@localhost/geomic_tours'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# configure routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

#end of page routes
#data routes
@app.route('/process', methods=['POST'])
def process():
    action = request.args.get('link')

    if action =='login':
         # Get username and password from the AJAX request
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verify the user using the function from models.py
        user = verify_user(username, password)
        
        if user:
            return jsonify({"message": "Login successful", "status": "success"})
        else:
            return jsonify({"message": "Invalid username or password", "status": "error"}), 401


if __name__ == '__main__':
    app.run(debug=True)
