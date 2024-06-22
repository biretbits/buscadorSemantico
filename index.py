from flask import Flask,render_template,request,session
from flask import Flask, Response, request, send_file
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
    #return render_template("index.html")
    # Verificar si existe la sesión de usuario
    if 'usuario' in session:
        # Renderizar el menú para usuario autenticado
        return render_template('index.html', usuario=session['usuario'])
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
    consulta = "SELECT * FROM respuesta"
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
            html+="<li class='page-item'><a class='page-link' onclick='buscarpor(1)'>"+anterior+"</a></li>"
        else:
            html+="<li class='page-item'><span class='page-link text-muted'>"+anterior+"</span></li>"


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
            html+="<li class='page-item'><a class='page-link' onclick='buscarporRES(1)'>"+anterior+"</a></li>"
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
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5003)







    #if cursor:
    #        return "¡Conexión exitosa a la base de datos!"
    #    else:
    #        return "NO hay conexion"
