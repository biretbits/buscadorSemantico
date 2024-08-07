import pymysql
from unidecode import unidecode
import numpy as np
def seleccionar_estudiante(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM estudiante WHERE cod_es = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante[1] + "|" + estudiante[2] + "|" + estudiante[3]
        return nombres
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"




def seleccionarAsignatura():
        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM asignatura"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta)
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchall()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            return estudiante
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"



def seleccionar_carrera():
    sql_consulta = "select *from carrera"#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"


def nombre_carrera_retor(id):

        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM carrera WHERE cod_carrera = %s"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta, (id))
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchone()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            # Si se encuentra el estudiante, obtener sus datos
            nombres = estudiante[1]
            return nombres
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"

def grado_Estudiante(id):

        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM grado WHERE cod_grado = %s"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta, (id))
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchone()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            # Si se encuentra el estudiante, obtener sus datos
            grado = estudiante[1]
            return grado
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"

def seleccionar_estudiante1(nombre, apellidos, carrera):
    ap = ""
    am = ""
    id_car = ""
    hay = "no"
    sql_consulta = "SELECT * FROM estudiante WHERE (nombre_es LIKE %s "
    if len(apellidos) >= 1:  # Solo hay un apellido
        ap = apellidos[0]
        sql_consulta+= " and ap_es like %s)"
        hay = "si"

    if hay != "si":
        sql_consulta+=")"
    if carrera:  # Si hay al menos un valor en la lista de carreras
        id_car = carrera[0]
    # Si se proporcionó una carrera, agregar filtro por carrera
    if id_car:
        sql_consulta += " AND cod_carrera = %s"

    # Conectar a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con los valores proporcionados como parámetros
    if len(apellidos) == 0 and id_car:
        cursor.execute(sql_consulta, ('%' + nombre + '%', id_car))
    if len(apellidos) >= 1 and id_car:
        cursor.execute(sql_consulta, ('%' + nombre + '%', '%' + ap + '%', id_car))

    # Obtener la primera fila de resultados
    estudiante = cursor.fetchone()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # Devolver el primer elemento de la fila de resultados si se encontró un estudiante
    if estudiante:
        return estudiante[0]
    else:
        return "no"


def nombre_materia(id):

        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM asignatura WHERE cod_asig = %s"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta, (id))
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchone()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            # Si se encuentra el estudiante, obtener sus datos
            nombres = estudiante[2]
            return nombres
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"

def obtener_nombre(id):
    sql_consulta = "select *from estudiante where cod_es = %s"#seleccionamos todos los estudiantes
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta,id)
    # Verifica si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtén los datos de la consulta
        sql_consulta = cursor.fetchone()
        cursor.close()
        conn.close()
        nombres = ""
        nombres+= sql_consulta[1]+" "+sql_consulta[2]+" "+sql_consulta[3]

        return nombres
    else:
        return "no"

def obtener_datos_de_curso(id):
    sql_consulta = "select *from estudiante_perdio where cod_es = %s"#seleccionamos todos los estudiantes
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta,id)
    # Verifica si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtén los datos de la consulta
        sql_consulta = cursor.fetchone()
        cursor.close()
        conn.close()
        grado = ""
        grado = sql_consulta[3]

        return grado
    else:
        return "no"

def seleccionarAreas():
    sql_consulta = "select *from area"#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"

def seleccionarAsignatura(id_car,id_pe):
    sql_consulta = "select *from asignatura where cod_carrera = "+str(id_car)#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"
def seleccionarAsignaturaAreas(id_car,id_pe):
    sql_consulta = "select *from asignatura where cod_area = "+str(id_car)#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"


