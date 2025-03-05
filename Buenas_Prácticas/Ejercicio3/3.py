import sqlite3
from flask import Flask, request, render_template_string, jsonify, send_file, abort
import hashlib
import os

'''
Application to create users and download games of players
'''

app = Flask(__name__)
def is_valid_password(pwd):
    if not (10 <= len(pwd) <= 15): #CWE-521 Weak Password Requirements
        return False
    digit_count = sum(c.isdigit() for c in pwd) #CWE-521 Weak Password Requirements
    return digit_count >= 2 #CWE-521 Weak Password Requirements

def create_user(username, password):
    #CWE-327 Use of a Broken or Risky Cryptographic Algorithm
    #CWE-916 Use of Password Hash With Insufficient Computational Effort
    hashed_password = hashlib.md5(password.encode()).hexdigest() 
    
    conn = sqlite3.connect(os.getenv("DB_NAME"))
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    cursor.execute(query, (username, hashed_password))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    user = request.args.get("id", "1")     #CWE-639 Authorization Bypass Through User-Controlled Key

    pwd = request.args.get("pwd", "")
    
    if is_valid_password(pwd) and user.isalpha(): #CWE-20 Improper Input Validation
        create_user(user,pwd)

    html_response = f"""
    <h1>Thank you!</h1>
    <p></p>
    """
    return render_template_string(html_response)


@app.route("/downloadGames/<game_id>", methods=["GET"])
def download_games(game_id):
    file_name = f"{game_id}.pgn"
    if not os.path.isfile(file_name):
        abort(404, "File not found")
    return send_file(file_name, as_attachment=True) #CWE-35 Path Traversal

if __name__ == "__main__":
    app.run(debug=False)