from flask import Flask,render_template,request,session
from flask import Flask, Response, request, send_file,jsonify,current_app as app
from chat import buscar
from retorno import retornar_valores
from flask_session import Session
import pymysql

import io
from weasyprint import HTML
from reportes import generar_reporte_de_consulta
from sentence_transformers import SentenceTransformer, util
import numpy as np
from unidecode import unidecode
from math import ceil
import os
import subprocess
from datetime import datetime

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
model = SentenceTransformer('all-MiniLM-L6-v1')

@app.route("/")

def principala():

    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consulta = "SELECT * FROM respuesta where estado='activo'"
    cursor.execute(consulta)
    sql_consulta = cursor.fetchall()
    cursor.close()
    conn.close()
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('index.html', usuario=session['usuario'],consulta = sql_consulta)
    # Si no existe la sesión de usuario, renderizar un menú básico
    return render_template('index.html', usuario=None)
#permite visualizar tabla de respuesta_bd

@app.route("/login")

def login():
    return render_template('login.html')

@app.route("/cerrar")
def cerrar():
    session.clear()
    return render_template('index.html')

@app.route("/preg")
def preguntasREg():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consulta = "SELECT * FROM respuesta where estado='activo'"
    cursor.execute(consulta)
    sql_consulta = cursor.fetchall()
    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registrarPreguntas.html',consulta = sql_consulta,usuario=session['usuario'])
    return render_template('registrarPreguntas.html',consulta = sql_consulta,usuario=None)

@app.route("/resp")
def RespuestaREg():
    if 'usuario' in session:
        return render_template('registrarRespuesta.html',usuario=session['usuario'])
    return render_template('registrarRespuesta.html',usuario=None)


@app.route("/regResp",methods = ['POST'])
def registrarRespuesta():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        posible_respuesta = request.form.get('posible_respuesta')
        consulta = request.form.get('consulta')
        descripcion = request.form.get('descripcion')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        estado = 'activo'

        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                sql_insert = "INSERT INTO respuesta (resp, consulta, descripcion,estado) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_insert, (posible_respuesta, consulta, descripcion,estado))

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'
@app.route("/regPreg",methods = ['POST'])
def RegistrarPreguntas():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pregunta_nuevo = request.form.get('pregunta_nuevo')
        posible_respuesta = int(request.form.get('posible_respuesta'))
        pregunta_nuevo = unidecode(pregunta_nuevo.lower())
        # Calcular el embedding del texto
        texto_embedding = model.encode(pregunta_nuevo)

        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()

        # Conectar a la base de datos
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        estado = 'activo'
        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                sql_insert = "INSERT INTO embeddings (texto, embedding, cod_respuesta,estado) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_insert, (pregunta_nuevo, embedding_bytes, posible_respuesta,estado))

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'

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
        posible_respuesta = request.form.get('posible_respuesta')
        respuesta = buscar(busqueda,posible_respuesta)
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
                return "<div class = 'alert alert-secondary'>Lo siento, no tengo una respuesta para esa pregunta, no cuento con la suficiente información para responder a su pregunta. puede argumentar un poco mas y tratare de responderle.</div>";

        else:
            return ("<div class = 'alert alert-secondary'>Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas</div>")
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
#visulaizar tabla de respuesta del usuario

@app.route("/tpreg")
def tablaPregunta():
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    listarDeCuanto = 5
    pagina = 1
    # Consulta para verificar si el usuario existe
    consulta_s = "SELECT COUNT(*) FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL"
    cursor.execute(consulta_s)
    num_filas_total = cursor.fetchone()[0]
    TotalPaginas = ceil(num_filas_total / listarDeCuanto)
    inicioList = (pagina - 1) * listarDeCuanto
    consulta = "SELECT * FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL LIMIT %s, %s"
    cursor.execute(consulta, (inicioList, listarDeCuanto))
    sql_consulta = cursor.fetchall()
    consulta_res = "SELECT * FROM respuesta where estado='activo'"
    cursor.execute(consulta_res)
    con_res = cursor.fetchall()
    cursor.close()
    conn.close()
    adjacents = 1
    anterior = "Anterior"
    siguiente = "Siguiente"
    start = max(pagina - adjacents, 1)
    end = min(pagina + adjacents + 1, TotalPaginas + 1)
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('tablaPreguntas.html', usuario=session['usuario'], consulta =sql_consulta, TotalPaginas=TotalPaginas,pagina=pagina,listarDeCuanto=listarDeCuanto
        , start=start,
        end=end,
        anterior=anterior,
        siguiente=siguiente,
        adjacents=adjacents,
        con_res=con_res,
        num_filas_total=num_filas_total)
    # Si no existe la sesión de usuario, renderizar un menú básico
    return render_template('tablaPreguntas.html', usuario=None)


