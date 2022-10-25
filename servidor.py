#from crypt import methods
#from distutils.log import debug
#
#from crypt import methods
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename  # Procesar datos de la web
from joblib import load # Empaquetar datso
import numpy as np
import os
from fileinput import filename

#Cargar el modelo
dt = load('modelo.joblib')


# Generar el servidor (Back-end)

servidorWeb = Flask(__name__)

#Anotación
@servidorWeb.route("/test", methods=['GET'])    # Esto es como declarar un app.js
def formulario():
    return render_template('pagina.html')

#Procesar datos a través del form
@servidorWeb.route('/modeloIA', methods=["POST"])
def modeloForm():
    #Procesar los datos de entrada
    contenido = request.form 
    print(contenido)
    
    datosEntrada = np.array([
         7.20000, 0.36000, 0.46000, 2.10000, 0.07400, 24.00000, 44.00000, 0.99534,
         contenido['pH'],
         contenido['sulfatos'],
         contenido['alcohol']
    ])
    #utilizar el modelo
    resultado = dt.predict(datosEntrada.reshape(1,-1))
    
    return jsonify({"Resultado":str(resultado[0])})


#Procesar datos de un archivo
@servidorWeb.route('/modeloFile', methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), filename)
    print(path)
    f.save(path)
    file = open(path, 'r')
    for line in file:
        print(line)
    return jsonify({"Resultado":"datos recibidos"})

@servidorWeb.route("/modelo", methods=["POST"])
def model():
    #Procesador de daros de entrada
    contenido = request.json
    print(contenido)
    return jsonify({"Resultado":"datos recibidos"})
    
        

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')    #Por si se quiere conectar a cualquier zona, pero se tiene que poner 
                                                                #EL puerto que se desea conecatr
