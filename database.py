import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    roll TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Attendance table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll TEXT NOT NULL,
    subject TEXT NOT NULL,
    present INTEGER NOT NULL,
    total INTEGER NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll TEXT NOT NULL,
    subject TEXT NOT NULL,
    internal INTEGER NOT NULL,
    external INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")
cursor.executemany("""
INSERT INTO marks(roll, subject, internal, external, grade)
VALUES (?, ?, ?, ?, ?)
""", [
    ("123", "Python", 29, 63, "A"),
    ("123", "AI", 30, 65, "A+"),
    ("123", "DBMS", 28, 61, "A"),
    ("123", "Operating Systems", 27, 60, "B+")
])
cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll TEXT,
    day TEXT,
    period1 TEXT,
    period2 TEXT,
    period3 TEXT,
    period4 TEXT,
    period5 TEXT
)
""")
cursor.executemany("""
INSERT INTO timetable(roll, day, period1, period2, period3, period4, period5)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", [
    ("123", "Monday", "Python", "AI", "DBMS", "OS", "Math"),
    ("123", "Tuesday", "DBMS", "Python", "AI", "Math", "OS"),
    ("123", "Wednesday", "OS", "Math", "Python", "DBMS", "AI"),
    ("123", "Thursday", "AI", "OS", "Math", "Python", "DBMS"),
    ("123", "Friday", "Math", "DBMS", "OS", "AI", "Python")
])
cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    message TEXT,
    date TEXT
)
""")
cursor.executemany("""
INSERT INTO notifications(title, message, date)
VALUES (?, ?, ?)
""", [
    ("Semester Exam", "Semester exams start from 10 August 2026.", "19-Jul-2026"),
    ("Holiday", "College will remain closed on Sunday.", "19-Jul-2026"),
    ("Placement Drive", "TCS Placement Drive on 25 July.", "19-Jul-2026")
])

conn.commit()
conn.close()

print("Database Created Successfully!")