from crypt import methods
from distutils.log import debug
from flask import Flask, request, jsonify, render_tem


# Generar el servidor (Back-end)

servidorWeb = Flask(__name__)

#Anotación
@servidorWeb.route("/test", methods=['GET'])    # Esto es como declarar un app.js
def formulario():
    return render_template('pagina.html')

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')    #Por si se quiere conectar a cualquier zona, pero se tiene que poner 
                                                                #EL puerto que se desea conecatr
