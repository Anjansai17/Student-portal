
import os
import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "studentportal123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "students.db")


@app.route("/")
def home():
    if "username" in session:
        return redirect("/dashboard")
    return redirect("/login")
# ---------------- HOME ----------------
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        roll = request.form["roll"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students(name, email, roll, password) VALUES (?, ?, ?, ?)",
            (name, email, roll, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE name=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["username"] = user[1]
            session["roll"] = user[3]
            return redirect("/dashboard")
        else:
            return "Invalid Username or Password"

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["username"],
        roll=session["roll"]
    )


# ---------------- ATTENDANCE ----------------
@app.route("/attendance")
def attendance():

    if "roll" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    

    cursor.execute(
        "SELECT subject, present, total FROM attendance WHERE roll=?",
        (session["roll"],)
    )

    attendance = cursor.fetchall()

    conn.close()

    return render_template(
        "attendance.html",
        attendance=attendance
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
#-----------------profile-----------------
@app.route("/profile")
def profile():

    if "roll" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll=?",
        (session["roll"],)
    )

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "profile.html",
        student=student
    )
#-------------------Marks---------------
@app.route("/marks")
def marks():

    if "roll" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT subject, internal, external, grade FROM marks WHERE roll=?",
        (session["roll"],)
    )

    marks = cursor.fetchall()
    conn.close()

    return render_template(
        "marks.html",
        marks=marks
    )
#-------------timetable-------------------
@app.route("/timetable")
def timetable():

    if "roll" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT day, period1, period2, period3, period4, period5
        FROM timetable
        WHERE roll=?
    """, (session["roll"],))

    timetable = cursor.fetchall()

    conn.close()

    return render_template(
        "timetable.html",
        timetable=timetable
    )
@app.route("/notifications")
def notifications():

    if "username" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, message, date
        FROM notifications
        ORDER BY id DESC
    """)

    notifications = cursor.fetchall()

    conn.close()

    return render_template(
        "notifications.html",
        notifications=notifications
    )



@app.route('/settings')
def settings():
    if 'username' not in session:
        return redirect('/login')
    return render_template('settings.html')

@app.route("/admin")
def admin():
    if "username" not in session:
        return redirect("/login")

    return render_template("admin.html")
@app.route("/courses")
def courses():
    if "username" not in session:
        return redirect("/login")

    return render_template("course.html")   # ✅ Correct

    return render_template("courses.html")
@app.route("/course/ai")
def ai_course():
    return render_template("course_ai.html")


@app.route("/course/ml")
def ml_course():
    return render_template("course_ml.html")


@app.route("/course/cn")
def cn_course():
    return render_template("course_cn.html")


@app.route("/course/cs")
def cs_course():
    return render_template("course_cs.html")
@app.route("/course/ai/materials")
def ai_materials():
    return render_template("ai_materials.html")


@app.route("/course/ai/videos")
def ai_videos():
    return render_template("ai_videos.html")


@app.route("/course/ai/assignments")
def ai_assignments():
    return render_template("ai_assignments.html")


@app.route("/course/ai/quizzes")
def ai_quizzes():
    return render_template("ai_quizzes.html")


@app.route("/course/ai/marks")
def ai_marks():
    return render_template("ai_marks.html")



@app.route("/course/ai/attendance")
def ai_attendance():
    return render_template("ai_attendance.html")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)