from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",        # change if needed
    password="vinay2593", # change your password
    database="internship_db"
)

cursor = db.cursor()

# 1. Render form
@app.route('/')
def index():
    return render_template('index.html')

# 2. Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    student_name = request.form['student_name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    domain = request.form['domain']

    # 3. Insert into DB
    query = """
    INSERT INTO internship_registrations 
    (student_name, email, phone, course, domain)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (student_name, email, phone, course, domain)

    cursor.execute(query, values)
    db.commit()

    return "Registration Successful!"

# Run app
if __name__ == '__main__':
    app.run(debug=True)