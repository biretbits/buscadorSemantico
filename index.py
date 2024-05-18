from flask import Flask,render_template,request,jsonify
from chat import buscar

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
        respuesta,valor_i = buscar(busqueda)

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
                # Retornar los resultados obtenidos de la consulta
                # Convertir los resultados a una lista de diccionarios
                if valor_i >= 0 and valor_i  < 1:
                    data = [{'carrera': row[0], 'to': row[1], 'indice':str(valor_i)} for row in resultados]
                if valor_i >= 1 and valor_i  < 2 or valor_i == 3:
                    data = [{'carrera': row[0], 'nombre': row[1],'ap': row[2],'am': row[3],'ci': row[4],'departamento': row[6], 'indice':str(valor_i)} for row in resultados]
                if valor_i >= 2 and valor_i  < 3 or valor_i == 4:
                    data = [{'carrera': row[0], 'nombre': row[1],'ap': row[2],'am': row[3],'ci': row[4],'departamento': row[6], 'indice':str(valor_i)} for row in resultados]
                if valor_i == 5:
                    data = [{'carrera': row[1], 'direccion': row[2], 'indice':str(valor_i)} for row in resultados]
                if valor_i == 6:
                    data = [{'carrera': row[1], 'direccion': row[2], 'indice':str(valor_i)} for row in resultados]

                #nombre_es,ap_es,am_es,ci,pais_es,departamento,provincia,ciudad,region,sexo
                # Enviar los datos como JSON al cliente
                return jsonify(data)
                # Aquí puedes continuar con tu lógica para procesar los resultados
            else:
                # Si no hay resultados, realiza alguna acción adecuada
                return "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.";

        else:
            return ("Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.")
    else:
        # Si no es una solicitud POST, puedes manejarlo aquí
        return "Solicitud no válida"



if __name__ == '__main__':
    app.run(debug=True,port=5003)







    #if cursor:
    #        return "¡Conexión exitosa a la base de datos!"
    #    else:
    #        return "NO hay conexion"