@app.route('/tpre', methods=['POST'])
def tablaPreguntas2():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pagina = int(request.form.get('pagina'))
        listarDeCuanto = int(request.form.get('listarDeCuanto'))
        buscar = request.form.get('buscar')
        tipo_respuesta = request.form.get('tipo_respuesta')
        sql1 = "SELECT COUNT(*) FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL"
        sql = "SELECT * FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL"
        if buscar != '':
            sql+=" and lower(e.texto) like '%"+buscar+"%' "
            sql1+=" and lower(e.texto) like '%"+buscar+"%' "
        if tipo_respuesta != '':
            sql+=" and e.cod_respuesta = "+(tipo_respuesta)
            sql1+=" and e.cod_respuesta = "+(tipo_respuesta)

        #return render_template("index.html")
        # Verificar si existe la sesión de usuario
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        cursor.execute(sql1)
        num_filas_total = cursor.fetchone()[0]
        TotalPaginas = ceil(num_filas_total / listarDeCuanto)
        inicioList = (pagina - 1) * listarDeCuanto
        sql+= " LIMIT "+str(inicioList)+" ,"+str(listarDeCuanto)+""
        cursor.execute(sql)
        sql_consulta = cursor.fetchall()
        consulta_res = "SELECT * FROM respuesta"
        cursor.execute(consulta_res)
        con_res = cursor.fetchall()
        cursor.close()
        conn.close()
        adjacents = 1
        anterior = "Anterior"
        siguiente = "Siguiente"
        start = max(pagina - adjacents, 1)
        end = min(pagina + adjacents + 1, TotalPaginas + 1)
        html = ''
        html += '''
<div class='table-responsive'>
    <table class='table table-bordered table-hover'>
        <thead class='thead-dark'>
            <tr>
                <th>Texto Pregunta</th>
                <th>Respuesta</th>
                <th>descripcion Respuesta</th>
                <th>Acción</th>

            </tr>
        </thead>
        <tbody>'''
        for row in sql_consulta:
            html+="<tr>"
            html+="<td>"+str(row[6])+"</td>"
            html+="<td>"+str(row[1])+"</td>"
            html+="<td>"+str(row[3])+"</td>"
            html+="<td>"
            html+="<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            html+="<button type='button' class='btn btn-info' title='Editar' onclick='editar("+str(row[5])+")'>Editar</button>"
            if row[9] == 'activo':
                html += "<button type='button' class='btn btn-danger' title='Desactivar' onclick=\"accionBtnActivar('activo'," + str(row[5]) + ")\">Desactivar</button>"
            else:
                html += "<button type='button' class='btn btn-success' title='Activar' onclick=\"accionBtnActivar('desactivo'," + str(row[5]) + ")\">Activar</button>"

            html+="</div>"
            html+="</td>"

        html+='''</tbody>
    </table>
</div>

<div class='row'>
    <div class='col'>
        <div class='d-flex flex-wrap flex-sm-row justify-content-between'>
            <ul class='pagination'>'''
        html+="<li class='page-item active'>Página "+str(pagina)+" de "+str(TotalPaginas)+" de "+str(num_filas_total)+" registros</li>"
        html+="</ul>"

        html+="<ul class='pagination d-flex flex-wrap'>"

        if pagina != 1:
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(pagina-1)+")'>"+anterior+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted' >"+anterior+"</span></li>"


        if pagina > (adjacents + 1):
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor(1)'>1</a></li>"

        if pagina > (adjacents + 2):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"
        for i in range(start, end):
            if i == pagina:
                html+="<li class='page-item active'><span class='page-link'>"+str(i)+"</span></li>"
            else:
                html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(i)+")'>"+str(i)+"</a></li>"

        if pagina < (TotalPaginas - adjacents - 1):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"

        if pagina < (TotalPaginas - adjacents):
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(TotalPaginas)+")'>"+str(TotalPaginas)+"</a></li>"

        if pagina < TotalPaginas:
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(pagina+1)+")'>"+siguiente+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted'>"+siguiente+"</span></li>"

        html+='''</ul>
        </div>
    </div>
'''

    return html
@app.route("/Efpreg", methods=['POST'])
def formulariopreguntasREg():
    if request.method == 'POST':
        id = request.form.get('id')
        listarDeCuanto = request.form.get('listarDeCuanto')
        buscar = request.form.get('buscar')
        tipo_respuesta = request.form.get('tipo_respuesta')
        pagina = request.form.get('pagina')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        # Consulta para verificar si el usuario existe
        consulta = "SELECT * FROM respuesta"
        cursor.execute(consulta)
        sql_consulta = cursor.fetchall()
        cons = "select * from embeddings where id = "+id
        cursor.execute(cons)
        sql_co = cursor.fetchone()
        cursor.close()
        conn.close()
        if 'usuario' in session:
            return render_template('EditarPreguntas.html',consulta = sql_consulta,usuario=session['usuario'],
            id=id,
            listarDeCuanto=listarDeCuanto,
            buscar=buscar,
            tipo_respuesta=tipo_respuesta,
            pagina=pagina,
            sql_co=sql_co)
        return render_template('EditarPreguntas.html',consulta = sql_consulta,usuario=None)


@app.route("/ActPreg",methods = ['POST'])
def ActualizarPreguntas():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pregunta_nuevo = request.form.get('pregunta_nuevo')
        posible_respuesta = int(request.form.get('posible_respuesta'))
        id = int(request.form.get('id'))
        pregunta_nuevo = unidecode(pregunta_nuevo.lower())
        # Calcular el embedding del texto
        texto_embedding = model.encode(pregunta_nuevo)

        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()

        # Conectar a la base de datos
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                sql_insert = "update embeddings set texto=%s, embedding=%s,cod_respuesta=%s where id="+str(id)
                cursor.execute(sql_insert, (pregunta_nuevo, embedding_bytes, posible_respuesta))

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'


@app.route("/Delpreg",methods = ['POST'])
def EliminarPreguntas():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        accion = request.form.get('accion')
        id = int(request.form.get('id'))
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                if accion == 'activo':
                    sql_insert = "update embeddings set estado = 'desactivo' where id="+str(id)
                else:
                    sql_insert = "update embeddings set estado = 'activo' where id="+str(id)

                cursor.execute(sql_insert)

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'
@app.route("/Tapreg", methods=['POST'])
def TablaPreguntadespuesDeActualizar():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pagina = int(request.form.get('pagina'))
        listarDeCuanto = int(request.form.get('listarDeCuanto'))
        buscar = request.form.get('buscar')
        tipo_respuesta = request.form.get('tipo_respuesta')
        sql1 = "SELECT COUNT(*) FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL"
        sql = "SELECT * FROM respuesta AS r INNER JOIN embeddings AS e ON r.cod_respuesta = e.cod_respuesta WHERE e.cod_respuesta IS NOT NULL"
        if buscar != '':
            sql+=" and lower(e.texto) like '%"+buscar+"%' "
            sql1+=" and lower(e.texto) like '%"+buscar+"%' "
        if tipo_respuesta != '':
            sql+=" and e.cod_respuesta = "+(tipo_respuesta)
            sql1+=" and e.cod_respuesta = "+(tipo_respuesta)

        #return render_template("index.html")
        # Verificar si existe la sesión de usuario
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        cursor.execute(sql1)
        num_filas_total = cursor.fetchone()[0]
        TotalPaginas = ceil(num_filas_total / listarDeCuanto)
        inicioList = (pagina - 1) * listarDeCuanto
        sql+= " LIMIT "+str(inicioList)+" ,"+str(listarDeCuanto)+""
        cursor.execute(sql)
        sql_consulta = cursor.fetchall()
        consulta_res = "SELECT * FROM respuesta"
        cursor.execute(consulta_res)
        con_res = cursor.fetchall()
        cursor.close()
        conn.close()
        adjacents = 1
        anterior = "Anterior"
        siguiente = "Siguiente"
        start = max(pagina - adjacents, 1)
        end = min(pagina + adjacents + 1, TotalPaginas + 1)
        if 'usuario' in session:
            # Renderizar el menú para usuario autenticado
            return render_template('tablaPreguntas.html', usuario=session['usuario'], consulta =sql_consulta, TotalPaginas=TotalPaginas,pagina=pagina,listarDeCuanto=listarDeCuanto
            , start=start,
            end=end,
            anterior=anterior,
            siguiente=siguiente,
            adjacents=adjacents,
            con_res=con_res,
            num_filas_total=num_filas_total)
        # Si no existe la sesión de usuario, renderizar un menú básico
        return render_template('tablaPreguntas.html', usuario=None)

#tabla de respuestas visualizar

