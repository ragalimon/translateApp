from app import app #hay que hacer una carpeta __init__ para cada modulo que corra scripts de python solamnete
from flask import render_template

@app.route("/")
def index():
	contexto = ["Xime", "Elena", "Mariana"]#{esto fue primero el diccionario{"name": "Elena", "aka": "Elenita"} y ahora pusimos un arreglo
	return render_template("index.html", data=contexto)