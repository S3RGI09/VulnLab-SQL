import os
import signal
import sqlite3

print("VulnLab SQL - By S3RGI09")
print("Stop Services")

def detener_flask():
    pid_file = 'flask_pid.txt'
    if os.path.exists(pid_file):
        with open(pid_file, 'r') as f:
            pid = int(f.read())
            try:
                os.kill(pid, signal.SIGTERM)
                print(f"Servidor Flask detenido (PID: {pid}).")
            except ProcessLookupError:
                print("El servidor Flask no estaba en ejecución.")
        os.remove(pid_file)
    else:
        print("No se encontró el archivo con el PID de Flask.")

def eliminar_base_datos(db_type):
    if db_type == 'SQLite':
        if os.path.exists('usuarios.db'):
            os.remove('usuarios.db')
            print("Base de datos SQLite eliminada.")
        else:
            print("No se encontró la base de datos SQLite.")
    elif db_type == 'MariaDB':
        print("Conectando a MariaDB para eliminar la base de datos...")

def revertir_web_server(web_server):
    if web_server == 'nginx':
        print("Revirtiendo configuraciones de Nginx...")
    elif web_server == 'apache2':
        print("Revirtiendo configuraciones de Apache2...")

def main():
    print("Finalizando la práctica y restaurando el entorno...")
    web_server = input("Escribe 'nginx' o 'apache2': ").strip().lower()
    db_type = input("Escribe 'MariaDB' o 'SQLite': ").strip().lower()
    detener_flask()
    eliminar_base_datos(db_type)
    revertir_web_server(web_server)
    print("El entorno ha sido restaurado a la normalidad.")

if __name__ == "__main__":
    main()
