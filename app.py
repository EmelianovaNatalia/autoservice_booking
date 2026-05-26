from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autoservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    box = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)


# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    box = request.form['box']
    date = request.form['date']
    time = request.form['time']

    new_booking = Booking(
        name=name,
        phone=phone,
        box=box,
        date=date,
        time=time
    )

    db.session.add(new_booking)
    db.session.commit()

    return redirect('/')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect('/login')

    bookings = Booking.query.all()
    return render_template('admin.html', bookings=bookings)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            session['logged_in'] = True
            return redirect('/admin')

        return "Неверный логин или пароль"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)