import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime, timedelta
from dotenv import load_dotenv
import bcrypt

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# ⚠️ SECRET KEY MUST COME FROM USER'S OWN .env
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# ⚠️ MAIL SETTINGS — USERS MUST SUPPLY THEIR OWN EMAIL + PASSWORD IN .env
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)
db = SQLAlchemy(app)


# DATABASE MODELS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class LoginAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    ip_address = db.Column(db.String(150), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    item_name = db.Column(db.String(150), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)


# ROUTES
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/successfullorder')
def successfullorder():
    return render_template('successfullorder.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password=hashed_password.decode('utf-8'))

    db.session.add(new_user)
    db.session.commit()

    return "User registered successfully"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        LoginAttempt.query.filter_by(username=username).delete()
        db.session.commit()
        return redirect(url_for('home'))
    else:
        ip_address = request.remote_addr
        attempt = LoginAttempt(username=username, ip_address=ip_address)
        db.session.add(attempt)
        db.session.commit()

        two_minutes_ago = datetime.utcnow() - timedelta(minutes=2)
        attempts = LoginAttempt.query.filter_by(username=username).filter(
            LoginAttempt.timestamp > two_minutes_ago
        ).count()

        if attempts > 3:
            send_alert_email(username, ip_address)
            return "Suspicious activity detected. Please try again later."

        return "Login failed"


def send_alert_email(username, ip_address):
    with app.app_context():
        msg = Message(
            'Suspicious Login Attempt Detected',
            recipients=['benjaminbusiness336@gmail.com']
        )
        msg.body = (
            f"Suspicious login attempt detected for username: {username} "
            f"from IP address: {ip_address}."
        )
        mail.send(msg)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/purchase', methods=['POST'])
def purchase():
    full_name = request.form['full_name']
    item_name = request.form['item_name']
    amount = float(request.form['amount'])

    purchase = Purchase(username=full_name, item_name=item_name, amount=amount)
    db.session.add(purchase)
    db.session.commit()

    return redirect(url_for('successfullorder'))


@app.route('/purchase_history')
def purchase_history():
    username = request.args.get('username')
    purchases = Purchase.query.filter_by(username=username).all()
    return render_template('purchase_history.html', purchases=purchases)


# MAIN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
