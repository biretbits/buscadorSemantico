from flask import jsonify
from sql import nombre_carrera_retor,grado_Estudiante,obtener_nombre,nombre_materia,obtener_datos_de_curso
from sql import seleccionarAreas,seleccionar_carrera,seleccionarAsignaturaAreas,seleccionarAsignatura
from sql import nombre_asignatura,nombre_carrera
from comprobar import formatear_fecha_solo_ano,obtener_ano_de_fecha
from datetime import datetime



ac = {
0: "Ingenieria Informatica",
1: "Ingenieria civil",
2: "Ingenieria de minas",
3: "Ingenieria electromecanica",
4: "Ingenieria mecanica automotriz",
5: "Ingenieria agronomia",
6: "Ingenieria evaporiticos del litio",
7: "Derecho",
8: "Ciencias de la Educacion",
9: "contaduria",
10: "Odontologia",
11: "Laboratorio Clinico",
12: "Enfermeria",
13: "Medicina",
14: "Ingenieria bio medica",
15: "comunicacion social",
16: "bioquimica"
}
colores1 = {
    0: '#FFCDD2',  # Red
    1: '#F8BBD0',  # Pink
    2: '#E1BEE7',  # Purple
    3: '#D1C4E9',  # Deep Purple
    4: '#C5CAE9',  # Indigo
    5: '#BBDEFB',  # Blue
    6: '#B3E5FC',  # Light Blue
    7: '#B2EBF2',  # Cyan
    8: '#B2DFDB',  # Teal
    9: '#C8E6C9',  # Green
    10: '#DCEDC8', # Light Green
    11: '#F0F4C3', # Lime
    12: '#FFF9C4', # Yellow
    13: '#FFECB3', # Amber
    14: '#FFE0B2', # Orange
    15: '#FFCCBC', # Deep Orange
    16: '#D7CCC8'  # Brown
}

#en la base de datos las carreras comienza de 1
#pero como los array comienzan en 0 por eso resto una posicion
areasU = {
0:'Tecnologia',1:"Salud",2:"Sociales"
}

c_infor = {}#xontar estudiantes aprobados por carrera y curso
c_inforr = {}#contar estudiantes reprobados por carrera y cursos
c_civil = {}#xontar estudiantes aprobados por carrera y curso
c_civilr = {}#contar estudiantes reprobados por carrera y cursos
c_minas = {}#xontar estudiantes aprobados por carrera y curso
c_minasr = {}#contar estudiantes reprobados por carrera y cursos
c_elec = {}#xontar estudiantes aprobados por carrera y curso
c_elecr = {}#contar estudiantes reprobados por carrera y cursos
c_mec = {}#xontar estudiantes aprobados por carrera y curso
c_mecr = {}#contar estudiantes reprobados por carrera y cursos
c_agro = {}#xontar estudiantes aprobados por carrera y curso
c_agror = {}#contar estudiantes reprobados por carrera y cursos
c_lit = {}#xontar estudiantes aprobados por carrera y curso
c_litr = {}#contar estudiantes reprobados por carrera y cursos
c_der = {}#xontar estudiantes aprobados por carrera y curso
c_derr = {}#contar estudiantes reprobados por carrera y cursos
c_cie = {}#xontar estudiantes aprobados por carrera y curso
c_cier = {}#contar estudiantes reprobados por carrera y cursos
c_cont = {}#xontar estudiantes aprobados por carrera y curso
c_contr = {}#contar estudiantes reprobados por carrera y cursos
c_odon = {}#xontar estudiantes aprobados por carrera y curso
c_odonr = {}#contar estudiantes reprobados por carrera y cursos
c_lab = {}#xontar estudiantes aprobados por carrera y curso
c_labr = {}#contar estudiantes reprobados por carrera y cursos
c_enf = {}#xontar estudiantes aprobados por carrera y curso
c_enfr = {}#contar estudiantes reprobados por carrera y cursos
c_med = {}#xontar estudiantes aprobados por carrera y curso
c_medr = {}#contar estudiantes reprobados por carrera y cursos
c_bio = {}#xontar estudiantes aprobados por carrera y curso
c_bior = {}#contar estudiantes reprobados por carrera y cursos
c_cso = {}#xontar estudiantes aprobados por carrera y curso
c_csor = {}#contar estudiantes reprobados por carrera y cursos
c_quim = {}#xontar estudiantes aprobados por carrera y curso
c_quimr = {}#contar estudiantes reprobados por carrera y cursos
def generar_reporte_de_consulta(datos,ress):
    accion = ress[-2]
    html = ""
    if accion == "mayor_inscritos":
        total = len(datos)
        fecha1 = ress[0]#obtenemos las fechas que llegan
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vanio = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        carreras = {}
        for anio in range(a1, a2 + (1)):
            vanio[anio]=[0,0,0]
        for anio in range(a1, a2 + (1)):
            carreras[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[16]>=fecha1 and row[16] <= fecha2:
                if row[14] == 1:
                    anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                    vanio[anoBD][row[12]-1]+=1#en cada año y area sumamos mas 1
                    carreras[anoBD][row[13]-1]+=1
        mensaje = "La información sobre que areas y carreras tiene mas inscritos lo detallamos en los siguientes cuadros"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"


        #crear para areas

        html += "<div class='row'style = 'border: 1px solid white;background-color:black'>"
        html += "<h6 class='centro'style='color:white'>Areas</h6><br><br>"
        k1 = 1
        areas ={0:"Técnologia",1:"Salud",2:"Sociales"}
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 class='centro'style='color:white;white-space: pre-line;'>"+str(anio)+"</h6>"
            for ar in range(3):
                html += "<div class='col'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading centro'>"
                html += areas[ar]
                html += "</div>"
                html += "<div class='panel-body'>"
                html += "Los inscritos del area fueron "+str(vanio[anio][ar])+" Estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"
        html += "</div>"
        html += "<br><br>"
        html += "<div class='row'style = 'border: 1px solid white;background-color:black'>"
        html += "<h6 class='centro'align='center'style='color:white'>Carreras</h6>"

        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 class='centro'style='color:white'>"+str(anio)+"</h6>"
            for car in range(17):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:"+colores1[car]+"'>"
                html += "<div class='panel-heading'>"
                html += nombre_carrera_retor(car+1)
                html += "</div>"
                html += "<div class='panel-body'>"
                html += "Los inscritos en la carrera fueron "+str(carreras[anio][car])+" Estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"
        html += "</div>"
        html += "<br><br>"
        html +="<style>.centro{text-align:center}"

        html +=""".row {
            display: flex;
            flex-wrap: wrap;
            with:100%

        }"""

        html+=""".col {
            width: 33.33%;
        }"""

        html +=""".col-sm-6 {
            width: 50%;
        }"""

        html +=""".col-lg-4 {
            width: 33.33%;
        }"""

    return html
