import os
import random
import sqlite3
from flask import Flask, request, render_template_string

print("VulnLab SQL - By S3RGI09")
app = Flask(__name__)

WEB_SERVER_OPTIONS = ['nginx', 'apache2']
DB_OPTIONS = ['MariaDB', 'SQLite']
SQL_INJECTION_DIFFICULTY = ['fácil', 'medio', 'difícil', 'muy difícil']

def generar_datos_aleatorios():
    usuarios = []
    for i in range(5):
        usuario = f"usuario{i}"
        contrasena = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789@#$%", k=random.randint(6, 12)))
        usuarios.append((usuario, contrasena))
    return usuarios

def crear_base_datos(db_type):
    if db_type == 'SQLite':
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT, contrasena TEXT)''')
        usuarios = generar_datos_aleatorios()
        cursor.executemany('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', usuarios)
        conn.commit()
        conn.close()
        print("Base de datos SQLite creada con datos aleatorios.")
    elif db_type == 'MariaDB':
        print("Configurar y crear la base de datos en MariaDB.")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        consulta_sql = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND contrasena = '{contrasena}'"
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        try:
            cursor.execute(consulta_sql)
            resultado = cursor.fetchone()
            if resultado:
                return "¡Login exitoso!"
            else:
                return "Usuario o contraseña incorrecta"
        except sqlite3.Error as e:
            return f"Error en la consulta SQL: {e}"
    
    return '''
        <h1>Práctica de Inyección SQL</h1>
        <form method="post">
            Usuario: <input type="text" name="usuario"><br>
            Contraseña: <input type="password" name="contrasena"><br>
            <input type="submit" value="Login">
        </form>
    '''

def main():
    print("Selecciona el servidor web:")
    for i, option in enumerate(WEB_SERVER_OPTIONS, 1):
        print(f"{i}. {option}")
    
    web_choice = int(input("Selecciona una opción (1/2): "))
    web_server = WEB_SERVER_OPTIONS[web_choice - 1]

    print("Selecciona el gestor de base de datos:")
    for i, option in enumerate(DB_OPTIONS, 1):
        print(f"{i}. {option}")
    
    db_choice = int(input("Selecciona una opción (1/2): "))
    db_type = DB_OPTIONS[db_choice - 1]

    print("Selecciona la dificultad de la inyección SQL:")
    for i, option in enumerate(SQL_INJECTION_DIFFICULTY, 1):
        print(f"{i}. {option}")
    
    difficulty_choice = int(input("Selecciona una opción (1-4): "))
    difficulty = SQL_INJECTION_DIFFICULTY[difficulty_choice - 1]

    crear_base_datos(db_type)

    if web_server == 'nginx':
        print("Configurando Nginx...")
    elif web_server == 'apache2':
        print("Configurando Apache2...")
    
    print("\nSelecciona el puerto para la aplicación web:")
    print("1. Puerto 5000 (default)")
    print("2. Puerto 80")
    print("3. Puerto 8080")
    
    puerto_choice = int(input("Selecciona una opción (1/2/3): "))
    if puerto_choice == 1:
        puerto = 5000
    elif puerto_choice == 2:
        puerto = 80
    elif puerto_choice == 3:
        puerto = 8080

    print(f"Desplegando servidor web con {web_server} y base de datos {db_type}...")
    print(f"La aplicación está disponible en: http://localhost:{puerto}")
    
    with open('flask_pid.txt', 'w') as f:
        f.write(str(os.getpid()))
    
    app.run(debug=True, port=puerto)

if __name__ == "__main__":
    main()
