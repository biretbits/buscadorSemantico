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