def nombre_asignatura(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM asignatura WHERE cod_asig = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante[2]
        return nombres
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"

def nombre_carrera(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM carrera WHERE cod_carrera = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante[1]
        return nombres
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"



def obtener_id_de_carrera(nombre):

        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM carrera WHERE nombre_carrera like %s"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta, ("%" + nombre + "%",))
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchone()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            # Si se encuentra el estudiante, obtener sus datos
            nombres = estudiante[0]
            return nombres
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"

def consulta_Titulado(sql):
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL
    cursor.execute(sql)
    # Verifica si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtén los datos de la consulta
        sql_consulta = cursor.fetchall()
        cursor.close()
        conn.close()
        return sql_consulta
    else:
        return "no"


def seleccionarcarrera_id(id):

        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT * FROM carrera WHERE cod_area = %s"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta, (id))
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            estudiante = cursor.fetchall()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            return estudiante
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"

def modalidad_titulacion_id(id):
    if id == 1:
        sql_consulta = "SELECT * FROM modalidad_titulacion WHERE cod_carrera = %s and cod_pe = 2"
    else:
        sql_consulta = "SELECT * FROM modalidad_titulacion WHERE cod_carrera = %s"
    #es Informatica# Consulta SQL para seleccionar un estudiante por su ID
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchall()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"
def seleccionarAsignatura_por_id(id_car):
    sql_consulta = "select *from asignatura where cod_carrera = "+str(id_car)#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"

#44

def contar_total_estudiante_curso(cod_grado,cod_carrera,fecha1,fecha2):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT count(*) FROM estudiante WHERE cod_grado = "+str(cod_grado)+" and cod_carrera = "+str(cod_carrera)+" and (fecha >= '"+fecha1+"' and fecha <= '"+fecha2+"')"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante
        return nombres[0]
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return 0


#seleccionar las consultas y embedding
def seleccionar_consultasEmbeddings():
    sql_consulta = "select *from embeddings where cod_respuesta is not null or cod_respuesta != '' and estado='activo'"#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"


def seleccionar_respuesta_y_consulta(id):
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * from respuesta WHERE cod_respuesta = "+str(id)
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"


#buscar area por # ID

def nombre_area_id(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM area WHERE cod_area = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante[1]
        return nombres
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"


def seleccionarCarrerasTodo():
    sql_consulta = "select *from carrera"#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"



def seleccionarGrado():
    sql_consulta = "select *from grado"#seleccionamos todos los estudiantes
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

        return sql_consulta
    else:
        return "no"

def NOmbredeGrado_por_id(id):
    sql_consulta = "select *from grado where cod_grado ="+str(id)#seleccionamos todos los estudiantes
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    # Verifica si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtén los datos de la consulta
        sql_consulta = cursor.fetchone()
        cursor.close()
        conn.close()

        return sql_consulta[1]
    else:
        return "no"

def seleccionarAsignaturaTodos():
        # Consulta SQL para seleccionar un estudiante por su ID
        sql_consulta = "SELECT cod_asig, nombre_asig FROM asignatura"
        conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutar la consulta SQL con el ID proporcionado como parámetro
        cursor.execute(sql_consulta)
        # Verificar si hay algún resultado antes de obtenerlos
        if cursor.rowcount > 0:
            # Si hay resultados, obtener los datos de la consulta
            asignaturas = cursor.fetchall()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            return asignaturas
        else:
            # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
            return "no"


def seleccionar_asignatura_porID(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT *FROM asignatura WHERE cod_asig = "+str(id)
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return 0

def buscar_AsignaturaPORnombre(posible_asignatura):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT *FROM asignatura WHERE LOWER(nombre_asig) like '"+str(posible_asignatura)+"%'"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante[0]
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return 0

def buscar_Area_por_nombre(posible_area):
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT *FROM area WHERE LOWER(nombre_area) = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta,(posible_area))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante[0]
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return 0

def buscar_Carrera_por_nombre(posible_carrera):
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT *FROM carrera WHERE LOWER(nombre_carrera) = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta,(posible_carrera))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante[0]
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return 0

# Función para obtener embeddings de un texto
def obtener_embedding(texto):
    return modelo.encode(texto.lower())

# Función para conectar a la base de datos y obtener embeddings de asignaturas
def obtener_asignaturas_embeddign(modelo):
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()
    sql_consulta = "SELECT * FROM asignatura where embedding =''"
    cursor.execute(sql_consulta)
    if cursor.rowcount > 0:
        res = cursor.fetchall()
        for asi in res:
            if asi[13] == b'':  # Si el campo embedding está vacío
                texto_embedding = modelo.encode(unidecode(asi[2].lower()))
                embedding_bytes = texto_embedding.tobytes()
                sql_update = "UPDATE asignatura SET embedding = %s WHERE cod_asig = %s"
                cursor.execute(sql_update, (embedding_bytes, asi[0]))

    sql_consu = "SELECT cod_asig,embedding FROM asignatura"
    cursor.execute(sql_consu)
    embed = cursor.fetchall()
    embeddings = []
    codigos = []
    # Obtener todos los embeddings y códigos de asignatura
    for row in embed:
        codigos.append(row[0])
        embeddings.append(np.frombuffer(row[1], dtype=np.float32))  # Convertir el blob a un array numpy
    conn.commit()
    conn.close()

    return codigos,embeddings



def obtener_embeddings_ahora(texto,modelo):
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT embedding FROM embeddings WHERE texto = %s and estado='activo' and cod_respuesta=null "
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta, (texto))

    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener el embedding de la consulta
        embedding_str = cursor.fetchone()[0]
        # Convertir la cadena de texto del embedding a un array numpy
        embedding = np.frombuffer(embedding_str, dtype=np.float32)
        return embedding
    else:
        # Si no se encuentra el embedding, calcularlo con el modelo
        texto_embedding = modelo.encode(texto)
        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()
        # Insertar el texto y el embedding en la base de datos
        sql_insert = "INSERT INTO embeddings (texto, embedding) VALUES (%s, %s)"
        cursor.execute(sql_insert, (texto, embedding_bytes))
        conn.commit()
        return texto_embedding


def seleccionarEstudianteTodo_id_Carreras(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM estudiante where cod_carrera = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchall()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return estudiante
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"

def seleccionarTodoPalabraClaves():
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT palabra_clave FROM claves"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchall()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        claves = []
        for est in estudiante:
            claves.append(est[0])
        return claves
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"

def seleccionarTodoClaves():
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT palabra_clave,cod_agrupar FROM claves"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta)
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchall()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        claves = []
        cod_agrupar = []
        for est in estudiante:
            claves.append(est[0])
            cod_agrupar.append(est[1])
        return claves,cod_agrupar
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"

def seleccionarTodoPalabraClaves_id(id):
    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT palabra_clave FROM claves where cod_agrupar = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta,(id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchall()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        claves = []
        for est in estudiante:
            claves.append(est[0])
        return claves
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "no"
