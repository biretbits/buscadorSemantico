from flask import Flask,render_template,request
from chat import buscar
from retorno import retornar_valores
import pymysql
app = Flask("mi proyecto nuevo")


'''
@app.route("/")

def principal():
    return "hola bien venido456465"

@app.route("/co")
def co():
    return "hola bien a contacto"

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/query')
def query():
    g = Graph()
    g.load("http://localhost:3030/dataset/sparql")  # URL de tu endpoint SPARQL
    results = g.query("SELECT ?s ?p ?o WHERE {?s ?p ?o} LIMIT 10")
    # Procesa los resultados y devuélvelos como JSON
    data = [{'subject': str(row[0]), 'predicate': str(row[1]), 'object': str(row[2])} for row in results]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

'''

@app.route("/")

def principala():
    return render_template("index.html")

@app.route("/respuesta",methods = ['POST'])
def respuesta():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        busqueda = request.form.get('bus')
        respuesta,accion = buscar(busqueda)
        if respuesta:
            # Establecer la conexión a la base de datos
            conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()
            # Ejecutar la consulta SQL
            cursor.execute(respuesta)
            # Verifica si hay algún resultado antes de obtenerlos
            if cursor.rowcount > 0:
                # Si hay resultados, obtén los datos de la consulta
                resultados = cursor.fetchall()
                cursor.close()
                conn.close()
                return retornar_valores(resultados,accion)
            else:
                # Si no hay resultados, realiza alguna acción adecuada
                return "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.1";

        else:
            return ("Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.2")
    else:
        # Si no es una solicitud POST, puedes manejarlo aquí
        return "Solicitud no válida"



if __name__ == '__main__':
    app.run(debug=True,port=5003)







    #if cursor:
    #        return "¡Conexión exitosa a la base de datos!"
    #    else:
    #        return "NO hay conexion"
