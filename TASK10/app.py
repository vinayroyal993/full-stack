from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# 🔗 MySQL Connection (Change password if needed)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vinay2593",
    database="order_tracking"
)

cursor = db.cursor(dictionary=True)

# 🏠 Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ➕ Add Order
@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.json
    query = "INSERT INTO orders (customer_name, product_name, status, amount) VALUES (%s,%s,%s,%s)"
    values = (data['customer'], data['product'], data['status'], data['amount'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Order Added Successfully"})

# 🔄 Update Order
@app.route('/update_order', methods=['POST'])
def update_order():
    data = request.json
    query = "UPDATE orders SET status=%s WHERE order_id=%s"
    cursor.execute(query, (data['status'], data['id']))
    db.commit()
    return jsonify({"message": "Order Updated Successfully"})

# 📜 Get Logs
@app.route('/logs')
def get_logs():
    cursor.execute("SELECT * FROM order_log")
    return jsonify(cursor.fetchall())

# 📊 Daily Report
@app.route('/report')
def get_report():
    cursor.execute("SELECT * FROM daily_order_report")
    return jsonify(cursor.fetchall())

# ▶ Run App
if __name__ == '__main__':
    app.run(debug=True)