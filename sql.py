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
