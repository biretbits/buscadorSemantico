import pymysql

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

def seleccionar_estudiante(id):
    sql_consulta = "select *from estudiante"#seleccionamos todos los estudiantes
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
        nombres = ""
        for row in datos:
            if row[id]:
                nombres+= row[1]+"|"+row[2]+"|"+row[3]
                break
        return nombres
    else:
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

def seleccionar_estudiante(nombre, apellidos, carrera):
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
