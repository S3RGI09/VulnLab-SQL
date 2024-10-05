# VulnLab SQL - By S3RGI09

VulnLab SQL es un entorno de práctica diseñado para experimentar con inyecciones SQL utilizando Flask y SQLite. Este proyecto permite a los usuarios configurar un servidor web y una base de datos para practicar vulnerabilidades de inyección SQL en un entorno controlado.

## Contenido

- `start.py`: Script principal para iniciar el entorno de práctica.
- `stop.py`: Script para detener el entorno y restaurar la configuración original.

## Requisitos

- Python 3.x
- Flask
- SQLite

Puedes instalar Flask usando pip:

```bash
pip install Flask
```

## Configuración y Ejecución

1. Ejecutar el script de práctica:
```bash
python start.py
```

Selecciona el servidor web (nginx o apache2).

Selecciona el gestor de base de datos (MariaDB o SQLite).

Selecciona la dificultad de la inyección SQL.

Selecciona el puerto para la aplicación web (5000, 80 o 8080).



2. Acceder a la aplicación:

Una vez que el entorno esté configurado, podrás acceder a la aplicación en la dirección que se muestra en la consola (por ejemplo, http://localhost:5000).


3. Realizar prácticas de inyección SQL:

Utiliza la interfaz de inicio de sesión para probar diferentes técnicas de inyección SQL.


4. Detener el entorno y restaurar la configuración:

Después de terminar la práctica, ejecuta el script de limpieza:
```bash
python stop.py
```
Te pedirá que ingreses el servidor web utilizado (nginx o apache2) y el tipo de base de datos (MariaDB o SQLite).

Detendrá el servidor Flask y eliminará la base de datos creada.




## Estructura de Archivos

start.py: Este script permite iniciar el servidor web y la base de datos, además de gestionar la generación de datos aleatorios.

stop.py: Este script se utiliza para detener el servidor y eliminar la base de datos, restaurando así el entorno.


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, haz un fork del repositorio y envía tus mejoras a través de un pull request.

## Licencia

Este proyecto está bajo la Licencia BSD de 3 cláusulas.