@app.route("/tresp")
def tablaRespuesta():
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    listarDeCuanto = 5
    pagina = 1
    # Consulta para verificar si el usuario existe
    consulta_s = "SELECT COUNT(*) FROM respuesta"
    cursor.execute(consulta_s)
    num_filas_total = cursor.fetchone()[0]
    TotalPaginas = ceil(num_filas_total / listarDeCuanto)
    inicioList = (pagina - 1) * listarDeCuanto
    consulta = "SELECT * FROM respuesta LIMIT %s, %s"
    cursor.execute(consulta, (inicioList, listarDeCuanto))
    sql_consulta = cursor.fetchall()
    consulta_res = "SELECT * FROM respuesta"
    cursor.execute(consulta_res)
    con_res = cursor.fetchall()
    cursor.close()
    conn.close()
    adjacents = 1
    anterior = "Anterior"
    siguiente = "Siguiente"
    start = max(pagina - adjacents, 1)
    end = min(pagina + adjacents + 1, TotalPaginas + 1)
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('tablaRespuesta.html', usuario=session['usuario'], consulta =sql_consulta, TotalPaginas=TotalPaginas,pagina=pagina,listarDeCuanto=listarDeCuanto
        , start=start,
        end=end,
        anterior=anterior,
        siguiente=siguiente,
        adjacents=adjacents,
        con_res=con_res,
        num_filas_total=num_filas_total)
    # Si no existe la sesión de usuario, renderizar un menú básico
    return render_template('tablaRespuesta.html', usuario=None)


@app.route('/trespues', methods=['POST'])
def tablaRespuesta2():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pagina = int(request.form.get('pagina'))
        listarDeCuanto = int(request.form.get('listarDeCuanto'))
        #buscar = request.form.get('buscar')
        respuesta = request.form.get('respuesta')

        sql1 = "SELECT COUNT(*) FROM respuesta "
        sql = "SELECT * FROM respuesta"
        if respuesta != '':
            sql+=" where resp = '"+respuesta+"' "
            sql1+=" where resp = '"+respuesta+"' "
        #return render_template("index.html")
        # Verificar si existe la sesión de usuario
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        cursor.execute(sql1)
        num_filas_total = cursor.fetchone()[0]
        TotalPaginas = ceil(num_filas_total / listarDeCuanto)
        inicioList = (pagina - 1) * listarDeCuanto
        sql+= " LIMIT "+str(inicioList)+" ,"+str(listarDeCuanto)+""
        cursor.execute(sql)
        sql_consulta = cursor.fetchall()
        consulta_res = "SELECT * FROM respuesta"
        cursor.execute(consulta_res)
        con_res = cursor.fetchall()
        cursor.close()
        conn.close()
        adjacents = 1
        anterior = "Anterior"
        siguiente = "Siguiente"
        start = max(pagina - adjacents, 1)
        end = min(pagina + adjacents + 1, TotalPaginas + 1)
        html = ''

        html += '''
<div class='table-responsive'>
    <table class='table table-bordered table-hover'>
        <thead class='thead-dark'>
            <tr>
                <th>Respuesta</th>
                <th>Consulta</th>
                <th>descripcion Respuesta</th>
                <th>Acción</th>
            </tr>
        </thead>
        <tbody>'''
        for row in sql_consulta:
            html+="<tr>"
            html+="<td>"+str(row[1])+"</td>"
            html+="<td>"+str(row[2])+"</td>"
            html+="<td>"+str(row[3])+"</td>"
            html+="<td>"
            html+="<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            html+="<button type='button' class='btn btn-info' title='Editar' onclick='editar("+str(row[0])+")'>Editar</button>"
            if row[4] == 'activo':
                html += "<button type='button' class='btn btn-danger' title='Desactivar' onclick=\"accionBtnActivar('activo'," + str(row[0]) + ")\">Desactivar</button>"
            else:
                html += "<button type='button' class='btn btn-success' title='Activar' onclick=\"accionBtnActivar('desactivo'," + str(row[0]) + ")\">Activar</button>"

            html+="</div>"
            html+="</td>"

        html+='''</tbody>
    </table>
</div>

<div class='row'>
    <div class='col'>
        <div class='d-flex flex-wrap flex-sm-row justify-content-between'>
            <ul class='pagination'>'''
        html+="<li class='page-item active'>Página "+str(pagina)+" de "+str(TotalPaginas)+" de "+str(num_filas_total)+" registros</li>"
        html+="</ul>"

        html+="<ul class='pagination d-flex flex-wrap'>"

        if pagina != 1:
            html+="<li class='page-item'><a class='page-link' onclick='buscarporRES("+str(pagina-1)+")'>"+anterior+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted'>"+anterior+"</span></li>"


        if pagina > (adjacents + 1):
            html+="<li class='page-item'><a class='page-link' onclick='buscarporRES(1)'>1</a></li>"

        if pagina > (adjacents + 2):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"
        for i in range(start, end):
            if i == pagina:
                html+="<li class='page-item active'><span class='page-link'>"+str(i)+"</span></li>"
            else:
                html+="<li class='page-item'><a class='page-link' onclick='buscarporRES("+str(i)+")'>"+str(i)+"</a></li>"

        if pagina < (TotalPaginas - adjacents - 1):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"

        if pagina < (TotalPaginas - adjacents):
            html+="<li class='page-item'><a class='page-link' onclick='buscarporRES("+str(TotalPaginas)+")'>"+str(TotalPaginas)+"</a></li>"

        if pagina < TotalPaginas:
            html+="<li class='page-item'><a class='page-link' onclick='buscarporRES("+str(pagina+1)+")'>"+siguiente+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted'>"+siguiente+"</span></li>"

        html+='''</ul>
        </div>
    </div>
'''

    return html

@app.route("/Efresp", methods=['POST'])
def formularioRespuestas():
    if request.method == 'POST':
        id = request.form.get('id')
        listarDeCuanto = request.form.get('listarDeCuanto')
        tipo_respuesta = request.form.get('respuesta')
        pagina = request.form.get('pagina')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        # Consulta para verificar si el usuario existe
        consulta = "SELECT * FROM respuesta"
        cursor.execute(consulta)
        sql_consulta = cursor.fetchall()
        cons = "select * from respuesta where cod_respuesta = "+str(id)
        cursor.execute(cons)
        sql_co = cursor.fetchone()
        cursor.close()
        conn.close()
        if 'usuario' in session:
            return render_template('EditarRespuesta.html',consulta = sql_consulta,usuario=session['usuario'],
            id=id,
            listarDeCuanto=listarDeCuanto,
            buscar=buscar,
            tipo_respuesta=tipo_respuesta,
            pagina=pagina,
            sql_co=sql_co)
        return render_template('EditarRespuesta.html',consulta = sql_consulta,usuario=None)


