from crypt import methods
from flask import Flask, request, jsonify, render_tem


# Generar el servidor (Back-end)

servidorWeb = Flask(__name__)

#Anotación
@servidorWeb.route("/test", methods=['GET'])    # Esto es como declarar un app.js