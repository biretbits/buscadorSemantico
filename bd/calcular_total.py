
import pymysql
from datetime import datetime

def obtener_embedding():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT * from cursa_asignatura"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)

    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener el embedding de la consulta
        datos = cursor.fetchall()
        fecha1 = '2022-01-01'
        fecha2 = '2024-12-30'
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux

        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        vec = {}
        carreras = seleccionarCarrerasTodo()
        parcial = seleccionarParciales()
        grado = seleccionarGrado()
        print(a11,"  ",a1," ",a2," ",a22)
        for car in carreras:
            vec[car[0]]={}
            estudiantes = seleccionarEstudianteTodo_id_Carreras(car[0])
            materias=seleccionarAsignatura(car[0],1)
            if estudiantes != 'no':
                for est in estudiantes:
                    vec[car[0]][est[0]]={}
                    for anio in range(a1, a2 + (1)):
                        vec[car[0]][est[0]][anio]={}
                        for gra in grado:
                            vec[car[0]][est[0]][anio][gra[0]]={}
                            if materias != 'no':
                                for mat in materias:
                                    vec[car[0]][est[0]][anio][gra[0]][mat[0]]={}
                                    for par in parcial:
                                        if gra[0] == mat[9]:
                                            vec[car[0]][est[0]][anio][gra[0]][mat[0]][par[0]]={'to':0,'cod_cursa':0}
        print(fecha1,"   ",fecha2)
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
                if row[18] is not None and row[15]>0 and row[16]>0 and row[17]>0:
                    vec[row[10]][row[5]][anoBD][row[11]][row[8]][row[18]]['to']=(row[15]+row[16]+row[17])/3
                    vec[row[10]][row[5]][anoBD][row[11]][row[8]][row[18]]['cod_cursa']=row[0]

                #if anoBD == 2024:
                    #print(row[15],"  ",row[16],"   ",row[17],"   ",vec[row[10]][row[5]][anoBD][row[8]][row[18]],"  ")
        for car in carreras:
            estudiantes = seleccionarEstudianteTodo_id_Carreras(car[0])
            materias=seleccionarAsignatura(car[0],1)
            if estudiantes != 'no':
                for est in estudiantes:
                    for anio in range(a1, a2 + (1)):
                        for gra in grado:
                            if materias != 'no':
                                for mat in materias:
                                    total = 0
                                    cod_cursa = 0
                                    for par in parcial:
                                        if gra[0] == mat[9] and vec[car[0]][est[0]][anio][gra[0]][mat[0]][par[0]]['to']>0:
                                            total+=vec[car[0]][est[0]][anio][gra[0]][mat[0]][par[0]]['to']
                                            cod_cursa = vec[car[0]][est[0]][anio][gra[0]][mat[0]][par[0]]['cod_cursa']
                                    if total>0:
                                        totales = int(total/4)
                                        insertar1(totales,cod_cursa)
                                    #if est[0] == 1:
                                    #print(str(anio)+" materia  "+str(mat[0])+" estudiantes "+str(est[0])+" total = "+str(total)+" totales = "+str(int(totales)))

def insertar1(calificacion_final,cod_cursa):
    print(str(cod_cursa)+" cod_cursa")
    # Consulta SQL para seleccionar un estudiante por su ID
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    try:
        with conn.cursor() as cursor:
            sql_consulta = "UPDATE cursa_asignatura SET calificacion = " + str(calificacion_final) + " WHERE cod_cursa = " + str(cod_cursa)
            cursor.execute(sql_consulta)
        # Confirmar la transacción
        conn.commit()
    finally:
        # Cerrar la conexión siempre, incluso si ocurre una excepción
        conn.close()

def obtener_ano_de_fecha(fecha):
    # Separar la fecha en sus componentes (día, mes, año)
    if '/' in fecha:
        partes = fecha.split('/')
    elif '-' in fecha:
        partes = fecha.split('-')
    else:
        partes = fecha.split('.')
    # Reordenar los componentes para el formato deseado (año, mes, día)
    return partes[0]

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

def seleccionarParciales():
    sql_consulta = "select *from parciales"#seleccionamos todos los estudiantes
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

obtener_embedding()
