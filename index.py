from flask import Flask,render_template,request,session
from chat import buscar
from retorno import retornar_valores
from flask_session import Session
import pymysql
from flask import Flask, Response, request, send_file
import io
from weasyprint import HTML
from reportes import generar_reporte_de_consulta
app = Flask("mi proyecto nuevo")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'supersecretkey'  # Clave secreta para firmar cookies de sesión


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
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('index.html', usuario=session['usuario'])
    # Si no existe la sesión de usuario, renderizar un menú básico
    return render_template('index.html', usuario=None)
@app.route("/login")

def login():
    return render_template('login.html')

@app.route("/cerrar")
def cerrar():
    session.clear()
    return render_template('index.html')

@app.route("/validando",methods = ['POST'])
def validar():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        # Consulta para verificar si el usuario existe
        consulta = "SELECT * FROM usuario WHERE usuario = %s AND contrasena = %s"
        cursor.execute(consulta, (usuario, password))
        usuariod = cursor.fetchone()

        if usuariod:
            session['usuario'] = usuariod[2]+" "+usuariod[3]
            return "si"
            # Aquí podrías devolver algún indicador de éxito o permitir el acceso
        else:
            return "no"
                # Aquí podrías devolver algún indicador de error o denegar el acceso

@app.route("/respuesta",methods = ['POST'])
def respuesta():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        busqueda = request.form.get('bus')
        respuesta = buscar(busqueda)
        preg = respuesta[-1]
        sql_consulta = respuesta[-1]
        print("sql ",sql_consulta)
        if preg != "argumentar_poco_mas":
            # Establecer la conexión a la base de datos
            conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()
            # Ejecutar la consulta SQL
            cursor.execute(sql_consulta)
            # Verifica si hay algún resultado antes de obtenerlos
            if cursor.rowcount > 0:
                # Si hay resultados, obtén los datos de la consulta
                sql_consulta = cursor.fetchall()
                cursor.close()
                conn.close()
                return retornar_valores(sql_consulta,respuesta)
            else:
                # Si no hay resultados, realiza alguna acción adecuada
                return "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.1";

        else:
            return ("Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.2")
    else:
        # Si no es una solicitud POST, puedes manejarlo aquí
        return "Solicitud no válida"

@app.route('/generar_reporte', methods=['POST'])
def generar_reporte():
    datos = request.form.get('datos')  # Obtener los datos del campo 'datos' del formulario POST
    cor= datos.split(',')
    accion = cor[-2]
    sql_consulta = cor[-1]
    # Generar el HTML del reporte con los datos recibidos
    #html_content = generar_html_reporte(datos)

    # Generar el PDF a partir del HTML
    #

    # Devolver el PDF como respuesta y abrirlo en el navegador
    #return send_file(pdf_file,'reporte.pdf')
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    # Verifica si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtén los datos de la consulta
        sql_consulta = cursor.fetchall()
        cursor.close()
        conn.close()
        html_retor=generar_reporte_de_consulta(sql_consulta,cor)
        pdf_file = generar_pdf(html_retor)

        return send_file(pdf_file,'reporte.pdf')

def generar_pdf(html_content):
    # Generar el PDF a partir del HTML utilizando WeasyPrint
    pdf_bytes = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes
def generar_html_reporte(datos):
    # Aquí generas el contenido HTML del reporte utilizando los datos recibidos
    # Por ejemplo:
    car =[0,1,2,4,5,7,8,4,5,2]
    html = ""
    html+="<!DOCTYPE html>"
    html+="<html>"
    html+="<head>"
    html +="""<style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
        </style>"""
    html+="</head>"
    html+="<body>"

    html+="<h2>Ejemplo de tabla con WeasyPrint</h2>"

    html+="<table>"
    for j in range(len(car)):
        html+="<tr>"
        html+="<th>"+str(car[j])+"</th>"
        html+="</tr>"
    html+="</table>"
    html+="</body>"
    html+="</html>"


    return html



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5003)







    #if cursor:
    #        return "¡Conexión exitosa a la base de datos!"
    #    else:
    #        return "NO hay conexion"
