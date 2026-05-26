DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS boxes;
DROP TABLE IF EXISTS bookings;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
);

CREATE TABLE boxes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price_per_hour REAL NOT NULL
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    box_id INTEGER,
    booking_date TEXT,
    start_time TEXT,
    end_time TEXT,
    status TEXT DEFAULT 'new',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (box_id) REFERENCES boxes(id)
);