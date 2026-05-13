from flask import Flask

# Создаём экземпляр приложения Flask
app = Flask(__name__)


# Маршрут для главной страницы
@app.route('/')
def home():
    return '<h1>Welcome to AutoService Booking</h1>'


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)