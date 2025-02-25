import sqlite3
from flask import Flask, request, render_template_string, jsonify, send_file, abort
import os
import re
import bcrypt
import os.path

'''
Application to create users and download games of players
'''

app = Flask(__name__)
GAMES_DIRECTORY = "games"  # Directorio específico para archivos de juegos
def is_valid_username(username):
    # Validar que el nombre de usuario tenga entre 4 y 20 caracteres
    if not (4 <= len(username) <= 20):
        return False
        
    # Permitir solo letras, números y guiones bajos
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False
        
    # Verificar que comience con una letra
    if not username[0].isalpha():
        return False
        
    # Evitar nombres de usuario reservados o sensibles
    reserved_names = ['admin', 'root', 'system', 'superuser']
    if username.lower() in reserved_names:
        return False
        
    return True

def is_valid_password(pwd):
    # Corregido CWE-521: Requisitos más robustos para contraseñas
    if not (10 <= len(pwd) <= 15):
        return False
    digit_count = sum(c.isdigit() for c in pwd)
    uppercase_count = sum(c.isupper() for c in pwd)
    lowercase_count = sum(c.islower() for c in pwd)
    special_chars = sum(not c.isalnum() for c in pwd)
    
    return (digit_count >= 2 and 
            uppercase_count >= 1 and 
            lowercase_count >= 1 and 
            special_chars >= 1)

def create_user(username, password):
    # Corregido CWE-327 y CWE-916: Reemplazo de MD5 por bcrypt (con salt)
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(os.getenv("DB_NAME", "users.db"))
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    cursor.execute(query, (username, hashed_password))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    # Corregido CWE-639: Eliminada la manipulación de ID de usuario
    # Ahora se valida adecuadamente el nombre de usuario
    username = request.args.get("username", "")
    pwd = request.args.get("pwd", "")

    if is_valid_password(pwd) and is_valid_username(username):
        create_user(username, pwd)

    html_response = f"""
    <h1>Thank you!</h1>
    <p></p>
    """
    return render_template_string(html_response)

@app.route("/downloadGames/<game_id>", methods=["GET"])
def download_games(game_id):
    # Corregido CWE-35: Prevención de path traversal
    # Validación para permitir solo caracteres alfanuméricos en el ID
    if not re.match(r'^[a-zA-Z0-9]+$', game_id):
        abort(400, "Invalid game ID")
    
    # Asegurar que el archivo esté dentro del directorio designado
    safe_path = os.path.join(GAMES_DIRECTORY, f"{game_id}.pgn")
    
    # Verificación adicional para prevenir path traversal
    abs_file_path = os.path.abspath(safe_path)
    abs_games_dir = os.path.abspath(GAMES_DIRECTORY)
    
    if not abs_file_path.startswith(abs_games_dir):
        abort(403, "Access denied")
    
    if not os.path.isfile(abs_file_path):
        abort(404, "File not found")
        
    return send_file(abs_file_path, as_attachment=True)

if __name__ == "__main__":
    # Crear directorio de juegos si no existe
    if not os.path.exists(GAMES_DIRECTORY):
        os.makedirs(GAMES_DIRECTORY)
        
    app.run(debug=False)