@app.route("/ActResp",methods = ['POST'])
def ActualizarRespuestas():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        posible_respuesta = request.form.get("posible_respuesta")
        consulta = request.form.get("consulta")
        descripcion = request.form.get("descripcion")
        id = int(request.form.get('id'))
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                sql_insert = "update respuesta set resp=%s, consulta=%s,descripcion=%s where cod_respuesta="+str(id)
                cursor.execute(sql_insert, (posible_respuesta, consulta, descripcion))

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'
@app.route("/Delresp",methods = ['POST'])
def EliminarRespuesta():

    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        accion = request.form.get('accion')
        id = int(request.form.get('id'))
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

        try:
            with conn.cursor() as cursor:
                # Consulta parametrizada para insertar datos
                if accion == 'activo':
                    sql_insert = "update respuesta set estado = 'desactivo' where cod_respuesta="+str(id)
                else:
                    sql_insert = "update respuesta set estado = 'activo' where cod_respuesta="+str(id)

                cursor.execute(sql_insert)

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'

@app.route('/Taresp', methods=['POST'])
def tablaRespuesta3():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pagina = int(request.form.get('pagina'))
        listarDeCuanto = int(request.form.get('listarDeCuanto'))
        #buscar = request.form.get('buscar')
        respuesta = request.form.get('respuesta')

        sql1 = "SELECT COUNT(*) FROM respuesta "
        sql = "SELECT * FROM respuesta"
        if respuesta != '':
            sql+=" where resp = '"+respuesta+"' "
            sql1+=" where resp = '"+respuesta+"' "
        #return render_template("index.html")
        # Verificar si existe la sesión de usuario
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        cursor.execute(sql1)
        num_filas_total = cursor.fetchone()[0]
        TotalPaginas = ceil(num_filas_total / listarDeCuanto)
        inicioList = (pagina - 1) * listarDeCuanto
        sql+= " LIMIT "+str(inicioList)+" ,"+str(listarDeCuanto)+""
        cursor.execute(sql)
        sql_consulta = cursor.fetchall()
        consulta_res = "SELECT * FROM respuesta"
        cursor.execute(consulta_res)
        con_res = cursor.fetchall()
        cursor.close()
        conn.close()
        adjacents = 1
        anterior = "Anterior"
        siguiente = "Siguiente"
        start = max(pagina - adjacents, 1)
        end = min(pagina + adjacents + 1, TotalPaginas + 1)
        if 'usuario' in session:
            # Renderizar el menú para usuario autenticado
            return render_template('tablaRespuesta.html', usuario=session['usuario'], consulta =sql_consulta, TotalPaginas=TotalPaginas,pagina=pagina,listarDeCuanto=listarDeCuanto
            , start=start,
            end=end,
            anterior=anterior,
            siguiente=siguiente,
            adjacents=adjacents,
            con_res=con_res,
            num_filas_total=num_filas_total)
        # Si no existe la sesión de usuario, renderizar un menú básico
        return render_template('tablaRespuesta.html', usuario=None)

@app.route('/backup')
def backup():
    try:
        # Nombre del archivo de backup (opcional: incluye la fecha y hora en el nombre)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"academico_{timestamp}.sql"
        backup_path = os.path.join(os.getcwd(), "bd", backup_filename)  # Ruta completa al archivo de backup

        # Comando para realizar el backup
        # Asegúrate de tener los permisos adecuados y que el directorio bd exista
        command = f"mysqldump -u unsxx -p'123' academico > {backup_path}"

        # Ejecuta el comando para hacer el backup
        subprocess.run(command, shell=True, check=True)
        # Verifica si el archivo existe en la ruta especificada
        if os.path.exists(backup_path):
            # Si el archivo existe, retorna una respuesta para descargarlo
            return send_file(backup_path, as_attachment=True)
        else:
            # Si el archivo no se guardó correctamente, retorna un mensaje de error
            return jsonify({"error": f"No se pudo crear el archivo de backup en {backup_path}"})

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)})

@app.route('/FormCarrera')
def FormCarrera():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consultas = "SELECT cod_area,nombre_area FROM area"
    cursor.execute(consultas)
    consulta = cursor.fetchall()
    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroCarrera.html',usuario=session['usuario'],consulta=consulta)
    return render_template('registroCarrera.html',usuario=None,consulta=consulta)

@app.route('/RegCarrera',methods=['POST'])
def RegFormCarrera():
    if request.method == 'POST':
        carrera = request.form.get('carrera')
        direccion = request.form.get('direccion')
        area = request.form.get('area')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = "insert into carrera(nombre_carrera,direccion_carrera,cod_area,estado)values(%s,%s,%s,%s)"
                cursor.execute(consultas,(carrera,direccion,area,'activo'))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de docente_

@app.route('/FormDocente')
def FormDocente():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consulcarrera = "SELECT cod_carrera,cod_area,nombre_carrera FROM carrera"
    cursor.execute(consulcarrera)
    consultacarrera = cursor.fetchall()
    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroDocente.html',usuario=session['usuario'],consultacarrera=consultacarrera)
    return render_template('registroDocente.html',usuario=None,consultacarrera=consultacarrera)

@app.route('/RegDocente',methods=['POST'])
def RegFormDocente():
    if request.method == 'POST':
        docente = request.form.get('docente')
        paterno = request.form.get('paterno')
        materno = request.form.get('materno')
        ci = request.form.get('ci')
        profesion = request.form.get('profesion')
        departamento = request.form.get('departamento')
        sexo = request.form.get('sexo')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual = datetime.now().date()

        # Formatear la fecha en el formato YYYY-MM-DD
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = "insert into docente(nombre_docente,ap_docente,am_docente,ci_docente,profesion,telefono,pais,departamento,ciudad,sexo,cod_area,cod_carrera,fecha,estado)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(consultas,(docente,paterno,materno,ci,profesion,0,'Bolivia',departamento,'',sexo,area,carrera,fecha_formateada,'activo'))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de materiasss

@app.route('/FormAsig')
def FormAsinagtura():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consulcarrera = "SELECT cod_carrera,cod_area,nombre_carrera FROM carrera"
    cursor.execute(consulcarrera)
    consultacarrera = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulgrado = "SELECT cod_grado,nombre_grado FROM grado"
    cursor.execute(consulgrado)
    consultagrado = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulplan = "select p.cod_pe,p.nombre_pe,c.nombre_carrera from carrera as c inner join plan_de_estudio as p where c.cod_carrera = p.cod_carrera"
    cursor.execute(consulplan)
    consultaplan = cursor.fetchall()
    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroAsignatura.html',usuario=session['usuario'],consultacarrera=consultacarrera,consultagrado=consultagrado,consultaplan=consultaplan)
    return render_template('registroAsignatura.html',usuario=None,consultacarrera=consultacarrera,consultagrado=consultagrado,consultaplan=consultaplan)

