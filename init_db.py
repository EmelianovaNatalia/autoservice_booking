import sqlite3

conn = sqlite3.connect("autoservice.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# тестовые пользователи
cursor.execute("INSERT INTO users (name, phone, email) VALUES ('Ivan Petrov', '+79001112233', 'ivan@mail.com')")
cursor.execute("INSERT INTO users (name, phone, email) VALUES ('Anna Smirnova', '+79004445566', 'anna@mail.com')")

# тестовые боксы
cursor.execute("INSERT INTO boxes (name, price_per_hour) VALUES ('Box 1', 500)")
cursor.execute("INSERT INTO boxes (name, price_per_hour) VALUES ('Box 2', 700)")

# тестовые бронирования
cursor.execute("""
INSERT INTO bookings (user_id, box_id, booking_date, start_time, end_time, status)
VALUES (1, 1, '2026-05-26', '10:00', '12:00', 'confirmed')
""")

conn.commit()
conn.close()

print("Database created with test data")