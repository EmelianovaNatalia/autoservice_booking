from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Подключение базы данных (пока SQLite для простоты)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autoservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Модель бронирования
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


# Обработка бронирования
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
    bookings = Booking.query.all()
    return render_template('admin.html', bookings=bookings)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # создаёт таблицы при первом запуске

    app.run(debug=True)