@app.route('/RegAsignatura',methods=['POST'])
def RegFormAsignatura():
    if request.method == 'POST':
        sigla = request.form.get('sigla')
        asignatura = request.form.get('asignatura')
        grado = request.form.get('grado')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        plan = request.form.get('plan')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        pregunta_nuevo = unidecode(asignatura.lower())
        # Calcular el embedding del texto
        texto_embedding = model.encode(pregunta_nuevo)
        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = "insert into asignatura(sigla_asig ,nombre_asig,ht ,hl ,th ,pre_req ,cod_pe ,cod_carrera,cod_grado,cod_area,cod_tp_asig,estado,embedding)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(consultas,(sigla,asignatura,0,0,0,'',plan,carrera,grado,area,1,'activo',embedding_bytes))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'
#treansferencia a otra universidad

@app.route('/FormTranferirO')
def FormTransferirOtraUNiversidad():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consulestu =("SELECT e.cod_es, e.cod_area, e.cod_carrera, e.nombre_es, e.ap_es, e.am_es, c.nombre_carrera, g.nombre_grado "
                   "FROM estudiante as e "
                   "INNER JOIN carrera as c ON e.cod_carrera = c.cod_carrera "
                   "INNER JOIN grado as g ON e.cod_grado = g.cod_grado")


    cursor.execute(consulestu)
    consultaestu = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroTransferirOtra.html',usuario=session['usuario'],consultaestu=consultaestu)
    return render_template('registroTransferirOtra.html',usuario=None,consultaestu=consultaestu)

@app.route('/RegTransferirO',methods=['POST'])
def RegFormTransferirOtra():
    if request.method == 'POST':
        cod_estudiante = request.form.get('cod_estudiante')
        otro = request.form.get('otro')
        fecha = request.form.get('fecha')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual_formateada = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        hora_actual = datetime.now().strftime('%H:%M:%S')
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into transferencia("
                "transferencia,universidad_transferencia,fecha_hora,fecha,cod_es,cod_area,cod_carrera,estado)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,('si',otro,fecha_actual_formateada,fecha,cod_estudiante,area,carrera,estado))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#transferencias de otras universidades

@app.route('/FormTranferirD')
def FormTransferirDEUNiversidad():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    año_actual = datetime.now().year
    # Consulta para verificar si el usuario existe
    consulestu =("SELECT e.cod_es, e.cod_area, e.cod_carrera, e.nombre_es, e.ap_es, e.am_es, c.nombre_carrera, g.nombre_grado,e.fecha "
                   "FROM estudiante as e "
                   "INNER JOIN carrera as c ON e.cod_carrera = c.cod_carrera "
                   "INNER JOIN grado as g ON e.cod_grado = g.cod_grado where e.transferido = 'si' order by e.cod_es desc")


    cursor.execute(consulestu)
    consultaestu = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroTransferirDEotra.html',usuario=session['usuario'],consultaestu=consultaestu)
    return render_template('registroTransferirDEotra.html',usuario=None,consultaestu=consultaestu)

@app.route('/RegTransferirD',methods=['POST'])
def RegFormTransferirDEotra():
    if request.method == 'POST':
        cod_estudiante = request.form.get('cod_estudiante')
        otro = request.form.get('otro')
        fecha = request.form.get('fecha')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'sactivo'
        fecha_actual_formateada = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        hora_actual = datetime.now().strftime('%H:%M:%S')
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into transferir(transferir,universidad_trans,fecha_hora,fecha,hora,cod_es,cod_area,cod_carrera,estado)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,('si',otro,fecha_actual_formateada,fecha,hora_actual,cod_estudiante,area,carrera,estado))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registra nuevo estudiantes

@app.route('/FormEstudiante')
def FormEstudiantes():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()

    # Consulta para verificar si el usuario existe
    consulcarrera = "SELECT cod_carrera,cod_area,nombre_carrera FROM carrera"
    cursor.execute(consulcarrera)
    consultacarrera = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulgrado = "SELECT cod_grado,nombre_grado FROM grado"
    cursor.execute(consulgrado)
    consultagrado = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroEstudiante.html',usuario=session['usuario'],consultagrado=consultagrado,consultacarrera=consultacarrera)
    return render_template('registroEstudiante.html',usuario=None,consultagrado=consultagrado,consultacarrera=consultacarrera)

