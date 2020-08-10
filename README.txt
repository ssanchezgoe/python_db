En este tutorial se resumen los pasos consignados en la página web:

https://code.visualstudio.com/docs/python/tutorial-flask

El tutorial de esta página se divide en las siguientes secciones.

1.  Prerrequisitos

1.1. Instalar las extensiones de Python para vscode https://marketplace.visualstudio.com/items?itemName=ms-python.python
1.2. Instalar Python 3.

2. Creación de un entorno de proyecto para el tutorial de flask.

En esta sección  se creará un ambiente virtual en el que esté instalado Flask.

2.1. En su sistema de archivos debe crear un proyecto, por ejemplo hellow_flask

2.2. En ese foldel, se debe crear un ambiente virtual llamado env que se basa en su interpretador actual

# macOS/Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv env

# Windows
python -m venv env

2.3 Abrir el folder del proyecto en VS Code mediante el comando code ., o corriendo VS Code y usando el comando File > Open Folder 

2.4. En VS Code abra la paleta de comandos (view->command palette - shift+cmd/ctrl+P) y seleccione o escriba "Python: Select Interpreter".

2.5 Cargar un entorno virtual (Terminal->New Terminal). Una vez en dicha terminal ejecute 

#Window
py -3 -m venv .venv
.venv\scripts\activate

Si se genera el mensaje "Activate.ps1 is not digitally signed. You cannot run this script on the current system.", entonces debe ejecutar

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Linux/macOs

python3 -m venv .venv
source .venv/bin/activate

2.6. Instalar Flask en el entorno virtual:

# macOS/Linux
pip3 install flask

# Windows
pip install flask

3. Creación y ejecución de una app minimalista en Flask

3.1 En VS Code, cree un nuevo archivo en el folder del proyecto que se llame app.py.

3.2 En el archivo app.py importe Flask y cree una instancia de un objeto de Flask

from flask import Flask
app = Flask(__name__)

3.3 Adicione también en el archivo app.py, una función que retorne algun contenido, en este caso, un string; use, además, el decorador app.route para mapear la ruta del URL / a esa función:

@app.route("/")
def home():
    return "Hello, Flask!"
    
Nota: Se pueden usar varios decoradores en una misma función, uno por línea, dependiendo de cuantas rutas diferentes se quieran mapear a la misma función.

3.4 Guarde la aplicación app.py (cmd/ctrl S).

3.5 En la terminal, ejecute la aplicación mediante el comando python3 -m flask run (macOS/Linux) or python -m flask run (Windows), que corre el servidor Flask de desarrollo. El servidor busca la aplicacción app.py por defecto. Al correr Flask, verá una salida similar a la siguiente:

(env) D:\py\\hello_flask>python -m flask run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Si lo desea, tambien puede ejecutar el servidor de desarrollo en una dirrección de IP o puerto diferente, usando los comandos de port y hos de la forma --host=0.0.0.0 --port=80.

3.6 Abra un navegador de internet para desplegar la página mediante Ctrl+click en el URL http://127.0.0.1:5000/ que figura en la terminal.

3.7 Observe que al visitar un URL como /, aparece un mensaje en la terminal de depuración que muesta la petición HTTP:

127.0.0.1 - - [10/Aug/2020 14:26:00] "GET / HTTP/1.1" 200 -

3.8 Parar la aplicación mediante Ctrl+C

Tip: If you want to use a different filename than app.py, such as program.py, define an environment variable named FLASK_APP and set its value to your chosen file. Flask's development server then uses the value of FLASK_APP instead of the default file app.py. For more information, see Flask command line interface

4. Uso de una pantilla para renderizar una página

5. Atención de archivos estáticos

6. Creación de plantillas múltiples que extiendan una plantilla base

7. Actividades Opcionales
