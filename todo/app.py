from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import os
import datetime

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        connect_timeout=3,
        charset='utf8mb4'
    )

@app.route("/")
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todo_list")
    todo_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return "タイトルが空です", 400

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todo_list (title) VALUES (%s)", (title,))
    connection.commit()
    cursor.close()
    connection.close()
    return "追加成功", 200


@app.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    todo_id = data.get("id")    

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todo_list WHERE todo_id = (%s)", (todo_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return "削除成功", 200


@app.route('/sort/<order>', methods=["POST"])
def sort(order):
    connection = get_db_connection()
    cursor = connection.cursor()
    if order == 'asc':
        cursor.execute("select * FROM todo_list ORDER BY insert_time asc")
    else:
        cursor.execute("select * FROM todo_list ORDER BY insert_time DESC")
    todo_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)