@app.route('/RegEstudiante',methods=['POST'])
def RegFormEstudiante():
    if request.method == 'POST':
        estudiante = request.form.get('estudiante')
        paterno = request.form.get('paterno')
        materno = request.form.get('materno')
        ci = request.form.get('ci')
        fecha = request.form.get('fecha')
        region = request.form.get('region')
        departamento = request.form.get('departamento')
        sexo = request.form.get('sexo')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        grado = request.form.get('grado')
        transferir = request.form.get('transferir')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into estudiante(nombre_es,ap_es,am_es,titulo_bachiller,ci,pais_es,departamento,"
                "provincia,ciudad,region,sexo,cod_area,cod_carrera,cod_grado,estado,fecha,transferido)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(estudiante,paterno,materno,'si',ci,'Bolivia',departamento,'','',region,sexo,area,carrera,grado,estado,fecha,transferir))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registrar modalidad de titulados_relacion

@app.route('/FormModalidad')
def FormModalidad():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consultas = "SELECT cod_area,nombre_area FROM area"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulcarrera = "SELECT cod_carrera,cod_area,nombre_carrera FROM carrera"
    cursor.execute(consulcarrera)
    consultacarrera = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulplan = "select p.cod_pe,p.nombre_pe,c.nombre_carrera from carrera as c inner join plan_de_estudio as p where c.cod_carrera = p.cod_carrera"
    cursor.execute(consulplan)
    consultaplan = cursor.fetchall()
    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroModalidadTitulacion.html',usuario=session['usuario'],consulta=consulta,consultacarrera=consultacarrera,consultaplan=consultaplan)
    return render_template('registroModalidadTitulacion.html',usuario=None,consulta=consulta,consultacarrera=consultacarrera,consultaplan=consultaplan)

@app.route('/RegModalidad',methods=['POST'])
def RegFormModalidad():
    if request.method == 'POST':
        modalidad = request.form.get('modalidad')
        carrera = request.form.get('carrera')
        area = request.form.get('area')
        plan = request.form.get('plan')

        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'

        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into modalidad_titulacion("
                "tipo_mt,cod_pe,cod_carrera,cod_area,estado"
                ")values(%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(modalidad,plan,carrera,area,estado))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de titulados

@app.route('/FormTitulado')
def FormTitulados():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consultas = "SELECT cod_area,nombre_area FROM area"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulcarrera = "SELECT cod_carrera,cod_area,nombre_carrera FROM carrera"
    cursor.execute(consulcarrera)
    consultacarrera = cursor.fetchall()


    # Consulta para verificar si el usuario existe
    consulmodalidad = "select cod_mt,p.cod_pe,tipo_mt,c.nombre_carrera,p.nombre_pe from modalidad_titulacion as m inner join carrera as c on m.cod_carrera = c.cod_carrera inner join plan_de_estudio as p on m.cod_pe = p.cod_pe where p.cod_pe>=2"
    cursor.execute(consulmodalidad)
    consultamodalidad = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulplan = "select p.cod_pe,p.nombre_pe,c.nombre_carrera from carrera as c inner join plan_de_estudio as p where c.cod_carrera = p.cod_carrera"
    cursor.execute(consulplan)
    consultaplan = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulestu =("SELECT e.cod_es, e.cod_area, e.cod_carrera, e.nombre_es, e.ap_es, e.am_es, c.nombre_carrera, g.nombre_grado,e.fecha "
                   "FROM estudiante as e "
                   "INNER JOIN carrera as c ON e.cod_carrera = c.cod_carrera "
                   "INNER JOIN grado as g ON e.cod_grado = g.cod_grado where e.cod_grado = 5 order by e.cod_es desc")


    cursor.execute(consulestu)
    consultaestu = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroTitulado.html',usuario=session['usuario'],consulta=consulta,consultacarrera=consultacarrera,consultaplan=consultaplan,consultamodalidad=consultamodalidad,consultaestu=consultaestu)
    return render_template('registroTitulado.html',usuario=None,consulta=consulta,consultacarrera=consultacarrera,consultaplan=consultaplan,consultamodalidad=consultamodalidad,consultaestu=consultaestu)

@app.route('/RegTitulado',methods=['POST'])
def RegFormTitulado():
    if request.method == 'POST':
        modalidad = request.form.get('modalidad')
        estado_mt = request.form.get('estado')
        nota = request.form.get('nota')
        fecha = request.form.get('fecha')
        cod_mt = request.form.get('cod_mt')
        cod_pe = request.form.get('cod_pe')
        cod_estudiante = request.form.get('cod_estudiante')
        cod_area = request.form.get('cod_area')
        cod_carrera = request.form.get('cod_carrera')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'

        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into titulado("
                "estado_titu,nota_titu,cod_mt,cod_pe,cod_es,cod_carrera,cod_area,fecha,hora,estado"
                ")values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(estado_mt,nota,cod_mt,cod_pe,cod_estudiante,cod_carrera,cod_area,fecha,'00:00:00',estado))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de asignaturas que dicta el docente_

@app.route('/FormDicta')
def FormDicta():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consultas = "SELECT d.cod_docente,d.nombre_docente,d.ap_docente,d.am_docente,c.nombre_carrera,d.fecha from carrera as c inner join docente as d on c.cod_carrera = d.cod_carrera order by d.cod_docente desc"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulasig = "select a.cod_asig,a.cod_carrera,a.cod_area,a.cod_grado,a.cod_pe,c.nombre_carrera,g.nombre_grado,a.nombre_asig from asignatura as a inner join carrera as c on a.cod_carrera = c.cod_carrera inner join grado as g on a.cod_grado=g.cod_grado"
    cursor.execute(consulasig)
    consultaasig = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroDicta.html',usuario=session['usuario'],consulta=consulta,consultaasig=consultaasig)
    return render_template('registroDicta.html',usuario=None,consulta=consulta,consultaasig=consultaasig)

@app.route('/RegDicta',methods=['POST'])
def RegFormDicta():
    if request.method == 'POST':
        modalidad = request.form.get('modalidad')
        avance = request.form.get('avance')
        docente = request.form.get('docente')
        fecha = request.form.get('fecha')
        cod_asig = request.form.get('cod_asig')
        cod_carrera = request.form.get('cod_carrera')
        cod_area = request.form.get('cod_area')
        cod_grado = request.form.get('cod_grado')
        cod_pe = request.form.get('cod_pe')
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual = datetime.now().strftime("%Y")
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into dicta_asignatura("
                "porcentaje_avance,ano_dicta,cod_docente,cod_asig,cod_pe,cod_carrera,cod_grado,cod_area,estado,fecha"
                ")values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(avance,fecha_actual,docente,cod_asig,cod_pe,cod_carrera,cod_grado,cod_area,estado,fecha))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de asignaturas del estudiante a pasar


@app.route('/FormAsigEst')
def FormAsigEst():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    # Consulta para verificar si el usuario existe
    consultas = "select e.cod_es,e.nombre_es,e.ap_es,e.am_es,nombre_carrera from estudiante as e inner join carrera as c on e.cod_carrera = c.cod_carrera order by e.cod_es desc"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consuldicta = "select da.cod_dicta,da.cod_docente,da.cod_asig,da.cod_pe,da.cod_carrera,da.cod_grado,da.cod_area,c.nombre_carrera,a.nombre_asig,g.nombre_grado from carrera as c inner join dicta_asignatura as da on c.cod_carrera = da.cod_carrera inner join asignatura as a on a.cod_asig = da.cod_asig inner join grado as g on g.cod_grado = da.cod_grado order by da.cod_dicta desc"
    cursor.execute(consuldicta)
    consultadicta = cursor.fetchall()

    # Consulta para verificar si el usuario existe
    consulparcial = "SELECT cod_parcial,nombre_parcial from parciales"
    cursor.execute(consulparcial)
    consultaparcial = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroAsigEstudiante.html',usuario=session['usuario'],consulta=consulta,consultadicta=consultadicta,consultaparcial=consultaparcial)
    return render_template('registroAsigEstudiante.html',usuario=None,consulta=consulta,consultadicta=consultadicta,consultaparcial=consultaparcial)

@app.route('/RegAsigEst',methods=['POST'])
def RegFormAsigEst():
    if request.method == 'POST':
        estudiante = request.form.get('estudiante')
        fecha = request.form.get('fecha').strip()
        cod_dicta = request.form.get('cod_dicta')
        cod_docente = request.form.get('cod_docente')
        cod_asig = request.form.get('cod_asig')
        cod_pe = request.form.get('cod_pe')
        cod_carrera = request.form.get('cod_carrera')
        cod_grado = request.form.get('cod_grado')
        cod_area = request.form.get('cod_area')

        parcial = request.form.get('parcial')
        desercion = request.form.get('desercion')
        teoria = request.form.get('teoria')
        investigacion = request.form.get('investigacion')
        extencion = request.form.get('extencion')

        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual = datetime.now().strftime("%Y")

        # Procesar la fecha
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")  # Convertir a objeto datetime
        ano = fecha_obj.year
        fecha1 = f"{ano}-01-01"
        fecha2 = f"{ano}-12-30"
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into cursa_asignatura("
                "ano,calificacion,estado_asignatura,desercion,cod_es,cod_dicta,cod_docente,cod_asig,cod_pe,"
                "cod_carrera,cod_grado,cod_area,estado,fecha,teoria,investigacion,extencion,cod_parcial"
                ")values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(fecha_actual,0,'',desercion,estudiante,cod_dicta,cod_docente,cod_asig,cod_pe,cod_carrera,
                cod_grado,cod_area,estado,fecha,teoria,investigacion,extencion,parcial))

                # Consulta de selección
                consulda = """
                SELECT teoria, investigacion, extencion, cod_parcial, cod_cursa,cod_asig
                FROM cursa_asignatura
                WHERE cod_es = %s and cod_asig = %s AND (fecha >= %s AND fecha <= %s)
                """
                cursor.execute(consulda, (estudiante, cod_asig, fecha1, fecha2))
                consultada = cursor.fetchall()

                # Consulta de selección de parciales
                consulparcial = "SELECT cod_parcial, nombre_parcial FROM parciales"
                cursor.execute(consulparcial)
                consultaparcial = cursor.fetchall()

                # Calcular el total y actualizar la calificación
                to = 0
                cod_cursa_primero = 0
                for par in consultaparcial:
                    sum = 0
                    for es in consultada:
                        if par[0] == es[3]:
                            sum = (es[0] + es[1] + es[2]) / 3
                        if es[3] == 1:
                            cod_cursa_primero = es[4]
                    if sum > 0:
                        to += sum

                if to > 0:
                    to = to / 4
                    consultas = "UPDATE cursa_asignatura SET calificacion=%s WHERE cod_cursa=%s AND cod_parcial=1"
                    cursor.execute(consultas, (to, cod_cursa_primero))
                print("cod_cursa ",cod_cursa_primero)
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'
#registrar transicion de cursos

@app.route('/FormAvance')
def FormAvance():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()

    # Consulta para verificar si el usuario existe
    consultas = "select e.cod_es,e.cod_carrera,e.cod_area,e.cod_grado,e.nombre_es,e.ap_es,e.am_es,nombre_carrera,g.nombre_grado from estudiante as e inner join carrera as c on e.cod_carrera = c.cod_carrera inner join grado as g on g.cod_grado = e.cod_grado order by e.cod_es desc"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroAvance.html',usuario=session['usuario'],consulta=consulta)
    return render_template('registroAvance.html',usuario=None,consulta=consulta)

@app.route('/RegAvance',methods=['POST'])
def RegFormAvance():
    if request.method == 'POST':

        desercion = request.form.get("desercion")
        abandono = request.form.get("abandono")
        fecha = request.form.get("fecha")
        cod_es = request.form.get("cod_es")
        cod_carrera = request.form.get("cod_carrera")
        cod_area = request.form.get("cod_area")
        cod_grado = request.form.get("cod_grado")
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual = datetime.now().strftime("%Y")
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into estudiante_perdio("
                "estado_ano,abandono,cod_grado,cod_docente,cod_carrera,cod_es,cod_area,fecha"
                ")values(%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(abandono,desercion,cod_grado,1,cod_carrera,cod_es,cod_area,fecha))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#funcion para registrar  plan de estudios

@app.route('/FormPlan')
def FormPLanDE():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()

    # Consulta para verificar si el usuario existe
    consultas = "select cod_carrera,cod_area,nombre_carrera from carrera order by cod_carrera desc"
    cursor.execute(consultas)
    consulta = cursor.fetchall()

    cursor.close()
    conn.close()
    if 'usuario' in session:
        return render_template('registroPlanEstudio.html',usuario=session['usuario'],consulta=consulta)
    return render_template('registroPlanEstudio.html',usuario=None,consulta=consulta)

@app.route('/RegPlan',methods=['POST'])
def RegFormPlan():
    if request.method == 'POST':
        nombre_plan = request.form.get("nombre_plan")
        cod_carrera = request.form.get("carrera")
        cod_area = request.form.get("area")
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        estado = 'activo'
        fecha_actual = datetime.now().strftime("%Y")
        fecha_actual_formateada = datetime.now().strftime("%Y-%m-%d")
        try:
            with conn.cursor() as cursor:
                # Consulta para verificar si el usuario existe
                consultas = ("insert into plan_de_estudio("
                "nombre_pe,ano_pe,fecha_pe,cod_carrera,cod_area,estado"
                ")values(%s,%s,%s,%s,%s,%s)")
                cursor.execute(consultas,(nombre_plan,fecha_actual,fecha_actual_formateada,cod_carrera,cod_area,estado))
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        return 'correcto'

#registro de palabras claves
@app.route("/Clave")
def tablaClave():
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    listarDeCuanto = 5
    pagina = 1
    # Consulta para verificar si el usuario existe
    consulta_s = "SELECT COUNT(*) FROM claves as c inner join agrupar as r on c.cod_agrupar = r.cod_agrupar"
    cursor.execute(consulta_s)
    num_filas_total = cursor.fetchone()[0]
    TotalPaginas = ceil(num_filas_total / listarDeCuanto)
    inicioList = (pagina - 1) * listarDeCuanto
    consulta = "SELECT * FROM claves as c inner join agrupar as r on c.cod_agrupar = r.cod_agrupar order by c.cod_clave desc LIMIT %s, %s"
    cursor.execute(consulta, (inicioList, listarDeCuanto))
    sql_consulta = cursor.fetchall()
    consulta_res = "SELECT * FROM agrupar"
    cursor.execute(consulta_res)
    con_res = cursor.fetchall()

    cursor.close()
    conn.close()
    adjacents = 1
    anterior = "Anterior"
    siguiente = "Siguiente"
    start = max(pagina - adjacents, 1)
    end = min(pagina + adjacents + 1, TotalPaginas + 1)
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('tablaClave.html', usuario=session['usuario'], consulta =sql_consulta, TotalPaginas=TotalPaginas,pagina=pagina,listarDeCuanto=listarDeCuanto
        , start=start,
        end=end,
        anterior=anterior,
        siguiente=siguiente,
        adjacents=adjacents,
        num_filas_total=num_filas_total,
        con_res=con_res)
    # Si no existe la sesión de usuario, renderizar un menú básico
    return render_template('tablaClave.html', usuario=None)



@app.route('/tablaClave', methods=['POST'])
def tablaClavess():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        pagina = int(request.form.get('pagina'))
        listarDeCuanto = int(request.form.get('listarDeCuanto'))
        buscar = request.form.get('buscar')
        respuesta = (request.form.get('respuesta'))
        sql1 = "select count(*) from claves as c inner join agrupar as r where c.cod_agrupar=r.cod_agrupar"
        sql = "select * from claves as c inner join agrupar as r where c.cod_agrupar=r.cod_agrupar"
        if buscar != '':
            sql+=" and lower(c.palabra_clave) like '%"+buscar+"%' "
            sql1+=" and lower(c.palabra_clave) like '%"+buscar+"%' "

        if  respuesta!='':
            respuesta = int(respuesta)
            sql+=" and c.cod_agrupar =  "+str(respuesta)
            sql1+=" and c.cod_agrupar = "+str(respuesta)

        #return render_template("index.html")
        # Verificar si existe la sesión de usuario
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        cursor = conn.cursor()
        cursor.execute(sql1)
        num_filas_total = cursor.fetchone()[0]
        TotalPaginas = ceil(num_filas_total / listarDeCuanto)
        inicioList = (pagina - 1) * listarDeCuanto
        sql+= " order by c.cod_clave desc LIMIT "+str(inicioList)+" ,"+str(listarDeCuanto)+" "
        print(sql)
        cursor.execute(sql)
        sql_consulta = cursor.fetchall()
        cursor.close()
        conn.close()
        adjacents = 1
        anterior = "Anterior"
        siguiente = "Siguiente"
        start = max(pagina - adjacents, 1)
        end = min(pagina + adjacents + 1, TotalPaginas + 1)
        html = ''
        html += '''
<div class='table-responsive'>
    <table class='table table-bordered table-hover'>
        <thead class='thead-dark'>
            <tr>
                <th>palabra clave</th>
                <th>palabra Agrupado en</th>
                <th>Acción</th>

            </tr>
        </thead>
        <tbody>'''
        for row in sql_consulta:
            html+="<tr>"
            html+="<td>"+str(row[1])+"</td>"
            html+="<td>"+str(row[4])+"</td>"
            html+="<td>"
            html+="<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            html+="<button type='button' class='btn btn-info' title='Editar' onclick='editaras("+str(row[0])+",\""+str(row[1])+"\","+str(row[2])+")'>Editar</button>"
            html+="<button align='center'type='button' class='btn btn-danger' title='Eliminar' onclick='Eliminar("+str(row[0])+")'>Eliminar</button>"
            html+="</div>"
            html+="</td>"

        html+='''</tbody>
    </table>
</div>

<div class='row'>
    <div class='col'>
        <div class='d-flex flex-wrap flex-sm-row justify-content-between'>
            <ul class='pagination'>'''
        html+="<li class='page-item active'>Página "+str(pagina)+" de "+str(TotalPaginas)+" de "+str(num_filas_total)+" registros</li>"
        html+="</ul>"

        html+="<ul class='pagination d-flex flex-wrap'>"

        if pagina != 1:
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(pagina-1)+")'>"+anterior+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted' >"+anterior+"</span></li>"


        if pagina > (adjacents + 1):
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor(1)'>1</a></li>"

        if pagina > (adjacents + 2):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"
        for i in range(start, end):
            if i == pagina:
                html+="<li class='page-item active'><span class='page-link'>"+str(i)+"</span></li>"
            else:
                html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(i)+")'>"+str(i)+"</a></li>"

        if pagina < (TotalPaginas - adjacents - 1):
            html+="<li class='page-item'><span class='page-link'>...</span></li>"

        if pagina < (TotalPaginas - adjacents):
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(TotalPaginas)+")'>"+str(TotalPaginas)+"</a></li>"

        if pagina < TotalPaginas:
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor("+str(pagina+1)+")'>"+siguiente+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted'>"+siguiente+"</span></li>"

        html+='''</ul>
        </div>
    </div>
'''

    return html
@app.route("/RegClave",methods = ['POST'])
def RegistrarClaves():
    if request.method == 'POST':
        mensaje = 'correcto'
        # Obtener los datos enviados mediante Ajax
        clave = request.form.get('clave')
        va = request.form.get("id_clave")
        tipo_respuesta = (request.form.get("tipo_respuesta"))
        agrupar = (request.form.get("agrupar"))
        if va:
            id_clave = int(va)
        else:
            id_clave = ''
        if tipo_respuesta != '':
            tipo_respuesta = int(tipo_respuesta)
        clave_nuevo = unidecode(clave.lower())
        # Conectar a la base de datos
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        estado = 'activo'
        try:
            with conn.cursor() as cursor:
                #si hay agrupar entonces hay que verificar que la palabra no se repita
                if agrupar != '':
                    print("agrupar es  ",agrupar)
                    select = "select count(*) from agrupar where palabra_agrupar = %s"
                    cursor.execute(select, (agrupar))
                    filas = cursor.fetchone()[0]
                    print("fila ",filas)
                    if filas > 0:
                        mensaje = 'ya_existe'
                    elif filas == 0:
                        #si filas es igual a cero insertamos
                        sql_insert = "INSERT INTO agrupar(palabra_agrupar) VALUES (%s)"
                        cursor.execute(sql_insert, (agrupar))
                        select1 = "select cod_agrupar from agrupar where palabra_agrupar = %s"
                        cursor.execute(select1, (agrupar))
                        cod_agrupar = cursor.fetchone()[0]

                # Consulta parametrizada para insertar datos
                if mensaje != "ya_existe":
                    if tipo_respuesta == '':
                        tipo_respuesta = cod_agrupar
                    if id_clave:
                        sql_insert = "update claves set palabra_clave = %s,cod_agrupar=%s where cod_clave = %s"
                        cursor.execute(sql_insert, (clave_nuevo,tipo_respuesta,id_clave))
                    else:
                        sql_insert = "INSERT INTO claves(palabra_clave,cod_agrupar) VALUES (%s,%s)"
                        cursor.execute(sql_insert, (clave_nuevo,tipo_respuesta))

            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return mensaje

@app.route("/RegELiminarClave",methods = ['POST'])
def RegistrarEliminarClave():
    if request.method == 'POST':
        # Obtener los datos enviados mediante Ajax
        id = int(request.form.get('id'))
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        estado = 'activo'
        try:
            with conn.cursor() as cursor:
                sql_insert = "delete from claves where cod_clave = %s"
                cursor.execute(sql_insert, (id))
            # Confirmar la transacción
            conn.commit()

        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()

        return 'correcto'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5003)







    #if cursor:
    #        return "¡Conexión exitosa a la base de datos!"
    #    else:
    #        return "NO hay conexion"
