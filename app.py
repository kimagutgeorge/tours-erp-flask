from flask import Flask, render_template, url_for, request, jsonify
from models.models import db, User, user_login  # Import the db and User model
from werkzeug.security import check_password_hash  # To verify password hashes

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
        
        # Query the database for the user
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):  # Verify the password
            return jsonify({"message": "Login successful", "status": "success"})
        else:
            return jsonify({"message": "Invalid username or password", "status": "error"}), 401


if __name__ == '__main__':
    app.run(debug=True)
