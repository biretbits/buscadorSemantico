from flask import jsonify
from sql import nombre_carrera_retor,grado_Estudiante,obtener_nombre,nombre_materia,obtener_datos_de_curso
from sql import seleccionarAreas,seleccionar_carrera,seleccionarAsignaturaAreas,seleccionarAsignatura,NOmbredeGrado_por_id
from sql import nombre_asignatura,nombre_carrera,consulta_Titulado,seleccionarcarrera_id,nombre_area_id,seleccionarGrado
from sql import modalidad_titulacion_id,seleccionarAsignatura_por_id,contar_total_estudiante_curso,seleccionarCarrerasTodo,seleccionar_asignatura_porID
from comprobar import formatear_fecha_solo_ano,obtener_ano_de_fecha,fechas
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
0:'Técnologia',1:"Salud",2:"Sociales"
}
cursoss ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
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

c_infor1 = []#xontar estudiantes aprobados por carrera y curso
c_inforr1 = []#contar estudiantes reprobados por carrera y cursos
c_civil1 = []#xontar estudiantes aprobados por carrera y curso
c_civilr1 = []#contar estudiantes reprobados por carrera y cursos
c_minas1 = []#xontar estudiantes aprobados por carrera y curso
c_minasr1 = []#contar estudiantes reprobados por carrera y cursos
c_elec1 = []#xontar estudiantes aprobados por carrera y curso
c_elecr1 = []#contar estudiantes reprobados por carrera y cursos
c_mec1 = []#xontar estudiantes aprobados por carrera y curso
c_mecr1 = []#contar estudiantes reprobados por carrera y cursos
c_agro1 = []#xontar estudiantes aprobados por carrera y curso
c_agror1 = []#contar estudiantes reprobados por carrera y cursos
c_lit1 = []#xontar estudiantes aprobados por carrera y curso
c_litr1 = []#contar estudiantes reprobados por carrera y cursos
c_der1 = []#xontar estudiantes aprobados por carrera y curso
c_derr1 = []#contar estudiantes reprobados por carrera y cursos
c_cie1 = []#xontar estudiantes aprobados por carrera y curso
c_cier1 = []#contar estudiantes reprobados por carrera y cursos
c_cont1 = []#xontar estudiantes aprobados por carrera y curso
c_contr1 = []#contar estudiantes reprobados por carrera y cursos
c_odon1 = []#xontar estudiantes aprobados por carrera y curso
c_odonr1 = []#contar estudiantes reprobados por carrera y cursos
c_lab1 = []#xontar estudiantes aprobados por carrera y curso
c_labr1 = []#contar estudiantes reprobados por carrera y cursos
c_enf1 = []#xontar estudiantes aprobados por carrera y curso
c_enfr1 = []#contar estudiantes reprobados por carrera y cursos
c_med1 = []#xontar estudiantes aprobados por carrera y curso
c_medr1 = []#contar estudiantes reprobados por carrera y cursos
c_bio1 = []#xontar estudiantes aprobados por carrera y curso
c_bior1 = []#contar estudiantes reprobados por carrera y cursos
c_cso1 = []#xontar estudiantes aprobados por carrera y curso
c_csor1 = []#contar estudiantes reprobados por carrera y cursos
c_quim1 = []#xontar estudiantes aprobados por carrera y curso
c_quimr1 = []#contar estudiantes reprobados por carrera y cursos

#array de 9 departamentos
departamento = ['oruro',"potosi","la paz","cochabamba","santa cruz","beni","tarija","chuquisaca","pando"]
id_dep = [0,1,2,3,4,5,6,7,8]
def  retornar_valores(datos,ress):
    accion1 = ress[-2]
    n_car = len(seleccionarCarrerasTodo())
    n_are = len(seleccionarAreas())
    n_grado = len(seleccionarGrado())
    print("la accion es : ",accion1)

    html = ""
    html += "<div class='container justify-content-center align-items-center' style='min-height: 100vh;'>"
    if accion1 == "ver_carreras":
        si_car_n = ress[0]
        id_car = ress[1]#id de carreras
        si_ar = ress[2]
        id_ar = ress[3]
        si_car = ress[4]
        if si_car_n == "si_car_n":#existe una carrera
            html += "Informacion de las siguientes carreras es lo siguiente: "
            html += "<h5>Tabla de carreras de la UNSXX</h5>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Carrera de "+str(nombre_carrera_retor(index1))+"<h5>"
                html += "<table class='table table-striped'>"
                html += "<thead>"
                html += "<tr>"
                html += "<th>Nro</th>"
                html += "<th>Carrera</th>"
                html += "<th>Direccion</th>"
                html += "</tr>"
                html += "</thead>"
                html += "<tbody>"
                k = 1
                for row in datos:
                    if row[0] == index1:
                        html += "<tr>"
                        html += "<td>" + str(k) + "</td>"
                        html += "<td>" + row[1] + "</td>"
                        html += "<td>" + row[2] + "</td>"
                        html += "</tr>"
                        k = k + 1
                html += "</tbody>"
                html += "</table>"
        elif si_ar == 'si_ar':
            html += "Las carreras de la universidad son las siguientes: "
            html += "<h5>Tabla de carreras de la UNSXX</h5>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area "+str(nombre_area_id(index1))+"<h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    html += "<table class='table table-striped'>"
                    html += "<thead>"
                    html += "<tr>"
                    html += "<th>Nro</th>"
                    html += "<th>Carrera</th>"
                    html += "<th>Direccion</th>"
                    html += "</tr>"
                    html += "</thead>"
                    html += "<tbody>"
                    k = 1
                    for car in carreras:
                        for row in datos:
                            if row[0] == car[0]:
                                html += "<tr>"
                                html += "<td>" + str(k) + "</td>"
                                html += "<td>" + row[1] + "</td>"
                                html += "<td>" + row[2] + "</td>"
                                html += "</tr>"
                                k = k + 1
                    html += "</tbody>"
                    html += "</table>"
                else:
                    html+="<h6 align='center'>No se encontro información</h6>"
        elif si_car == "si_car":
            html += "Las carreras de la universidad son las siguientes: "
            html += "<h5>Tabla de carreras de la UNSXX</h5>"
            html += "<table class='table table-striped'>"
            html += "<thead>"
            html += "<tr>"
            html += "<th>Nro</th>"
            html += "<th>Carrera</th>"
            html += "<th>Direccion</th>"
            html += "</tr>"
            html += "</thead>"
            html += "<tbody>"
            k = 1
            for row in datos:
                html += "<tr>"
                html += "<td>" + str(k) + "</td>"
                html += "<td>" + row[1] + "</td>"
                html += "<td>" + row[2] + "</td>"
                html += "</tr>"
                k = k + 1
            html += "</tbody>"
            html += "</table>"

    if accion1 == "total_de_estudiantes":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))

        for anio in range(a1, a2 + (1)):
            vare[anio]=[0]*n_are
        for anio in range(a1, a2 + (1)):
            vcar[anio]=[0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                vare[anoBD][row[12]-1]+=1
                vcar[anoBD][row[13]-1]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            html += "<div class='row'>"
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcar[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vare[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>Se mostrara cuadros por areas y carreras con la cantidad de estudiantes</div>"
            areas = seleccionarAreas()#si hay doble veces repetido el id lo eliminamos a 1
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html+="<div align='center' class='alert alert-secondary'>Areas</div>"

                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vare[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos todo los id de carreras
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcar[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "total_de_estudiantes_carrera3":
        if datos == "argumentar_poco_mas":
            html += "argumentar_poco_mas"
        else:
            # Obtener el número de filasp
            print("la carrera es ",datos[0][13])
            valor = datos[0][13]
            print(valor, " kdffasdfasd f sd fas df ",ress)
            total = len(datos)
            si_activo = ress[1]
            si_desactivo = ress[2]
            si_m = ress[3]
            si_f = ress[4]
            si_dep = ress[5]
            si_prov = ress[6]
            si_nom = ress[7]
            si_apell = ress[8]
            si_apla = ress[10]
            si_apro = ress[11]
            si_des = ress[9]
            si_curso = ress[12]
            carrera = ""
            k = 0
            print(nombre_carrera_retor(datos[0][13]),"no se encuentra a carrera")
            for row in datos:
                dep = row[7]
                provi = row[8]
                nom = row[1]
                ap = row[2]
                am = row[3]
                grado = grado_Estudiante(row[18])
                carrera = nombre_carrera_retor(row[13])
                k = k + 1
                if k == 1:
                    break
            si = "no"
            if si_nom != "no":
                mensaje = "El estudiante "
            else:
                mensaje = "Los estudiantes "

            retu = verificar(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, si_nom, si_apell, carrera, dep, provi, nom, ap, am, si, si_apla, si_apro, si_des, si_curso, grado)

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + " " + retu + " son " + str(total) + "</div>"
            html += "<div class='alert alert-secondary' role='alert'>Detallamos en la siguiente tabla</div>"

            html += "<h2>Tabla de estudiantes</h2>"
            html += "<table class='table table-striped'>"
            html += "<thead>"
            html += "<tr>"
            html += "<th>Nro</th>"
            html += "<th>Nombre</th>"
            html += "<th>Apellido Paterno</th>"
            html += "<th>Apellido Materno</th>"
            html += "<th>Cédula de Identidad</th>"
            html += "<th>pais</th>"
            html += "<th>Departamento</th>"
            html += "<th>provincia</th>"
            html += "<th>region</th>"
            html += "<th>sexo</th>"
            html += "<th>Abandono</th>"
            html += "<th>Perdio año</th>"
            html += "<th>Carrera</th>"
            html += "<th>Curso</th>"
            html += "</tr>"
            html += "</thead>"
            html += "<tbody>"
            contar = 0
            k = 0
            for row in datos:
                if carrera  == "":
                    html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas."
                else:
                    html += "<tr>"
                    html += "<td>" + str(k) + "</td>"
                    html += "<td>" + row[1] + "</td>"
                    html += "<td>" + row[2] + "</td>"
                    html += "<td>" + row[3] + "</td>"
                    html += "<td>" + str(row[5]) + "</td>"
                    html += "<td>" + row[6] + "</td>"
                    html += "<td>" + row[7] + "</td>"
                    html += "<td>" + row[8] + "</td>"
                    html += "<td>" + row[10] + "</td>"
                    html += "<td>" + row[11] + "</td>"
                    html += "<td>" + row[17] + "</td>"
                    html += "<td>" + row[16] + "</td>"
                    html += "<td>" + nombre_carrera_retor(row[13]) + "</td>"
                    html += "<td>" + grado_Estudiante(row[18]) + "</td>"
                    html += "</tr>"
                contar += 1
                k += 1
            html += "</tbody>"
            html += "</table>"


    if accion1 == "datos_especificos_estudiante":
        me = ""
        if me == "argumentar_poco_mas":
            html += "<div class='alert alert-secondary' role='alert'> Le pido que argumente un poco mas</div>"
        else:
            si_activo = "no"
            si_desactivo = "no"
            si_m = "no"
            si_f = "no"
            si_dep = "no"
            si_prov = "no"
            si_nom = ress[1]
            si_apell = ""
            si_apla = "no"
            si_apro = "no"
            si_des = "no"
            si_curso = "no"
            grado = "no"
            k = 0
            for row in datos:
                carrera = row[10]
                dep = row[5]
                provi = row[6]
                nom = row[0]
                ap = row[1]
                am = row[2]
                if ress[2] != "no":
                    si_apell = row[2]
                else:
                    si_apell = ress[2]
                k = k + 1
                if k == 1:
                    break

            si = "no"
            mensaje = " Los datos del estudiante "
            retu = verificar(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, si_nom, si_apell, carrera, dep, provi, nom, ap, am, si,si_apla, si_apro, si_des, si_curso, grado)

            html += "<div class='alert alert-secondary' role='alert'>"+mensaje+" "+retu+" son los siguientes</div>"
            html += "<div class='alert alert-secondary' role='alert'>Detallamos en la siguiente tabla</div>"

            html += "<h2>Tabla de estudiantes</h2>"
            html += "<table class='table table-striped'>"
            html += "<thead>"
            html += "<tr>"
            html += "<th>Nro</th>"
            html += "<th>Nombre</th>"
            html += "<th>Apellido Paterno</th>"
            html += "<th>Apellido Materno</th>"
            html += "<th>Cédula de Identidad</th>"
            html += "<th>pais</th>"
            html += "<th>Departamento</th>"
            html += "<th>provincia</th>"
            html += "<th>region</th>"
            html += "<th>sexo</th>"
            html += "<th>carrera</th>"
            html += "<th>Curso</th>"
            html += "</tr>"
            html += "</thead>"
            html += "<tbody>"
            contar = 0
            k = 1
            for row in datos:
                if row[10] is None or row[10] == "":
                    html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas."
                else:
                    html += "<tr>"
                    html += "<td>"+str(k)+"</td>"
                    html += "<td>"+row[0]+"</td>"
                    html += "<td>"+row[1]+"</td>"
                    html += "<td>"+row[2]+"</td>"
                    html += "<td>"+str(row[3])+"</td>"
                    html += "<td>"+row[4]+"</td>"
                    html += "<td>"+row[5]+"</td>"
                    html += "<td>"+row[6]+"</td>"
                    html += "<td>"+row[8]+"</td>"
                    html += "<td>"+row[9]+"</td>"
                    html += "<td>"+row[10]+"</td>"
                    html += "<td>"+grado_Estudiante(obtener_datos_de_curso(row[11]))+"</td>"

                    html += "</tr>"
                contar += 1
                k += 1
            html += "</tbody>"
            html += "</table>"

    if accion1 == "seleccionar_carreras_area":

        # Variables para el bucle for
        for row in datos:
            area = row[1]
            direccion_area = row[6]
            telefono_area = row[3]
            nombre_carrera = row[5]
            direccion_carrera = row[6]

        # Variables adicionales después del bucle
        c_area = ress[1]
        si_ar = ress[0]
        si = "no"
        mensaje = "El área de "
        retu = verificar_area(si, area, direccion_area, telefono_area, nombre_carrera, direccion_carrera, si_ar, c_area)
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + " " + retu + " tiene las siguientes carreras </div>"
        html += "<h2>Tabla de carreras</h2>"
        html += "<table class='table table-striped'>"
        html += "<thead>"
        html += "<tr>"
        html += "<th>Nro</th>"
        html += "<th>Carrera</th>"
        html += "<th>Direccion</th>"
        html += "</tr>"
        html += "</thead>"
        html += "<tbody>"
        contar = 0
        # Bucle para la tabla de carreras
        k = 1
        for row in datos:
            if row[5] is None or row[5] == "":
                html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas."
            else:
                html += "<tr>"
                html += "<td>" + str(k) + "</td>"
                html += "<td>" + row[5] + "</td>"
                html += "<td>" + row[6] + "</td>"
                html += "</tr>"
            contar += 1
            k = k + 1

        html += "</tbody>"
        html += "</table>"


    if accion1 == "estudiante_por_area":
        total = len(datos)
        si_activo = ress[0]
        si_desactivo = ress[1]
        si_m = ress[2]
        si_f = ress[3]
        si_dep = ress[5]
        si_prov = ress[4]
        si_des = ress[6]
        si_apla = ress[7]
        si_apro = ress[8]
        si_ar = ress[9]
        c_area = ress[10]

        # Supongo que solo necesitas los datos del primer estudiante
        k = 0
        for row in datos:
            dep = row[7]
            provi = row[8]
            k = k+1
            if k == 1:
                break
        si = "no"
        mensaje = "Los estudiantes "
        retu = verificar2(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, dep, provi, si_des, si_apla, si_ar, si_apro, c_area, si)

        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + " " + retu + " son " + str(total) + "</div>"
        html += "<div class='alert alert-secondary' role='alert'>Detallamos en la siguiente tabla</div>"

        html += "<h2>Tabla de estudiantes</h2>"
        html += "<table class='table table-striped'>"
        html += "<thead>"
        html += "<tr>"
        html += "<th>Nro</th>"
        html += "<th>Nombre</th>"
        html += "<th>Apellido Paterno</th>"
        html += "<th>Apellido Materno</th>"
        html += "<th>Cédula de Identidad</th>"
        html += "<th>País</th>"
        html += "<th>Departamento</th>"
        html += "<th>Provincia</th>"
        html += "<th>Región</th>"
        html += "<th>Sexo</th>"
        html += "<th>Abandono</th>"
        html += "<th>Año perdido</th>"
        html += "</tr>"
        html += "</thead>"
        html += "<tbody>"
        contar = 0
        # Bucle para la tabla de estudiantes
        k = 1
        for row in datos:
            html += "<tr>"
            html += "<td>" + str(k) + "</td>"
            html += "<td>" + (row[1]) + "</td>"
            html += "<td>" + row[2] + "</td>"
            html += "<td>" + row[3] + "</td>"
            html += "<td>" + str(row[5]) + "</td>"
            html += "<td>" + row[6] + "</td>"
            html += "<td>" + row[7] + "</td>"
            html += "<td>" + row[8] + "</td>"
            html += "<td>" + row[10] + "</td>"
            html += "<td>" + row[11] + "</td>"
            html += "<td>" + row[17] + "</td>"
            html += "<td>" + row[16] + "</td>"
            html += "</tr>"
            k = k+1
            contar += 1

        html += "</tbody>"
        html += "</table>"


    if accion1 == "seleccionar_asignatura_estudiante":
        nombres = ""
        carrera = ""
        grado = ""
        mensaje = ""
        si_hay = "no"
        nom_apell = ress[4]
        calif = ress[2]
        if nom_apell != "no":

            k = 0
            for row in datos:
                nombres = obtener_nombre(row[5])
                carrera = nombre_carrera_retor(row[10])
                grado = grado_Estudiante(row[11])
                k=k+1
                if(k == 1):
                    break
            si_car = ress[3]
            si_curso = ress[5]
            mensaje = "El estudiante " + nombres
            si = "no"
            mensaje += verificar_grado(si_car, si_curso, carrera, grado, si)
            si_hay = "si"
        else:
            nombres = ress[0] + " " + ress[1]
            mensaje = "No se encontró información del estudiante " + nombres

        html = ""

        if si_hay == "si":
            if calif != "no":
                html += "<div class='alert alert-secondary' role='alert'>" + mensaje + " tiene las siguientes calificaciones en las materias</div>"
            else:
                html += "<div class='alert alert-secondary' role='alert'>" + mensaje + " tiene las siguientes materias</div>"
            html += "<h2>Tabla de Asignaturas</h2>"
            html += "<table class='table table-striped'>"
            html += "<thead>"
            html += "<tr>"
            html += "<th>Nro</th>"
            html += "<th>Asignatura</th>"
            html += "<th>Curso</th>"
            if calif != "no":
                html += "<th>Calificación</th>"
            html += "</tr>"
            html += "</thead>"
            html += "<tbody>"
            contar = 0
            k = 1
            for row in datos:
                if row[10] is None or row[10] == "":
                    html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco más."
                else:
                    html += "<tr>"
                    html += "<td>" + str(k) + "</td>"
                    html += "<td>" + nombre_materia(row[8]) + "</td>"
                    html += "<td>" + grado_Estudiante(row[11]) + "</td>"
                    if calif != "no":
                        html += "<td>" + row[2] + "</td>"
                    html += "</tr>"
                contar += 1
                k  = k + 1
            html += "</tbody>"
            html += "</table>"
            html += "Se tiene " + str(contar) + " asignaturas activas"
        else:
            html+="<div class='alert alert-secondary' role='alert'>"+mensaje+"</div>"
    if accion1 == "total_de_estudiantes_estadisticas":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux

        vareasApro = {}
        vcarApro = {}
        vcarCurApro ={}
        cndes = 0
        total = 0
        ctec = 0
        csal = 0
        csoc = 0
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()
        for are in areas:
            vareasApro[are[0]] = {}
            for anio in range(a1, a2 + 1):
                vareasApro[are[0]][anio] = {'aprobado': 0, 'aplazado': 0}
        carreras = seleccionarCarrerasTodo()
        grado = seleccionarGrado()
        for car in carreras:
            vcarApro[car[0]] = {}
            vcarCurApro[car[0]] = {}
            for anio in range(a1, a2 + 1):
                vcarApro[car[0]][anio] = {'aprobado': 0, 'aplazado': 0}
                vcarCurApro[car[0]][anio] = {}
                for grad in grado:
                    vcarCurApro[car[0]][anio][grad[0]] = {'aprobado': 0, 'aplazado': 0}

        #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if not isinstance(row[8], type(None)) and row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango
                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                if row[1] == "aprobado":
                    vareasApro[row[7]][anoBD]['aprobado']+=1
                    vcarApro[row[5]][anoBD]['aprobado']+=1
                    vcarCurApro[row[5]][anoBD][row[3]]['aprobado']+=1
                elif row[1] == "reprobado":
                    vareasApro[row[7]][anoBD]['aplazado']+=1
                    vcarApro[row[5]][anoBD]['aplazado']+=1
                    vcarCurApro[row[5]][anoBD][row[3]]['aplazado']+=1


        if si_car_n == "si_car_n":#esta buscando carreras
            mensaje = "La cantidad de estudiantes reprobados y aprobados en las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='row'>"
                    html += "<div class='col-lg-12' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html +="<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Aprobados</td>"
                    html+="<td>Reprobados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vcarApro[index1][anio]['aprobado'])+"</td>"
                    html+="<td>"+str(vcarApro[index1][anio]['aplazado'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html +="</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "<div class='row'>"
                    for gra in grado:#recorremos todos los cursos aprobados por año

                        html += "<div class='col-lg-3'style = 'background-color:khaki;border: 1px solid black;'>"
                        html += "<div class='panel panel-default text-center'>"
                        html += "<div class='panel-heading'>"
                        html += "Curso "+str(gra[1])
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html +="<table class='table'>"
                        html+= "<thead>"
                        html+="<tr>"
                        html+="<td>Aprobados</td>"
                        html+="<td>Reprobados</td>"
                        html+="</tr>"
                        html+="</thead>"
                        html+="<tbody>"
                        html+="<tr>"

                        html += "<td>" + str(vcarCurApro[index1][anio][gra[0]]['aprobado']) + "</td>"
                        html +="<td> " + str(vcarCurApro[index1][anio][gra[0]]['aplazado']) + "</td>"  # es de la carrera de bioquimica

                        html+="</tr>"
                        html+="</tbody>"
                        html +="</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"

                html += "</div>"
        elif si_ar == "si_ar":
            mensaje = "La cantidad de estudiantes reprobados y aprobados en las siguientes areas son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h6 align='center'>Area "+str(nombre_area_id(index1))+"<h6>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):

                    html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html +="<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Aprobados</td>"
                    html+="<td>Reprobados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vareasApro[index1][anio]['aprobado'])+"</td>"
                    html+="<td>"+str(vareasApro[index1][anio]['aplazado'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html +="</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            mensaje = "La cantidad de Estudiantes reprobados y aprobados "
            mensaje += " es lo siguiente por área y carreras"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            html += "<h4 align='center'>Areas</h4>"
            areas = seleccionarAreas()
            for are in areas:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h6 align='center'>Area "+str(nombre_area_id(index1))+"<h6>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):
                    html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html+= "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html +="<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Aprobados</td>"
                    html+="<td>Reprobados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vareasApro[index1][anio]['aprobado'])+"</td>"
                    html+="<td>"+str(vareasApro[index1][anio]['aplazado'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html +="</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"

            h = 1
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='row'>"
                    html += "<div class='col-lg-12' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html +="<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Aprobados</td>"
                    html+="<td>Reprobados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vcarApro[index1][anio]['aprobado'])+"</td>"
                    html+="<td>"+str(vcarApro[index1][anio]['aplazado'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html +="</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "<div class='row'>"
                    for gra in grado:#recorremos todos los cursos aprobados por año

                        html += "<div class='col-lg-3'style = 'background-color:khaki;border: 1px solid black;'>"
                        html += "<div class='panel panel-default text-center'>"
                        html += "<div class='panel-heading'>"
                        html += "Curso "+str(gra[1])
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html +="<table class='table'>"
                        html+= "<thead>"
                        html+="<tr>"
                        html+="<td>Aprobados</td>"
                        html+="<td>Reprobados</td>"
                        html+="</tr>"
                        html+="</thead>"
                        html+="<tbody>"
                        html+="<tr>"

                        html += "<td>" + str(vcarCurApro[index1][anio][gra[0]]['aprobado']) + "</td>"
                        html +="<td> " + str(vcarCurApro[index1][anio][gra[0]]['aplazado']) + "</td>"  # es de la carrera de bioquimica

                        html+="</tr>"
                        html+="</tbody>"
                        html +="</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"

                    html += "</div>"


        # Datos para el gráfico

    if accion1 == "seleccionar_estudiantes_desertores":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux

        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        vcar={}
        vare={}
        vcarCur={}
        areas = seleccionarAreas()
        carreras = seleccionarCarrerasTodo()
        grado = seleccionarGrado()
        for are in areas:
            vare[are[0]]={}
            for anio in range(a1, a2 + (1)):
                vare[are[0]][anio]={'si':0,'no':0}
        for car in carreras:
            vcar[car[0]]={}
            vcarCur[car[0]]={}
            for anio in range(a1, a2 + (1)):
                vcar[car[0]][anio]={'si':0,'no':0}
                vcarCur[car[0]][anio]={}
                for gra in grado:
                    vcarCur[car[0]][anio][gra[0]]={'si':0,'no':0}

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if not isinstance(row[8], type(None)) and row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango
                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                if row[2] == "no":#no abandonaron
                    vare[row[7]][anoBD][row[2]]=+1
                    vcar[row[5]][anoBD][row[2]]=+1
                    vcarCur[row[5]][anoBD][row[3]][row[2]]=+1
                elif row[2] == "si":#si abandonaron
                    vare[row[7]][anoBD][row[2]]=+1
                    vcar[row[5]][anoBD][row[2]]=+1
                    vcarCur[row[5]][anoBD][row[3]][row[2]]=+1

        if si_car_n == "si_car_n":#esta buscando carreras
            mensaje = "La cantidad de estudiantes que desertaron en las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='row'>"
                    html += "<div class='col-lg-12'>"
                    html += "<div class='panel panel-default text-center bg-light' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Desertores "+str(vcar[index1][anio]['si'])+"</h6></center>"
                    html += "<center><h6>No desertores "+str(vcar[index1][anio]['no'])+"</h6></center>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "<br>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "<div class='row'>"
                    for gra in grado:#recorremos todos los cursos aprobados por año

                        html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                        html += "<div class='panel panel-default text-center'>"
                        html += "<div class='panel-heading'>"
                        html += "<b>"+str(gra[1])+"</b>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "<center><h6>Desertores "+str(vcarCur[index1][anio][gra[0]]['si'])+"</h6></center>"
                        html += "<center><h6>No desertores "+str(vcarCur[index1][anio][gra[0]]['no'])+"</h6></center>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html += "</div>"
                    html += "<br>"
        elif si_ar == "si_ar":
            mensaje = "La cantidad de estudiantes que desertaron por areas son lo siguiente"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h6 align='center'>Area "+str(nombre_area_id(index1))+"</h6>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Desertores: "+str(vare[index1][anio]['si'])+"</h6></center>"
                    html += "<center><h6>No desertores: "+str(vare[index1][anio]['no'])+"</h6></center>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
        else:
            mensaje = "La cantidad de estudiantes que desertaron "
            mensaje += "es lo siguiente por área y carreras"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            #crear para areas

            html += "<h4 align='center'>Areas</h4>"

            for are in areas:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area "+str(nombre_area_id(index1))+"<h5>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center' >"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Desertores: "+str(vare[index1][anio]['si'])+"</h6></center>"
                    html += "<center><h6>No desertores: "+str(vare[index1][anio]['no'])+"</h6></center>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
            h = 1

            for car  in carreras:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='row'>"
                    html += "<div class='col-lg-12'style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Desertores "+str(vcar[index1][anio]['si'])+"</h6></center>"
                    html += "<center><h6>No desertores "+str(vcar[index1][anio]['no'])+"</h6></center>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html += "<br>"
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    html += "<div class='row'>"
                    for gra in grado:#recorremos todos los cursos aprobados por año

                        html += "<div class='col-lg-3' style = 'background-color:RGBA(0, 255, 250, 0.3);border: 1px solid black;'>"
                        html += "<div class='panel panel-default text-center'>"
                        html += "<div class='panel-heading'>"
                        html += "<b>"+str(gra[1])+"</b>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "<center><h6>Desertores "+str(vcarCur[index1][anio][gra[0]]['si'])+"</h6></center>"
                        html += "<center><h6>No desertores "+str(vcarCur[index1][anio][gra[0]]['no'])+"</h6></center>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html += "</div>"
                    html += "<br>"
    if accion1 == "diferencia_entre_primero_quinto":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = {}
        vaplaz = {}
        vareasApro = {}
        vareasApla = {}
        capro = 0
        caplaz = 0
        cdes = 0
        cndes = 0
        total = 0
        ctec = 0
        csal = 0
        csoc = 0
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        for anio in range(a1, a2 + (1)):
            vareasApro[anio]=[0]*n_are
            vareasApla[anio]=[0]*n_are
            vapro[anio]= [0] * n_car
            vaplaz[anio] = [0] * n_car

        #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if not isinstance(row[8], type(None)) and row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango
                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                if row[3] == 1:#contar los de primer año
                    capro += 1
                    vapro[anoBD][row[5]-1] += 1
                    vareasApro[anoBD][row[7]-1] += 1
                elif row[3] == 5 and row[1] == "aprobado":#contar los de 5to añp
                    caplaz += 1
                    vaplaz[anoBD][row[5]-1] += 1
                    vareasApla[anoBD][row[7]-1] += 1
        if si_car_n == "si_car_n":#esta buscando carreras
            mensaje = "La cantidad de estudiantes que concluyeron sus estudios en relacion a 1er año de las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                k = 0
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas

                    html += "<div class='col-lg-4 p-4' style = 'border: 1px solid black;background-color:RGBA(255, 250, 0, 0.5)'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'>Año "+str(anio)+"<h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Los estudiantes de 1er año son "+str(vapro[anio][index])+"</h6></center>"
                    html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vaplaz[anio][index])+"</h6></center>"
                    html += menCOncluyeron(vapro[anio][index],vaplaz[anio][index])
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            mensaje = "La cantidad de estudiantes que concluyeron sus estudios en relacion a 1er año en las siguientes areas son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area "+str(nombre_area_id(index1))+"<h5>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='col-lg-4' style = 'border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Los estudiantes de 1er año son "+str(vareasApro[anio][index])+"</h6></center>"
                    html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vareasApla[anio][index])+"</h6></center>"
                    html += menCOncluyeron(vareasApro[anio][index],vareasApla[anio][index])
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
        else:
            mensaje = "La cantidad de estudiantes que concluyeron sus estudios en relacion a 1er año"
            mensaje += " por áreas y carreras, detallamos en los siguientes cuadros"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            # Crear el gráfico de torta
            html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
            html += "<h5 align='center'>Total</h5>"
            html += "<div class='col-lg-12'>"
            html += "<div class='panel panel-default text-center bg-light' style = 'border: 1px solid black;'>"
            html += "<div class='panel-heading'>"
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><h6>Los estudiantes de 1er año son "+str(capro)+"</h6></center>"
            html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(caplaz)+"</h6></center>"
            html += menCOncluyeron(capro,caplaz)
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "<br>"
            #crear para areas

            html += "<h5 align='center'>Áreas</h5>"
            areas = seleccionarAreas()
            for are in areas:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                html += "<h6 align='center'>Área "+str(nombre_area_id(are[0]))+"</h6>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='col-lg-4' style='border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Los estudiantes de 1er año son "+str(vareasApro[anio][are[0]-1])+"</h6></center>"
                    html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vareasApla[anio][are[0]-1])+"</h6></center>"
                    html += menCOncluyeron(vareasApro[anio][are[0]-1],vareasApla[anio][are[0]-1])
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
            h = 1
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                html += "<h6 align = 'center'>Carrera</h6>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(car[0]))+"</h6>"
                html += "<div class='row' style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<div class='col-lg-4 p-4' style = 'border: 1px solid black;background-color:RGBA(255, 250, 0, 0.5)'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><h6>Los estudiantes de 1er año son "+str(vapro[anio][car[0]-1])+"</h6></center>"
                    html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vaplaz[anio][car[0]-1])+"</h6></center>"
                    html += menCOncluyeron(vapro[anio][car[0]-1],vaplaz[anio][car[0]-1])
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div><br>"

    if accion1 == 'asignaturas_desercion':
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vasigDeser={}
        vasigCar={}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()
        grado = seleccionarGrado()
        for area in areas:
            vasigDeser[area[0]]={}
            materias = seleccionarAsignaturaAreas(area[0],1)
            if materias != 'no':
                for anio in range(a1, a2 + (1)):
                    vasigDeser[area[0]][anio]={}
                    for mat in materias:
                        vasigDeser[area[0]][anio][mat[0]]={'si':0,'no':0,'asignatura':mat[2],'carrera':mat[8]}
        carreras = seleccionarCarrerasTodo()
        for car in carreras:
            vasigCar[car[0]] = {}
            materias = seleccionarAsignatura_por_id(car[0])
            if materias != 'no':
                for anio in range(a1, a2 + (1)):
                    vasigCar[car[0]][anio]={}
                    for gra in grado:
                        vasigCar[car[0]][anio][gra[0]]={}
                        for mat in materias:
                            if mat[9] == gra[0]:
                                vasigCar[car[0]][anio][gra[0]][mat[0]]={'si':0,'no':0,'asignatura':mat[2]}

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[14], type(None)) and  row[14]>=fecha1 and row[14] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
                if row[4] == 'si':#contar los de primer año
                    vasigDeser[row[12]][anoBD][row[8]][row[4]]+=1
                    vasigCar[row[10]][anoBD][row[11]][row[8]][row[4]]+=1
                elif row[4] == 'no':#contamos solo de 5to año y aprobados
                    vasigDeser[row[12]][anoBD][row[8]][row[4]]+=1
                    vasigCar[row[10]][anoBD][row[11]][row[8]][row[4]]+=1
        if si_car_n == "si_car_n":#esta buscando carreras
            mensaje = "Las asignaturas que tienen mas estudiantes desertores en las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h6 align = 'center'>Carrera</h6>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                asig = seleccionarAsignatura_por_id((index1))#seleccionamos las asiganturas con el cod id
                if asig != "no":
                    for anio in range(a1, a2 + 1):#recorremos las fechas
                        html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                        html += "<div class='row'>"#abrimos una fila
                        for gra in grado:#recorremos los cursos
                            html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                            html += "<div class='panel panel-default text-center'>"
                            html += "<div class='panel-heading'>"
                            html += "Curso "+str(gra[1])#imprimimos el curso
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html += "<table class='table table-striped' style='font-size: smaller;'>"
                            html += "<thead>"
                            html += "<tr>"
                            html += "<th>Asignatura</th>"
                            html += "<th>Deserciones</th>"
                            html += "</tr>"
                            html += "</thead>"
                            html += "<tbody>"
                            for asi in asig:#recorremos las asignaturas
                                if gra[0] == asi[9]:
                                    html += "<tr><td>"+str(vasigCar[index1][anio][gra[0]][asi[0]]['asignatura'])+"</td>"
                                    html += "<td>"+str(vasigCar[index1][anio][gra[0]][asi[0]]['si'])+"</td></tr>"
                            #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                            html += "<tbody>"
                            html += "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                    html += "</div>"
                    html += "<br>"
                else:
                    html += "<div class='col-lg-12' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html+="<h6>No se encontro información</h6>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
        elif si_ar == "si_ar":
            mensaje = "Las asignaturas que tienen mas estudiantes desertores en las siguientes areas son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                materias = seleccionarAsignaturaAreas(index1,1)
                if materias != "no":
                    html += "<div class='row'>"
                    for anio in range(a1, a2 + (1)):
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "Año "+str(anio)
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "<table class='table table-striped' style='font-size: smaller;'>"
                        html += "<thead>"
                        html += "<tr>"
                        html += "<th>Asignatura</th>"
                        html += "<th>Deserciones</th>"
                        html += "<th>Carrera</th>"
                        html += "</tr>"
                        html += "</thead>"
                        html += "<tbody>"
                        contar = 0
                        for asi in materias:
                            if vasigDeser[index1][anio][asi[0]]['si']>0:
                                html += "<tr><td>"+str(vasigDeser[index1][anio][asi[0]]['asignatura'])+"</td>"
                                html += "<td>"+str(vasigDeser[index1][anio][asi[0]]['si'])+"</td>"
                                html += "<td>"+str(vasigDeser[index1][anio][asi[0]]['carrera'])+"</td></tr>"
                                    #html += "<td>"+str(nombre_carrera(vareasT[i+1][asi[0]].get(1)))+"</td></tr>"
                                contar = 1
                        if contar == 0:
                            html+="<tr><td colspan='3'>No se encontro información</td></tr>"
                        html += "<tbody>"
                        html += "</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html += "</div>"
                else:
                    html+="<h6 align='center' style='background-color:khaki'>No se encontro información</h6>"

        else:
            mensaje = "Las asignaturas que tienen mas estudiantes desertores"
            mensaje += " por áreas y carreras, detallamos en los siguientes cuadros"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            # Crear el gráfico de torta

            #crear para areas

            html += "<h5 align='center'>Áreas</h5>"
            k1 = 1
            for are in areas:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                materias = seleccionarAsignaturaAreas(index1,1)
                if materias != "no":
                    html += "<div class='row'>"
                    for anio in range(a1, a2 + (1)):
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "Año "+str(anio)
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "<table class='table table-striped' style='font-size: smaller;'>"
                        html += "<thead>"
                        html += "<tr>"
                        html += "<th>Asignatura</th>"
                        html += "<th>Deserciones</th>"
                        html += "<th>Carrera</th>"
                        html += "</tr>"
                        html += "</thead>"
                        html += "<tbody>"
                        contar = 0
                        for asi in materias:
                            if vasigDeser[index1][anio][asi[0]]['si']>0:
                                html += "<tr><td>"+str(vasigDeser[index1][anio][asi[0]]['asignatura'])+"</td>"
                                html += "<td>"+str(vasigDeser[index1][anio][asi[0]]['si'])+"</td>"
                                html += "<td>"+str(vasigDeser[index1][anio][asi[0]]['carrera'])+"</td></tr>"
                                contar = 1
                        if contar == 0:
                            html+="<tr><td colspan='3'>No se encontro información</td></tr>"
                                    #html += "<td>"+str(nombre_carrera(vareasT[i+1][asi[0]].get(1)))+"</td></tr>"
                        html += "<tbody>"
                        html += "</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html += "</div>"
                else:
                    html+="<h6 align='center' style='background-color:khaki'>No se encontro información</h6>"

            for car in carreras:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h6 align = 'center'>Carrera</h6>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                asig = seleccionarAsignatura_por_id((index1))#seleccionamos las asiganturas con el cod id
                if asig != "no":
                    for anio in range(a1, a2 + 1):#recorremos las fechas
                        html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                        html += "<div class='row'>"#abrimos una fila
                        for gra in grado:#recorremos los cursos
                            html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                            html += "<div class='panel panel-default text-center'>"
                            html += "<div class='panel-heading'>"
                            html += "Curso "+str(gra[1])#imprimimos el curso
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html += "<table class='table table-striped' style='font-size: smaller;'>"
                            html += "<thead>"
                            html += "<tr>"
                            html += "<th>Asignatura</th>"
                            html += "<th>Deserciones</th>"
                            html += "</tr>"
                            html += "</thead>"
                            html += "<tbody>"
                            for asi in asig:#recorremos las asignaturas
                                if gra[0] == asi[9]:
                                    html += "<tr><td>"+str(vasigCar[index1][anio][gra[0]][asi[0]]['asignatura'])+"</td>"
                                    html += "<td>"+str(vasigCar[index1][anio][gra[0]][asi[0]]['si'])+"</td></tr>"
                            #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                            html += "<tbody>"
                            html += "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                    html += "</div>"
                    html += "<br>"
                else:
                    html += "<div class='col-lg-12' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html+="<h6>No se encontro información</h6>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
    if accion1 == "clasificado_sexo":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux

        vareas = {}
        vareasr = {}
        c_infor = {}
        c_inforr = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
            ##enviamos el id de la carrera y el plan de estudio
        for anio in range(a1, a2 + (1)):
            vareas[anio] = [0]*n_are
            vareasr[anio] = [0]*n_are
        for anio in range(a1, a2 + (1)):
            c_infor[anio] = [0]*n_car
            c_inforr[anio] = [0]*n_car

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                if row[11] == 'masculino':#contar los de primer año
                    vareas[anoBD][row[12]-1]+=1
                    c_infor[anoBD][row[13]-1]+=1
                elif row[11] == 'femenino':#contar los de 5to añp
                    vareasr[anoBD][row[12]-1]+=1
                    c_inforr[anoBD][row[13]-1]+=1

        colorr ={0:'beige',1:'Gainsboro',2:'Khaki',3:'Lavender',4:'LightYellow'}
        if si_car_n == "si_car_n":#esta buscando carreras
            mensaje = "La cantidad de estudiantes clasificado por varones y mujeres de las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):#recoremos los anos que pueden sere desde una año inicio a un año fin
                    html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<table class='table table-striped' style='font-size: smaller;'>"
                    html += "<thead>"
                    html += "<tr>"
                    html += "<th>Varones</th>"
                    html += "<th>Mujeres</th>"
                    html += "</tr>"
                    html += "</thead>"
                    html += "<tbody>"

                    html += "<tr><td>"+str(c_infor[anio][index])+"</td>"
                    html += "<td>"+str(c_inforr[anio][index])+"</td></tr>"
                                      #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                    html += "<tbody>"
                    html += "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"

                html += "</div>"
                html += "<br>"
        elif si_ar == "si_ar":
            mensaje = "La cantidad de estudiantes clasificado por varones y mujeres de las siguientes áreas son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            s_dupli = eliminar_dobles(id_ar)#
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"

                html += "<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<table class='table table-striped' style='font-size: smaller;'>"
                    html += "<thead>"
                    html += "<tr>"
                    html += "<th>Varones</th>"
                    html += "<th>Mujeres</th>"
                    html += "</tr>"
                    html += "</thead>"
                    html += "<tbody>"
                    html += "<tr><td>"+str(vareas[anio][index])+"</td>"
                    html += "<td>"+str(vareasr[anio][index])+"</td></tr>"
                    html += "<tbody>"
                    html += "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
        else:
            mensaje = "La cantidad de estudiantes clasificado por varones y mujeres"
            mensaje += " detallamos en los siguientes cuadros por áreas y carreras"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            # Crear el gráfico de torta

            #crear para areas

            html += "<h5 align='center'>Áreas</h5>"
            areas = seleccionarAreas()
            for are in areas:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                html += "<h6 align='center'>Área "+str(nombre_area_id(are[0]))+"</h6>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<table class='table table-striped' style='font-size: smaller;'>"
                    html += "<thead>"
                    html += "<tr>"
                    html += "<th>Varones</th>"
                    html += "<th>Mujeres</th>"
                    html += "</tr>"
                    html += "</thead>"
                    html += "<tbody>"
                    html += "<tr><td>"+str(vareas[anio][are[0]-1])+"</td>"
                    html += "<td>"+str(vareasr[anio][are[0]-1])+"</td></tr>"
                    html += "<tbody>"
                    html += "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br>"
            h = 1
            html += "<h5 align='center'>Carreras</h5>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                html+="<h5 align='center'>Carrera "+str(nombre_carrera_retor(car[0]))+"</h5>"#nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):#recoremos los anos que pueden sere desde una año inicio a un año fin
                    html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<table class='table table-striped' style='font-size: smaller;'>"
                    html += "<thead>"
                    html += "<tr>"
                    html += "<th>Varones</th>"
                    html += "<th>Mujeres</th>"
                    html += "</tr>"
                    html += "</thead>"
                    html += "<tbody>"

                    html += "<tr><td>"+str(c_infor[anio][car[0]-1])+"</td>"
                    html += "<td>"+str(c_inforr[anio][car[0]-1])+"</td></tr>"
                                      #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                    html += "<tbody>"
                    html += "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                h = h + 1
                html += "</div>"
                html += "<br>"

    if accion1 == "transferencias_buscar":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vanio = {}
        vcaranio={}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        for anio in range(a1, a2 + (1)):
            vanio[anio] = [0]*n_are
            vcaranio[anio] = [0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[4], type(None)) and row[4]>=fecha1 and row[4] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[4].strftime("%Y-%m-%d")))
                vanio[anoBD][row[6]-1] +=1
                vcaranio[anoBD][row[7]-1] +=1
        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" de la siguiente carrera"
            else:
                mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" de las siguientes carreras"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcaranio[anio][index])+" Estudiantes transferidos"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":

            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" de la siguiente área"
            else:
                mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" de las siguientes áreas"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vanio[anio][index])+" Estudiantes transfereridos"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
                # Crear el gráfico de torta

                #crear para areas

            html += "<h6 align='center'>TRANSFERENCIAS POR AÑO</h6>"
            k1 = 1
            areas = seleccionarAreas()

            for ar in areas:
                html += "<h6 align='center'>Área "+nombre_area_id(ar[0])+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vanio[anio][ar[0]-1])+" Estudiantes transferidos"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br><br>"
            html += "<h6 align='center'>CARRERAS</h6>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:
                html += "<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcaranio[anio][car[0]-1])+" Estudiantes transferidos"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
                html += "<br><br>"
    if accion1 == "concepto_transferencia":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vanio = {}
        vcaranio = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        for anio in range(a1, a2 + (1)):
            vanio[anio]=[0]*n_are
            vcaranio[anio]=[0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[4], type(None)) and row[4]>=fecha1 and row[4] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[4].strftime("%Y-%m-%d")))
                vanio[anoBD][row[14]-1] +=1
                vcaranio[anoBD][row[12]-1] +=1
        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "Los estudiantes transferidos de otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" en total de la siguiente carrera"
            else:
                mensaje = "Los estudiantes transferidos de otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" en total de las siguientes carreras"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los transferidos fueron "+str(vcaranio[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":

            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "Los estudiantes transferidos de otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" en total en la siguiente área"
            else:
                mensaje = "Los estudiantes transferidos de otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)+" en total de las siguientes áreas"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los transferidos fueron "+str(vanio[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            mensaje = "Los estudiante transferidos de otras Universidades desde el año "+str(a1)+" al año "+str(a2)
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            # Crear el gráfico de torta
            #crear para areas
            html += "<h6 align='center'>TRANSFERENCIAS POR AÑO</h6>"
            html += "<h6 align='center'>ÁREAS</h6>"
            k1 = 1
            areas = seleccionarAreas()
            for ar in areas:#recorremos todo los id de areas
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(ar[0])+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los transferidos fueron "+str(vanio[anio][ar[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            carreras = seleccionarCarrerasTodo()
            html += "<h6 align='center'>CARRERAS</h6>"
            for car in carreras:
                html += "<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los transferidos fueron "+str(vcaranio[anio][car[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html += "<br><br>"
    if accion1 == "mayor_inscritos":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
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
            vanio[anio]=[0]*n_are
            carreras[anio] = [0]*n_car

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                if row[14] == 1:
                    anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                    vanio[anoBD][row[12]-1]+=1#en cada año y area sumamos mas 1
                    carreras[anoBD][row[13]-1]+=1
        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La información sobre cuantos inscritos tiene la carrera se mostrara en los siguientes cuadros"
            else:
                mensaje = "La información sobre cuantos inscritos tiene la carreras se mostrara en los siguientes cuadros"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los inscritos fueron "+str(carreras[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":

            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La información sobre cuantos inscritos tiene el área se mostrara en los siguientes cuadros"
            else:
                mensaje = "La información sobre cuantos inscritos tiene las áreas se mostrara en los siguientes cuadros"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los inscritos fueron "+str(vanio[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:

            mensaje = "La información cuantos inscritos existen por áreas y carreras lo detallamos en los siguientes cuadros"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            html += "<button onclick='generar()'>Generar</button>"
            html += "<script>"
            html += "function generar(){"
            html +="const formulario = document.createElement('form');"
            html +="formulario.style.display = 'none';"
            html +="formulario.method = 'POST';"
            html +="formulario.action = '/generar_reporte';"
            html +="const campoDatos = document.createElement('input');"
            html +="campoDatos.type = 'hidden';"
            html +="campoDatos.name = 'datos';"
            html +="campoDatos.value = "+str(ress)+";"
            html +="formulario.appendChild(campoDatos);"
            html +="document.body.appendChild(formulario);"
            html +="formulario.submit();"
            html += "}"
            html += "</script>"
            #crear ara areas
            html += "<h6 align='center'>Áreas</h6>"
            k1 = 1
            areas = seleccionarAreas()
            for ar in areas:#recorremos todo los id de areas
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(ar[0])+"</h6>"
                html += "<div class='row'style = 'border: 1px solid black;'>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los inscritos fueron "+str(vanio[anio][ar[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html += "<br><br>"
            carreras1 = seleccionarCarrerasTodo()
            html += "<h6 align='center'>Carreras</h6>"
            for car in carreras1:#recorremos todo los id carreras puede ser 12,1,9
                html += "<h6 align = 'center'> Carrera "+str(nombre_carrera_retor(car[0]))+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Los inscritos fueron "+str(carreras[anio][car[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html += "<br><br>"
    if accion1 == "modalidad_titulacion":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        vareas = ['']*n_are
        vcarreras = ['']*n_car
        for row in datos:
            if row[2] != 2 and row[3] == 1:
                vcarreras[row[3]-1]=vcarreras[row[3]-1]+"|"+str(row[1])
            elif row[2] != 2:
                vcarreras[row[3]-1]=vcarreras[row[3]-1]+"|"+str(row[1])

        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La modalidad de titulación de la carrera es"
            else:
                mensaje = "Las modalidades de titulación de las siguientes carreras son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            html += "<div class='row'>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += "<h5 align = 'center'>Carrera "+str(nombre_carrera_retor(index1))+"</h5>"
                html += "</div>"
                html += "<div class='panel-body'>"
                html+= "<table class='table'>"
                html+= "<thead>"
                html+="<tr>"
                html+="<td>Nro</td>"
                html+="<td>Titulación</td>"
                html+="</tr>"
                html+="</thead>"
                html+="<tbody>"
                nombre_modalidad = separar_guiones(vcarreras[index])
                k = 1
                if not nombre_modalidad:
                    html += "<tr>"
                    html += "<td colspan='2' style='text-align:center;'>No se encontró información</td>"
                    html += "</tr>"
                else:
                    for name in nombre_modalidad:
                        html += "<tr>"
                        html+="<td>"+str(k)+"</td>"
                        k=k+1
                        html+="<td>"+name+"</td>"
                        html+="</tr>"
                html+="</tbody>"
                html+= "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
            html+="</div>"

        elif si_ar == "si_ar":

            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La modalidad de titulación del área son"
            else:
                mensaje = "Las modalidades de titulación de las siguientes áreas son"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            print(s_dupli,"vector ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                carreras = seleccionarcarrera_id(index1)
                html += "<div class='row'>"
                for car in carreras:
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align = 'center'>Carrera "+str(nombre_carrera_retor(car[0]))+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Nro</td>"
                    html+="<td>Titulación</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    nombre_modalidad = separar_guiones(vcarreras[car[0]-1])
                    k = 1
                    if not nombre_modalidad:
                        html += "<tr>"
                        html += "<td colspan='2' style='text-align:center;'>No se encontró información</td>"
                        html += "</tr>"
                    else:
                        for name in nombre_modalidad:
                            html += "<tr>"
                            html+="<td>"+str(k)+"</td>"
                            k=k+1
                            html+="<td>"+name+"</td>"
                            html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html+="</div>"
        else:
            mensaje = ''
            mensaje+="<h6>MODALIDADES DE TITULACIÓN</h6>"
            html+=mensaje
            html += "<button onclick='generar()' class='btn btn-warning'>Reporte</button><br><br>"
            html += "<script>"
            html += "function generar(){"
            html +="const formulario = document.createElement('form');"
            html +="formulario.style.display = 'none';"
            html +="formulario.method = 'POST';"
            html +="formulario.action = '/generar_reporte';"
            html +="const campoDatos = document.createElement('input');"
            html +="campoDatos.type = 'hidden';"
            html +="campoDatos.name = 'datos';"
            html +="campoDatos.value = "+str(ress)+";"
            html +="formulario.appendChild(campoDatos);"

            html +="document.body.appendChild(formulario);"
            html +="formulario.submit();"
            html += "}"
            html += "</script>"
            areas = seleccionarAreas()
            for ar in areas:#recorremos todo los id de areas
                html += "<h6 align='center'>Área "+nombre_area_id(ar[0])+"</h6>"
                carreras = seleccionarcarrera_id(ar[0])
                html+="<div class='row'>"
                for car in carreras:
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Nro</td>"
                    html+="<td>Titulación</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    k = 1
                    nombre_modalidad = separar_guiones(vcarreras[car[0]-1])
                    print("modalida de titulacion  ",nombre_modalidad)
                    if not nombre_modalidad:
                        html += "<tr>"
                        html += "<td colspan='2' style='text-align:center;'>No se encontró información</td>"
                        html += "</tr>"
                    else:
                        for name in nombre_modalidad:
                            html += "<tr>"
                            html+="<td>"+str(k)+"</td>"
                            k=k+1
                            html+="<td>"+name+"</td>"
                            html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html+="</div><br>"
    if accion1 == "total_estudiante_desercion":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vareas = {}
        vareasno = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        carreras = {}
        carrerasno = {}
        for anio in range(a1, a2 + (1)):
            vareas[anio]=[0]*n_are
            vareasno[anio]=[0]*n_are
        for anio in range(a1, a2 + (1)):
            carreras[anio] = [0]*n_car
            carrerasno[anio] = [0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[8], type(None)) and row[8]>=fecha1 and row[8] <= fecha2:
                if row[2] == "si":
                    anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                    vareas[anoBD][row[7]-1]+=1#en cada año y area sumamos mas 1
                    carreras[anoBD][row[5]-1]+=1
                elif row[2] == "no":
                    anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                    carrerasno[anoBD][row[5]-1]+=1
                    vareasno[anoBD][row[5]-1]+=1
        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La información sobre desercion estudiantil de la carrera es"
            else:
                mensaje = "La información sobre desercion estudiantil de las carreras es"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "La deserción estudiantil es de "+str(carreras[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html+="</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La información sobre desercion estudiantil del área es"
            else:
                mensaje = "La información sobre desercion estudiantil de los áreas son"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Area "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "La deserción estudiantil es de "+str(vareas[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            mensaje = "La información sobre desercion estudiantil en areas y carreras es lo siguiente"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            #crear para areas

            html += "<h6 align='center'style='color:black'>Areas</h6>"
            k1 = 1

            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(are[0])+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "La deserción estudiantil es de "+str(vareas[anio][are[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"


            html += "<h6 align='center'style='color:black'>Carreras</h6>"
            carreras1 = seleccionarCarrerasTodo()
            for car in carreras1:
                k = 1
                html += "<h6 align='center'style='color:black'>Carrera "+nombre_carrera_retor(car[0])+"</h6>"
                html+="<div class='row'>"

                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "La deserción estudiantil es de "+str(carreras[anio][car[0]-1])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html+="</div>"
    if accion1 == "titulados_relacion":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        consultaTitulado = ress[7]
        titulados_re= consulta_Titulado(consultaTitulado)
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vareas = {}
        vareasTitu = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        carreras = {}
        carrerasTitu = {}
        for anio in range(a1, a2 + (1)):
            vareas[anio]=[0]*n_are
            vareasTitu[anio]=[0]*n_are
        for anio in range(a1, a2 + (1)):
            carreras[anio] = [0]*n_car
            carrerasTitu[anio] = [0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                if row[14] ==1:
                    anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                    carreras[anoBD][row[13]-1]+=1
                    vareas[anoBD][row[12]-1]+=1

        for row in titulados_re:
            if not isinstance(row[9], type(None)) and row[9]>=fecha1 and row[9] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[9].strftime("%Y-%m-%d")))
                carrerasTitu[anoBD][row[7]-1]+=1
                vareasTitu[anoBD][row[8]-1]+=1

        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "En los siguientes cuadros detallamos los titulados con relación a los primeros niveles de la siguiente carrera"
            else:
                mensaje = "En los siguientes cuadros detallamos los titulados con relación a los primeros niveles de las siguientes carreras"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>1er año</td>"
                    html+="<td>Titulados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(carreras[anio][index])+"</td>"
                    html+="<td>"+str(carrerasTitu[anio][index])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"

        elif si_ar == "si_ar":

            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "En los siguientes cuadros detallamos los titulados con relación a los primeros niveles de la siguiente área"
            else:
                mensaje = "En los siguientes cuadros detallamos los titulados con relación a los primeros niveles de las siguientes áreas"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>1er año</td>"
                    html+="<td>Titulados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vareas[anio][index])+"</td>"
                    html+="<td>"+str(vareasTitu[anio][index])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:

            mensaje = "En los siguientes cuadros detallamos los titulados con relacion a los primeros niveles"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            #crear para areas

            html += "<h6 align='center'style='color:black'>Areas</h6>"
            k1 = 1
            html += "<div class='row'>"
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(are[0])+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>1er año</td>"
                    html+="<td>Titulados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vareas[anio][are[0]-1])+"</td>"
                    html+="<td>"+str(vareasTitu[anio][are[0]-1])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html += "<h6 align='center'style='color:black'>Carreras</h6>"
            carreras1 = seleccionarCarrerasTodo()
            for car in carreras1:#recorremos todo los id carreras puede ser 12,1,9
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h5 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h5>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>1er año</td>"
                    html+="<td>Titulados</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(carreras[anio][index])+"</td>"
                    html+="<td>"+str(carrerasTitu[anio][index])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"

    if accion1 == "clasificacion_departamento":
        total = len(datos)
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux

        region  = ['Occidente',"Central","Oriente"]
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        depar = {}
        occidente = {}
        cdepar = {}
        coccidente = {}
        for anio in range(a1, a2 + (1)):
            occidente[anio]={}
            depar[anio] = {}
            areas = seleccionarAreas()
            for are in areas:
                occidente[anio][are[0]] = [0]*3
                depar[anio][are[0]] = [0]*9
        for anio in range(a1, a2 + (1)):
            cdepar[anio] = {}
            coccidente[anio] = {}
            carrer = seleccionarCarrerasTodo()
            for car in carrer:
                cdepar[anio][car[0]] = [0]*9
                coccidente[anio][car[0]] = [0]*3
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                if row[7].lower().strip() == 'oruro':
                    depar[anoBD][row[12]][0]+=1
                    cdepar[anoBD][row[13]][0]+=1
                elif row[7].lower().strip() == 'potosi':
                    depar[anoBD][row[12]][1]+=1
                    cdepar[anoBD][row[13]][1]+=1
                elif row[7].lower().strip() == 'la paz':
                    depar[anoBD][row[12]][2]+=1
                    cdepar[anoBD][row[13]][2]+=1
                elif row[7].lower().strip() == 'cochabamba':
                    depar[anoBD][row[12]][3]+=1
                    cdepar[anoBD][row[13]][3]+=1
                elif row[7].lower().strip() == 'santa cruz':
                    depar[anoBD][row[12]][4]+=1
                    cdepar[anoBD][row[13]][4]+=1
                elif row[7].lower().strip() == 'beni':
                    depar[anoBD][row[12]][5]+=1
                    cdepar[anoBD][row[13]][5]+=1
                elif row[7].lower().strip() == 'tarija':
                    depar[anoBD][row[12]][6]+=1
                    cdepar[anoBD][row[13]][6]+=1
                elif row[7].lower().strip() == 'chuquisaca':
                    depar[anoBD][row[12]][7]+=1
                    cdepar[anoBD][row[13]][7]+=1
                elif row[7].lower().strip() == 'pando':
                    depar[anoBD][row[12]][8]+=1
                    cdepar[anoBD][row[13]][8]+=1

                if row[10].lower().strip() == "occidente":
                    occidente[anoBD][row[12]][0]+=1
                    coccidente[anoBD][row[13]][0]+=1
                elif row[10].lower().strip() == "central":
                    occidente[anoBD][row[12]][1]+=1
                    coccidente[anoBD][row[13]][1]+=1
                elif row[10].lower().strip() == "oriente":
                    occidente[anoBD][row[12]][2]+=1
                    coccidente[anoBD][row[13]][2]+=1
        if si_car_n == "si_car_n":#esta buscando carreras
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La cantidad de estudiantes clasificados por departamentos y regiones de la carrera son"
            else:
                mensaje = "La cantidad de estudiantes clasificados por departamentos y regiones de las carreras son"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            html += "<div class='alert alert-secondary'>Regiones</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for reg in region:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += reg
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(coccidente[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "<div class='alert alert-secondary'>Departamentos</div>"
            for i in s_dupli:#recorremos todo los id carreras puede ser 12,1,9
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for dep in departamento:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += dep
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(cdepar[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                mensaje = "La cantidad de estudiantes clasificados por departamentos y regiones del área son"
            else:
                mensaje = "La cantidad de estudiantes clasificados por departamentos y regiones de los áreas son"

            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            html += "<div class='alert alert-secondary'>Regiones</div>"
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for reg in region:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += reg
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(occidente[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "<div class = 'alert alert-secondary'>Departamentos</div>"
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for dep in departamento:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += dep
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(depar[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
        else:

            mensaje = "Detallaremos en los siguientes cuadros sobre estudiantes a que departamento y region pertencen"
            html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
                #crear para areas
            html += "<div align='center'class='alert alert-secondary'>Areas</div>"
            html += "<div class='alert alert-secondary'>Regiones</div>"
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Área "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for reg in region:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += reg
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(occidente[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "<div align='center'class='alert alert-secondary'>Areas</div>"
            html += "<div class='alert alert-secondary'>Departamentos</div>"
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                #seleccionamos las asingturas con el cod de area
                html += "<h6 align='center'>Area "+nombre_area_id(index1)+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for dep in departamento:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += dep
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(depar[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "<div align='center'class='alert alert-secondary'>Carreras</div>"
            html += "<div class='alert alert-secondary'>Regiones</div>"
            carreras1 = seleccionarCarrerasTodo()
            for car in carreras1:#recorremos todo los id carreras puede ser 12,1,9
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for reg in region:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += reg
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(coccidente[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "<div align='center'class='alert alert-secondary'>Carreras</div>"
            html += "<div class='alert alert-secondary'>Departamentos</div>"
            for car in carreras1:#recorremos todo los id carreras puede ser 12,1,9
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h5 align = 'center'>Carrera</h5>"
                html += "<h6 align = 'center'>"+str(nombre_carrera_retor(index1))+"</h6>"
                html += "<div class = 'row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
                    k = 0
                    for dep in departamento:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += dep
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+=""+str(cdepar[anio][index1][k])+" estudiantes"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                        k = k + 1
                html += "</div><br>"
            html += "</div><br>"

    if accion1 == "plan_de_estudio":
        si_ar = ress[0]
        id_ar  = ress[1]
        si_car_n = ress[2]
        id_car   = ress[3]

        si_total = ress[4]
        curs ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        if si_ar == "si_ar":#si es diferente de no existe una area o areas
            #obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<br><h5 align='center'>Area " + str(areasU[index])+"</h5>"
                print("index   ",index1)
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html+="<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+" plan de estudio</h6>"#impirmimos el nombre de la carrera
                        asig=seleccionarAsignatura_por_id(car[0])#seleccionamos las asignaturas
                        mt = modalidad_titulacion_id(car[0])#seleccinamos la modalidad de titulacion
                        if asig != "no":
                            html+="<div class='row'>"
                            grado = seleccionarGrado()
                            for gra in grado:
                                html += "<div class='col-lg-6'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += "Curso "+str(gra[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size: 12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Sigla</td>"
                                html+="<td>Asignatura</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                p = 1
                                for asigg in asig:
                                    html+="<tr>"
                                    if gra[0] == asigg[9]:#si el curso de asignatura es igual a k entonces
                                        html+="<td>"+str(p)+"</td>"
                                        p = p + 1
                                        html+="<td>"+str(asigg[1])+"</td>"
                                        html+="<td>"+str(asigg[2])+"</td>"
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html+="<h5 align='center'>Modalidades de titulación<h5>"
                            html+="</div>"
                            html+="<div class='row'>"
                            j = 1
                        if mt != "no":
                            html += "<div class='col-lg-12'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html+= "<table class='table' style='font-size:12px'>"
                            html+= "<thead>"
                            html+="<tr>"
                            html+="<td>N°</td>"
                            html+="<td>Modalidad</td>"
                            html+="</tr>"
                            html+="</thead>"
                            html+="<tbody>"
                            for moda in mt:
                                html+="<tr>"
                                html+="<td>"+str(j)+"</td>"
                                j = j + 1
                                html+="<td>"+str(moda[1])+"</td>"
                                html+="</tr>"
                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                            html+="</div>"
                        else:
                            html+="<h6 align='center'>No se encontro resultados<h6>"
                else:
                    html+="<h6 align='center'>No se encontro resultados<h6>"
        elif si_car_n == "si_car":#si carrera es diferente de no entonces existe carrera
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+" plan de estudio</h6><br>"#impirmimos el nombre de la carrera
                asig=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                mt = modalidad_titulacion_id(index1)#seleccinamos la modalidad de titulacion
                if asig != "no":
                    html+="<div class='row'>"
                    grado = seleccionarGrado()
                    for gra in grado:
                        html += "<div class='col-lg-6'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html +="Curso "+str(gra[1])
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+= "<table class='table' style='font-size: 12px'>"
                        html+= "<thead>"
                        html+="<tr>"
                        html+="<td>N°</td>"
                        html+="<td>Sigla</td>"
                        html+="<td>Asignatura</td>"
                        html+="</tr>"
                        html+="</thead>"
                        html+="<tbody>"
                        p = 1
                        for asigg in asig:
                            html+="<tr>"
                            if gra[0] == asigg[9]:#si el curso de asignatura es igual a k entonces
                                html+="<td>"+str(p)+"</td>"
                                p = p + 1
                                html+="<td>"+str(asigg[1])+"</td>"
                                html+="<td>"+str(asigg[2])+"</td>"
                            html+="</tr>"
                        html+="</tbody>"
                        html+= "</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html+="<h5 align='center'>Modalidades de titulación<h5>"
                    html+="</div>"
                    html+="<div class='row'>"
                    j = 1
                else:
                    html+="<h6 align='center'>No se encontro resultados<h6>"
                if mt != "no":
                    html += "<div class='col-lg-12'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>N°</td>"
                    html+="<td>Modalidad</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    for moda in mt:
                        html+="<tr>"
                        html+="<td>"+str(j)+"</td>"
                        j = j + 1
                        html+="<td>"+str(moda[1])+"</td>"
                        html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                    html+="</div>"


        else:#no hay ni carrera ni area pero si existe plan de estudio
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<br><h5 align='center'>Area " + str(areasU[index])+"</h5><br>"
                print("index   ",index1)
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html+="<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+" plan de estudio</h6>"#impirmimos el nombre de la carrera
                        asig=seleccionarAsignatura_por_id(car[0])#seleccionamos las asignaturas
                        mt = modalidad_titulacion_id(car[0])#seleccinamos la modalidad de titulacion
                        if asig != "no":
                            html+="<div class='row'>"
                            grado = seleccionarGrado()
                            for gra in grado:
                                html += "<div class='col-lg-6'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += "Curso "+str(gra[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size: 12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Sigla</td>"
                                html+="<td>Asignatura</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                p = 1
                                for asigg in asig:
                                    html+="<tr>"
                                    if gra[0] == asigg[9]:#si el curso de asignatura es igual a k entonces
                                        html+="<td>"+str(p)+"</td>"
                                        p = p + 1
                                        html+="<td>"+str(asigg[1])+"</td>"
                                        html+="<td>"+str(asigg[2])+"</td>"
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html+="<h5 align='center'>Modalidades de titulación<h5>"
                            html+="</div>"
                            html+="<div class='row'>"
                            j = 1
                        if mt != "no":
                            html += "<div class='col-lg-12'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html+= "<table class='table' style='font-size:12px'>"
                            html+= "<thead>"
                            html+="<tr>"
                            html+="<td>N°</td>"
                            html+="<td>Modalidad</td>"
                            html+="</tr>"
                            html+="</thead>"
                            html+="<tbody>"
                            for moda in mt:
                                html+="<tr>"
                                html+="<td>"+str(j)+"</td>"
                                j = j + 1
                                html+="<td>"+str(moda[1])+"</td>"
                                html+="</tr>"
                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                            html+="</div>"
                        else:
                            html+="<h6 align='center'>No se encontro resultados<h6>"
                else:
                    html+="<h6 align='center'>No se encontro resultados<h6>"
    if accion1 == "materias_inscritos":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar={}
        vare = {}

        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        carreras = seleccionarCarrerasTodo()
        for car in carreras:
            vcar[car[0]]={}
            asig = seleccionarAsignatura(car[0],1)##enviamos el id de la carrera y el plan de estudio
            if asig != "no":
                for anio in range(a1, a2 + (1)):
                    vcar[car[0]][anio]={}
                    grado = seleccionarGrado()
                    for gra in grado:
                        vcar[car[0]][anio][gra[0]]={}
                        for arr in asig:
                            vcar[car[0]][anio][gra[0]][arr[0]]={'inscritos':0,'materia':arr[2]}

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()

        for row in datos:#recorremos los datos obtenidos de la base de datos

            if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
                if row[8] != '' or row[8] is not None:
                    vcar[row[10]][anoBD][row[11]][row[8]]['inscritos']+=1
        si_are = ress[0]
        if si_ar == "si_ar":#si es diferente de no existe una area o areas
            #obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Área " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            html += "<h5 align='center'>Carrera " + str(car[1])+"</h5>"
                            html+="<div class='row'>"
                            for anio in range(a1, a2 + (1)):
                                html += "<h6 align='center'>" + str(anio)+"</h6>"
                                grado = seleccionarGrado()
                                for gra in grado:
                                    html += "<div class='col-lg-4'>"
                                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                    html += "<div class='panel-heading'>"
                                    cur = gra[0]
                                    print(cur," = ",car[0])
                                    fech1 = str(anio)+"-01-01"
                                    fech2 = str(anio)+"-12-30"
                                    html += str(gra[1])
                                    html += "</div>"
                                    html += "<div class='panel-body'>"
                                    html+= "<table class='table' style='font-size:12px'>"
                                    html+= "<thead>"
                                    html+="<tr>"
                                    html+="<td>Asignatura</td>"
                                    html+="<td>Inscritos</td>"
                                    html+="</tr>"
                                    html+="</thead>"
                                    html+="<tbody>"
                                    k = 1
                                    for mat in materias:
                                        if gra[0] == mat[9]:#si el grado actual es igula a 1, 2 o etc ingresa
                                            html+="<tr><td>"+(vcar[car[0]][anio][gra[0]][mat[0]]['materia'])+"</td>"
                                            html+="<td>"+str(vcar[car[0]][anio][gra[0]][mat[0]]['inscritos'])+"</td></tr>"

                                    html+="</tbody>"
                                    html+= "</table>"
                                    html += "</div>"
                                    html += "</div>"
                                    html += "</div>"
                            html+="</div>"
                        else:
                            html+="<br><h6 align='center'>Carrera "+str(car[1])+"</h6><br>"#impirmimos el nombre de la carrera

                            html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"

                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"


        elif si_car_n == "si_car_n":

            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                materias=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                if materias != "no":
                    html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera

                    html+="<div class='row'>"
                    for anio in range(a1, a2 + (1)):
                        html += "<h6 align='center'>" + str(anio)+"</h6>"
                        grado = seleccionarGrado()
                        for gra in grado:
                            html += "<div class='col-lg-4'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            cur = gra[0]
                            fech1 = str(anio)+"-01-01"
                            fech2 = str(anio)+"-12-30"
                            html += "Curso "+str(gra[1])
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html+= "<table class='table' style='font-size:12px'>"
                            html+= "<thead>"
                            html+="<tr>"
                            html+="<td>Asignatura</td>"
                            html+="<td>Inscritos</td>"
                            html+="</tr>"
                            html+="</thead>"
                            html+="<tbody>"
                            k = 1
                            for mat in materias:
                                if gra[0] == mat[9]:#si el grado actual es igula a 1, 2 o etc ingresa
                                    html+="<tr><td>"+(vcar[index1][anio][gra[0]][mat[0]]['materia'])+"</td>"
                                    html+="<td>"+str(vcar[index1][anio][gra[0]][mat[0]]['inscritos'])+"</td></tr>"

                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                    html+="</div>"
                else:
                    html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera

                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
        else:#si es diferente de no existe una area o areas
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0]-1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas

                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            html += "<h5 align='center'>Carrera " + str(car[1])+"</h5>"
                            html+="<div class='row'>"
                            for anio in range(a1, a2 + (1)):
                                html += "<h6 align='center'>" + str(anio)+"</h6>"
                                grado = seleccionarGrado()
                                for gra in grado:
                                    html += "<div class='col-lg-4'>"
                                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                    html += "<div class='panel-heading'>"
                                    cur = gra[0]
                                    print(cur," = ",car[0])
                                    fech1 = str(anio)+"-01-01"
                                    fech2 = str(anio)+"-12-30"
                                    html += gra[1]
                                    html += "</div>"
                                    html += "<div class='panel-body'>"
                                    html+= "<table class='table' style='font-size:12px'>"
                                    html+= "<thead>"
                                    html+="<tr>"
                                    html+="<td>Asignatura</td>"
                                    html+="<td>Inscritos</td>"
                                    html+="</tr>"
                                    html+="</thead>"
                                    html+="<tbody>"
                                    k = 1
                                    for mat in materias:
                                        if gra[0] == mat[9]:#si el grado actual es igula a 1, 2 o etc ingresa
                                            html+="<tr><td>"+(vcar[car[0]][anio][gra[0]][mat[0]]['materia'])+"</td>"
                                            html+="<td>"+str(vcar[car[0]][anio][gra[0]][mat[0]]['inscritos'])+"</td></tr>"

                                    html+="</tbody>"
                                    html+= "</table>"
                                    html += "</div>"
                                    html += "</div>"
                                    html += "</div>"
                            html+="</div>"
                        else:
                            html+="<br><h6 align='center'>Carrera "+str(car[1])+"</h6><br>"#impirmimos el nombre de la carrera
                            html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"

                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"


    if accion1 == "asignaturas":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_grado = ress[2]
        id_grado = ress[3]
        si_ar = ress[4]
        id_ar  = ress[5]
        si_total = ress[6]

        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            existe = "no"
            if si_grado == "si_grado":
                existe = "si"
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                materias=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera

                if materias != "no":
                    if existe == "si":
                        curso = eliminar_dobles(id_grado)
                    else:
                        curso = seleccionarGrado()
                    html+="<div class='row'>"
                    for cur in curso:
                        if existe == "si":
                            id = int(cur)
                        else:
                            id = cur[0]
                        k = 1
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += " Curso "+str(NOmbredeGrado_por_id(id))
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html+= "<table class='table' style='font-size:12px'>"
                        html+= "<thead>"
                        html+="<tr>"
                        html+="<td>N°</td>"
                        html+="<td>Sigla</td>"
                        html+="<td>Asignatura</td>"
                        html+="</tr>"
                        html+="</thead>"
                        html+="<tbody>"
                        for asi in materias:
                            html+="<tr>"
                            if asi[9] == id:
                                html+="<td>"+str(k)+"</td>"
                                html+="<td>"+asi[1]+"</td>"
                                html+="<td>"+asi[2]+"</td>"
                                k = k + 1
                            html+="</tr>"
                        html+="</tbody>"
                        html+= "</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                    html+="<div>"
                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
        elif si_ar == "si_ar":#si es diferente de no existe una area o areas
            #obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html += "<h6 align='center'>Carrera " + str(nombre_carrera_retor(car[0]))+"</h6>"
                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            curso = seleccionarGrado()
                            html+="<div class='row'>"
                            for cur in curso:
                                k = 1
                                id=cur[0]
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(cur[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Sigla</td>"
                                html+="<td>Asignatura</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asi in materias:
                                    html+="<tr>"
                                    if asi[9] == id:
                                        html+="<td>"+str(k)+"</td>"
                                        html+="<td>"+asi[1]+"</td>"
                                        html+="<td>"+asi[2]+"</td>"
                                        k = k + 1
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html += "</div>"
                        else:
                            html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
        else:
            areas = seleccionarAreas()
            for i in areas:#recorremos todo los id de areas
                index = i[0] - 1#obtenemos el id
                index1 = i[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html += "<h6 align='center'>Carrera " + str(nombre_carrera_retor(car[0]))+"</h6>"
                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            curso = seleccionarGrado()
                            html+="<div class='row'>"
                            for cur in curso:
                                k = 1
                                id=cur[0]
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(cur[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Sigla</td>"
                                html+="<td>Asignatura</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asi in materias:
                                    html+="<tr>"
                                    if asi[9] == id:
                                        html+="<td>"+str(k)+"</td>"
                                        html+="<td>"+asi[1]+"</td>"
                                        html+="<td>"+asi[2]+"</td>"
                                        k = k + 1
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html += "</div>"
                        else:
                            html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
    if accion1 == "total_de_estudiantes_carrera":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))

        for anio in range(a1, a2 + (1)):
            vare[anio]=[0]*n_are
        for anio in range(a1, a2 + (1)):
            vcar[anio]=[0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                vare[anoBD][row[12]-1]+=1
                vcar[anoBD][row[13]-1]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            html += "<div class='row'>"
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcar[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vare[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>Se mostrara cuadros por areas y carreras con la cantidad de estudiantes</div>"
            areas = seleccionarAreas()#si hay doble veces repetido el id lo eliminamos a 1
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html+="<div align='center' class='alert alert-secondary'>Areas</div>"

                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vare[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos todo los id de carreras
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "Se tiene "+str(vcar[anio][index])+" Estudiantes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "porcentaje_de_avance_materias":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()
        for are in areas:
            vare[are[0]] = {}
            carreras = seleccionarcarrera_id(are[0])
            for car in carreras:
                vare[are[0]][car[0]] = {}
                asignatura = seleccionarAsignatura_por_id(car[0])
                for anio in range(a1, a2 + (1)):
                    vare[are[0]][car[0]][anio] = {}
                    for asig in asignatura:
                        vare[are[0]][car[0]][anio][asig[0]] = [0]*2
        carreras = seleccionarCarrerasTodo()#seleccionamos las carreras
        for car in carreras:
            vcar[car[0]]={}
            asignatura = seleccionarAsignatura_por_id(car[0])#seleccionamos asignatura de las carreras
            for anio in range(a1, a2 + (1)):
                vcar[car[0]][anio]={}#creamos un diccionario con el año y id carrera
                for asig in asignatura:#recorremos las asignaturas
                    vcar[car[0]][anio][asig[0]]=[0,0]#


        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[10], type(None)) and row[10]>=fecha1 and row[10] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[10].strftime("%Y-%m-%d")))
                vcar[row[6]][anoBD][row[4]][0] = row[1]#guardamos el porcentaje de avance
                vcar[row[6]][anoBD][row[4]][1] = row[7]#guardamos el cod de grado
                vare[row[8]][row[6]][anoBD][row[4]][0]=row[1]
                vare[row[8]][row[6]][anoBD][row[4]][1]=row[7]
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>El porcentaje de avance en materias de la siguiente carrera es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>El porcentaje de avance en materias de las siguientes carreras son</div>"

            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#impirmimos el nombre de la carrera
                asignaturas = seleccionarAsignatura_por_id(index1)
                if asignaturas != "no":
                    for anio in range(a1, a2 + (1)):
                        html+="<h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera
                        curso = seleccionarGrado()
                        html+="<div class='row'>"
                        for cur in curso:
                            k = 1
                            id=cur[0]
                            html += "<div class='col-lg-4'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            html += " Curso "+str(cur[1])
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html+= "<table class='table' style='font-size:12px'>"
                            html+= "<thead>"
                            html+="<tr>"
                            html+="<td>N°</td>"
                            html+="<td>Asignatura</td>"
                            html+="<td>Avance</td>"
                            html+="</tr>"
                            html+="</thead>"
                            html+="<tbody>"
                            for asig in asignaturas:
                                html+="<tr>"
                                if vcar[index1][anio][asig[0]][1] == id:
                                    html+="<td>"+str(k)+"</td>"
                                    html+="<td>"+asig[2]+"</td>"
                                    html+="<td>"+str(vcar[index1][anio][asig[0]][0])+"%</td>"
                                    k = k + 1
                                html+="</tr>"
                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                        html += "</div>"
                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"

        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>El porcentaje de avance en materias de la siguiente area es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>El porcentaje de avance en materias de las siguientes areas son</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                carreras = seleccionarcarrera_id(index1)
                for car in carreras:#recorremos todo los id de carreras
                    html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6><br>"#impirmimos el nombre de la carrera
                    asignaturas = seleccionarAsignatura_por_id(car[0])
                    if asignaturas != "no":
                        for anio in range(a1, a2 + (1)):
                            html+="<br><h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera
                            curso = seleccionarGrado()
                            html+="<div class='row'>"
                            for cur in curso:
                                k = 1
                                id=cur[0]
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(cur[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Asignatura</td>"
                                html+="<td>Avance</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asig in asignaturas:
                                    html+="<tr>"
                                    if vare[index1][car[0]][anio][asig[0]][1] == id:
                                        html+="<td>"+str(k)+"</td>"
                                        html+="<td>"+asig[2]+"</td>"
                                        html+="<td>"+str(vare[index1][car[0]][anio][asig[0]][0])+"%</td>"
                                        k = k + 1
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html += "</div>"
                    else:
                        html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>El porcentaje de avance en materias por areas y carreras se indicara en los siguientes cuadros</div>"
            html+="<div align='center' class='alert alert-secondary'>Areas y carreras</div>"
            areas = seleccionarAreas()#si hay doble veces repetido el id lo eliminamos a 1
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                carreras = seleccionarcarrera_id(index1)
                for car in carreras:#recorremos todo los id de carreras
                    html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6><br>"#impirmimos el nombre de la carrera
                    asignaturas = seleccionarAsignatura_por_id(car[0])
                    if asignaturas != "no":
                        for anio in range(a1, a2 + (1)):
                            html+="<br><h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera
                            curso = seleccionarGrado()
                            html+="<div class='row'>"
                            for cur in curso:
                                k = 1
                                id=cur[0]
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(cur[1])
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Asignatura</td>"
                                html+="<td>Avance</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asig in asignaturas:
                                    html+="<tr>"
                                    if vare[index1][car[0]][anio][asig[0]][1] == id:
                                        html+="<td>"+str(k)+"</td>"
                                        html+="<td>"+asig[2]+"</td>"
                                        html+="<td>"+str(vare[index1][car[0]][anio][asig[0]][0])+"%</td>"
                                        k = k + 1
                                    html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html += "</div>"
                    else:
                        html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
    if accion1 == "titulados":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()

        for anio in range(a1, a2 + (1)):
            vare[anio] = [0]*n_are
            vcar[anio] = [0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[9], type(None)) and row[9]>=fecha1 and row[9] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[9].strftime("%Y-%m-%d")))
              if row[1] == "aprobado":
                  vare[anoBD][row[8]-1]+=1
                  vcar[anoBD][row[7]-1]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Los titulados que se encontro de la siguiente carrera es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Los titulados que se encontro de las siguientes carreras son</div>"

            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vcar[anio][index])+" Titulados"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Los titulados que se encontro de la siguiente area es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Los titulados que se encontro de las siguientes areas son</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vare[anio][index])+" Titulados"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>Los titulados que se encontro por areas y carreras son </div>"
            html+="<div align='center' class='alert alert-secondary'>Areas</div>"

            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de carreras
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html+="<h6 align='center'>Area "+nombre_area_id(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vare[anio][index])+" Titulados"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos todo los id de areas
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h6 align='center'>Carrera " + str(nombre_carrera_retor(index1))+"</h6>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vcar[anio][index])+" Titulados"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "cantidad_docentes":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()

        for anio in range(a1, a2 + (1)):
            vare[anio] = [0]*n_are
            vcar[anio] = [0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[13], type(None)) and row[13]>=fecha1 and row[13] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[13].strftime("%Y-%m-%d")))
              vare[anoBD][row[11]-1]+=1
              vcar[anoBD][row[12]-1]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>La cantidad de docentes que tiene la siguiente carrera es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>La cantidad de docentes que tiene las siguientes carreras son</div>"

            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vcar[anio][index])+" docentes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>La cantidad de docentes que tiene la siguiente area es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>La cantidad de docentes que tiene las siguientes areas son</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vare[anio][index])+" docentes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>La cantidad de docentes por areas y carreras </div>"
            html+="<div align='center' class='alert alert-secondary'>Areas</div>"

            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de carreras
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html+="<h6 align='center'>Area "+nombre_area_id(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vare[anio][index])+" docentes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos todo los id de areas
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html += "<h6 align='center'>Carrera " + str(nombre_carrera_retor(index1))+"</h6>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += str(vcar[anio][index])+" docentes"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "docente_sexo":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()
        for are in areas:
            vare[are[0]] = {}
            for anio in range(a1, a2 + (1)):
                vare[are[0]][anio] = {
                    'masculino': 0,
                    'femenino': 0
                }
        carreras = seleccionarCarrerasTodo()
        for car in carreras:
            vcar[car[0]] = {}
            for anio in range(a1, a2 + (1)):
                vcar[car[0]][anio] = {
                    'masculino': 0,
                    'femenino': 0
                }
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[13], type(None)) and row[13]>=fecha1 and row[13] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[13].strftime("%Y-%m-%d")))
              vare[row[11]][anoBD][row[10]]+=1
              vcar[row[12]][anoBD][row[10]]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1

            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Se encontro un total de docentes clasificados por sexo de la siguiente carrera</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Se encontro un total de docentes clasificados por sexo de las siguientes carreras</div>"

            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Masculino</td>"
                    html+="<td>Femenino</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vcar[index1][anio]['masculino'])+"</td>"
                    html+="<td>"+str(vcar[index1][anio]['femenino'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Se encontro un total de docentes clasificados por sexo de la siguiente area</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Se encontro un total de docentes clasificados por sexo de las siguientes areas</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Masculino</td>"
                    html+="<td>Femenino</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vare[index1][anio]['masculino'])+"</td>"
                    html+="<td>"+str(vare[index1][anio]['femenino'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por sexo por areas y carreras</div>"
            html+="<div align='center' class='alert alert-secondary'>Areas</div>"
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Masculino</td>"
                    html+="<td>Femenino</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vare[index1][anio]['masculino'])+"</td>"
                    html+="<td>"+str(vare[index1][anio]['femenino'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carrera = seleccionarCarrerasTodo()
            for car in carrera:#recorremos todo los id de carreras
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Masculino</td>"
                    html+="<td>Femenino</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    html+="<tr>"
                    html+="<td>"+str(vcar[index1][anio]['masculino'])+"</td>"
                    html+="<td>"+str(vcar[index1][anio]['femenino'])+"</td>"
                    html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "departamento_docente":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_ar = ress[2]
        id_ar  = ress[3]
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        areas = seleccionarAreas()
        for are in areas:
            vare[are[0]] = {}
            for anio in range(a1, a2 + (1)):
                vare[are[0]][anio]={}
                for dep in departamento:
                    vare[are[0]][anio][dep] = 0

        carreras = seleccionarCarrerasTodo()
        for car in carreras:
            vcar[car[0]] = {}
            for anio in range(a1, a2 + (1)):
                vcar[car[0]][anio] = {}
                for dep in departamento:
                    vcar[car[0]][anio][dep] = 0
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[13], type(None)) and row[13]>=fecha1 and row[13] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[13].strftime("%Y-%m-%d")))
              vare[row[11]][anoBD][row[8]]+=1
              vcar[row[12]][anoBD][row[8]]+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1

            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por departamentos de la siguiente carrera es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por departamentos de las siguientes carreras son</div>"

            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Departamento</td>"
                    html+="<td>Docentes</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    for dep in departamento:
                        html+="<tr>"
                        html+="<td>"+str(dep)+"</td>"
                        html+="<td>"+str(vcar[index1][anio][dep])+"</td>"
                        html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        elif si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por departamentos de la siguiente area es</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por departamentos de las siguientes areas son</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Departamento</td>"
                    html+="<td>Docentes</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    for dep in departamento:
                        html+="<tr>"
                        html+="<td>"+str(dep)+"</td>"
                        html+="<td>"+str(vare[index1][anio][dep])+"</td>"
                        html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
        else:
            html+="<div align='center' class='alert alert-secondary'>Los docentes clasificados por departamentos son los siguientes por areas y carreras</div>"
            html+="<div align='center' class='alert alert-secondary'>Areas</div>"
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html += "<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Departamento</td>"
                    html+="<td>Docentes</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    for dep in departamento:
                        html+="<tr>"
                        html+="<td>"+str(dep)+"</td>"
                        html+="<td>"+str(vare[index1][anio][dep])+"</td>"
                        html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
            html+="<div align='center' class='alert alert-secondary'>Carreras</div>"
            carrera = seleccionarCarrerasTodo()
            for car in carrera:#recorremos todo los id de carreras
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6>"#im
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "Año "+str(anio)
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html+= "<table class='table' style='font-size:12px'>"
                    html+= "<thead>"
                    html+="<tr>"
                    html+="<td>Departamento</td>"
                    html+="<td>Docentes</td>"
                    html+="</tr>"
                    html+="</thead>"
                    html+="<tbody>"
                    for dep in departamento:
                        html+="<tr>"
                        html+="<td>"+str(dep)+"</td>"
                        html+="<td>"+str(vcar[index1][anio][dep])+"</td>"
                        html+="</tr>"
                    html+="</tbody>"
                    html+= "</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html += "</div>"
    if accion1 == "datos_carrera":
        si_car_n = ress[0]
        id_car   = ress[1]
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>La información de la carrera es la siguente</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>La información de las carreras es la siguiente</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<div class='row'>"
                html += "<div class='col-lg-12'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += "<h6 align='center'>Carrera "+ str(nombre_carrera_retor
                (index1))+"</h6>"
                html += "</div>"
                html += "<div class='panel-body'>"
                html+= "<table class='table' style='font-size:12px'>"
                html+= "<thead>"
                html+="<tr>"
                html+="<td>Dirección</td>"
                html+="<td>Area</td>"
                html+="</tr>"
                html+="</thead>"
                html+="<tbody>"
                for row in datos:
                    if row[0] == index1:
                        html+="<tr>"
                        html+="<td>"+str(row[2])+"</td>"
                        html+="<td>"+str(nombre_area_id(row[3]))+"</td>"
                        html+="</tr>"
                html+="</tbody>"
                html+= "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
    if accion1 == "areas":
        si_ar = ress[0]
        id_ar   = ress[1]
        if si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            if len(s_dupli)==1:
                html+="<div align='center' class='alert alert-secondary'>La información del área es la siguente</div>"
            else:
                html+="<div align='center' class='alert alert-secondary'>La información de las áreas es la siguiente</div>"

            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<div class='row'>"
                html += "<div class='col-lg-12'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += "<h6 align='center'>Área "+ str(nombre_area_id(index1))+"</h6>"
                html += "</div>"
                html += "<div class='panel-body'>"
                html+= "<table class='table' style='font-size:12px'>"
                html+= "<thead>"
                html+="<tr>"
                html+="<td>Área</td>"
                html+="<td>Dirección</td>"
                html+="<td>Telefono área</td>"
                html+="</tr>"
                html+="</thead>"
                html+="<tbody>"
                for row in datos:
                    if row[0] == index1:
                        html+="<tr>"
                        html+="<td>"+str(row[1])+"</td>"
                        html+="<td>"+str(row[2])+"</td>"
                        html+="<td>"+str((row[3]))+"</td>"
                        html+="</tr>"
                html+="</tbody>"
                html+= "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
    if accion1 == 'areas_unsxx':
        html+="<div align='center' class='alert alert-secondary'>La Universidad tiene las siguientes Áreas</div>"
        html += "<div class='row'>"
        html += "<div class='col-lg-12'>"
        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
        html += "<div class='panel-heading'>"
        html += "<h6 align='center'>Áreas</h6>"
        html += "</div>"
        html += "<div class='panel-body'>"
        html+= "<table class='table' style='font-size:12px'>"
        html+= "<thead>"
        html+="<tr>"
        html+="<td>Dirección</td>"
        html+="<td>Área</td>"
        html+="<td>Telefono área</td>"
        html+="</tr>"
        html+="</thead>"
        html+="<tbody>"
        for row in datos:#recorremos todo los id de areas
            html+="<tr>"
            html+="<td>"+str(row[2])+"</td>"
            html+="<td>"+str(row[1])+"</td>"
            html+="<td>"+str((row[3]))+"</td>"
            html+="</tr>"
        html+="</tbody>"
        html+= "</table>"
        html += "</div>"
        html += "</div>"
        html += "</div>"
        html += "</div>"
    if accion1 == "materias_aprobados":
        si_mat = ress[0]
        id_mat = ress[1]
        si_car_n = ress[2]
        id_car   = ress[3]
        si_ar = ress[4]
        id_ar  = ress[5]
        si_total = ress[6]
        fecha1 = ress[7]
        fecha2 = ress[8]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        id_materias = eliminar_dobles(id_mat)
        for mat in id_materias:
            index = int(mat)
            vcar[index] = {}
            dat = seleccionar_asignatura_porID(index)
            for anio in range(a1, a2 + 1):
                vcar[index][anio] = {
                    'aprobado': 0,
                    'reprobado': 0,
                    'tipo_asignatura': dat[11],
                    'area':dat[10],
                    'carrera':dat[8]
                }

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
              if row[2]>50:
                  vcar[row[8]][anoBD]['aprobado']+=1
              else:
                  vcar[row[8]][anoBD]['reprobado']+=1
        html+="<div class='alert alert-secondary'>Los estudiantes aprobados y reprobados son lo siguiente</div>"
        for mat in id_materias:
            index = int(mat)
            for anio in range(a1, a2 + 1):
                if si_car_n == "si_car_n":
                    carreras = eliminar_dobles(id_car)
                    for car in carreras:
                        ind = int(car)
                        if ind == vcar[index][anio]['carrera']:
                            html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" aprobados y "+str(vcar[index][anio]['reprobado'])+" reprobados del año "+str(anio)+"</div>"
                elif si_ar == "si_ar":
                    areas = eliminar_dobles(id_ar)
                    if vcar[index][anio]['tipo_asignatura'] == 2:#estamos en lo correcto es asignatura de todo el area
                        for are in areas:
                            ind = int(are)
                            if ind == vcar[index][anio]['area']:
                                html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" aprobados y "+str(vcar[index][anio]['reprobado'])+" reprobados del año "+str(anio)+"</div>"
                    else:
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" aprobados y "+str(vcar[index][anio]['reprobado'])+" reprobados del año "+str(anio)+"</div>"

                else:
                    if vcar[index][anio]['tipo_asignatura'] == 1:#normal
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" aprobados y "+str(vcar[index][anio]['reprobado'])+" reprobados del año "+str(anio)+"</div>"
                    else:#materia de un area completo
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(vcar[index][anio]['area'])+" tiene "+str(vcar[index][anio]['aprobado'])+" aprobados y "+str(vcar[index][anio]['reprobado'])+" reprobados del año "+str(anio)+"</div>"
    if accion1 == "datos_asignaturas":
        si_car_n = ress[0]
        id_car   = ress[1]
        si_grado = ress[2]
        id_grado = ress[3]
        si_ar = ress[4]
        id_ar  = ress[5]
        si_total = ress[6]
        fecha1 = ress[7]
        fecha2 = ress[8]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        varea = {}
        vcar={}
        areas = seleccionarAreas()
        for are in areas:
            varea[are[0]]={}
            carreras = seleccionarcarrera_id(are[0])#seleccionamos las carreras
            for car in carreras:
                asignaturas = seleccionarAsignatura_por_id(car[0])#seleccionamos las asignaturas de la carreras
                if asignaturas != "no":
                    varea[are[0]][car[0]] = {}
                    for anio in range(a1, a2 + (1)):#recorremos los años
                        varea[are[0]][car[0]][anio]={}
                        cursos = seleccionarGrado()#selccionamos los cursos
                        for cur in cursos:#recorremos los cursos
                            varea[are[0]][car[0]][anio][cur[0]]={}
                            for asig in asignaturas:
                                if cur[0] == asig[9]:
                                    varea[are[0]][car[0]][anio][cur[0]][asig[0]] = {'aprobado':0,'reprobado':0,'id_asignatura':asig[0]}
        carreras = seleccionarCarrerasTodo()
        for car in carreras:
            asignatura = seleccionarAsignatura_por_id(car[0])
            if asignatura != "no":
                vcar[car[0]] = {}
                for anio in range(a1, a2 + (1)):
                    vcar[car[0]][anio]={}
                    cursos = seleccionarGrado()
                    for cur in cursos:
                        vcar[car[0]][anio][cur[0]]={}
                        for asig in asignatura:
                            if cur[0] == asig[9]:
                                vcar[car[0]][anio][cur[0]][asig[0]] = {'aprobado':0,'reprobado':0,'id_asignatura':asig[0]}


        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
                if row[2]>50:
                    varea[row[12]][row[10]][anoBD][row[11]][row[8]]['aprobado']+=1
                    vcar[row[10]][anoBD][row[11]][row[8]]['aprobado']+=1
                else:
                    varea[row[12]][row[10]][anoBD][row[11]][row[8]]['reprobado']+=1
                    vcar[row[10]][anoBD][row[11]][row[8]]['reprobado']+=1
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            existe = "no"
            if si_grado == "si_grado":
                existe = "si"
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                materias=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera

                if materias != "no":
                    if existe == "si":
                        curso = eliminar_dobles(id_grado)
                    else:
                        curso = seleccionarGrado()
                    for anio in range(a1, a2 + (1)):
                        html+="<h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera

                        html+="<div class='row'>"
                        for cur in curso:
                            if existe == "si":
                                id = int(cur)
                            else:
                                id = cur[0]
                            k = 1
                            print(id," es el curso")
                            html += "<div class='col-lg-4'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            html += " Curso "+str(NOmbredeGrado_por_id(id))
                            html += "</div>"
                            html += "<div class='panel-body'>"
                            html+= "<table class='table' style='font-size:12px'>"
                            html+= "<thead>"
                            html+="<tr>"
                            html+="<td>N°</td>"
                            html+="<td>Asignatura</td>"
                            html+="<td>Apro.</td>"
                            html+="<td>Repro.</td>"
                            html+="</tr>"
                            html+="</thead>"
                            html+="<tbody>"
                            for asi in materias:
                                if id == asi[9]:
                                    html+="<tr>"
                                    html+="<td>"+str(k)+"</td>"
                                    html+="<td>"+str(nombre_asignatura(vcar[index1][anio][id][asi[0]]['id_asignatura']))+"</td>"
                                    html+="<td>"+str(vcar[index1][anio][id][asi[0]]['aprobado'])+"</td>"
                                    html+="<td>"+str(vcar[index1][anio][id][asi[0]]['reprobado'])+"</td>"
                                    k = k + 1
                                    html+="</tr>"
                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                        html+="<div>"
                else:
                    html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"

        elif si_ar == "si_ar":#si es diferente de no existe una area o areas
            #obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area

                for car in carreras:#recorremos todas las carreras encontradas
                    html+="<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6><br>"#impirmimos el nombre de la carrera
                    materias=seleccionarAsignatura_por_id(car[0])
                    if materias != "no":
                        for anio in range(a1, a2 + (1)):
                            html+="<h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera

                            html+="<div class='row'>"
                            curso = seleccionarGrado()
                            for cur in cursos:
                                id = cur[0]
                                k = 1
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(NOmbredeGrado_por_id(id))
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Asignatura</td>"
                                html+="<td>Apro.</td>"
                                html+="<td>Repro.</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asi in materias:
                                    if id == asi[9]:
                                        html+="<tr>"
                                        html+="<td>"+str(k)+"</td>"

                                        html+="<td>"+str(nombre_asignatura(varea[index1][car[0]][anio][id][asi[0]]['id_asignatura']))+"</td>"
                                        html+="<td>"+str(varea[index1][car[0]][anio][id][asi[0]]['aprobado'])+"</td>"
                                        html+="<td>"+str(varea[index1][car[0]][anio][id][asi[0]]['reprobado'])+"</td>"
                                        k = k + 1
                                        html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html+="<div>"
                    else:
                        html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"

        else:
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                index = are[0] - 1#obtenemos el id
                index1 = are[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area

                for car in carreras:#recorremos todas las carreras encontradas
                    html+="<h6 align='center'>Carrera "+nombre_carrera_retor(car[0])+"</h6><br>"#impirmimos el nombre de la carrera
                    materias=seleccionarAsignatura_por_id(car[0])
                    if materias != "no":
                        for anio in range(a1, a2 + (1)):
                            html+="<h6 align='center'>Año "+str(anio)+"</h6><br>"#impirmimos el nombre de la carrera

                            html+="<div class='row'>"
                            curso = seleccionarGrado()
                            for cur in cursos:
                                id = cur[0]
                                k = 1
                                html += "<div class='col-lg-4'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += " Curso "+str(NOmbredeGrado_por_id(id))
                                html += "</div>"
                                html += "<div class='panel-body'>"
                                html+= "<table class='table' style='font-size:12px'>"
                                html+= "<thead>"
                                html+="<tr>"
                                html+="<td>N°</td>"
                                html+="<td>Asignatura</td>"
                                html+="<td>Apro.</td>"
                                html+="<td>Repro.</td>"
                                html+="</tr>"
                                html+="</thead>"
                                html+="<tbody>"
                                for asi in materias:
                                    if id == asi[9]:
                                        html+="<tr>"
                                        html+="<td>"+str(k)+"</td>"

                                        html+="<td>"+str(nombre_asignatura(varea[index1][car[0]][anio][id][asi[0]]['id_asignatura']))+"</td>"
                                        html+="<td>"+str(varea[index1][car[0]][anio][id][asi[0]]['aprobado'])+"</td>"
                                        html+="<td>"+str(varea[index1][car[0]][anio][id][asi[0]]['reprobado'])+"</td>"
                                        k = k + 1
                                        html+="</tr>"
                                html+="</tbody>"
                                html+= "</table>"
                                html += "</div>"
                                html += "</div>"
                                html += "</div>"
                            html+="<div>"
                    else:
                        html+="<div align='center' class='alert alert-secondary'>No se encontro información</div>"
    if accion1 == "carrera_area_mas_inscritos":
        si_hay_area_carr = ress[0]
        si_car_n = ress[1]
        id_car   = ress[2]
        si_ar = ress[3]
        id_ar  = ress[4]
        fecha1 = ress[6]
        fecha2 = ress[7]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        area = {}
        carre = {}
        for anio in range(a1, a2 + (1)):
            area[anio]=[0]*n_are
            carre[anio]=[0]*n_car
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                if row[14]==1:#si es 1 es le curso primero o los recien matriculados
                    area[anoBD][row[12]-1]+=1
                    carre[anoBD][row[13]-1]+=1


        for anio in range(a1, a2 + 1):  # Asumiendo que a1 y a2 son años inicial y final, +1 para incluir a2
            areas = seleccionarAreas()  # Esto debe devolver una lista de áreas
            n = len(areas)  # n es el número de áreas
            for arr in range(n):
                for ar1 in range(arr + 1, n):  # Recorrer de izquierda a derecha
                    if area[anio][arr] < area[anio][ar1]:  # Comparación de elementos
                        aux = area[anio][arr]
                        area[anio][arr] = area[anio][ar1]
                        area[anio][ar1] = aux
            carrera = seleccionarCarrerasTodo()
            n = len(carrera)
            for car in range(n):
                for car1 in range(car + 1, n):  # Recorrer de izquierda a derecha
                    if carre[anio][car] < carre[anio][car1]:  # Comparación de elementos
                        aux = carre[anio][car]
                        carre[anio][car] = carre[anio][car1]
                        carre[anio][car1] = aux
        ar = list(set(si_hay_area_carr))
        siarea = 0
        sicarrera = 0
        for doble in ar:
            if doble == 1:
                siarea = 1
            elif doble == 2:
                sicarrera=1
        if siarea == 1 and sicarrera == 1:
            html+="<div class='alert alert-secondary'>La carrera y área que tienen mas matriculados son los siguientes</div>"
            areas = seleccionarAreas()
            html+="<div class='alert alert-warning'>Áreas</div>"

            for anio in range(a1, a2 + (1)):
                k = 0
                html+="<div align='center' class='alert alert-secondary'>El área de "
                for are in areas:
                    if k < 2:
                        if k == 0:
                            html+=str(are[1])+" tiene "+str(area[anio][are[0]-1])+" nuevos matriculados y como tambien el área de "
                        else:
                            html+=str(are[1])+" tiene "+str(area[anio][are[0]-1])+" nuevos matriculados"
                    k = k + 1
                html+=" en el Año "+str(anio)+"</div>"

            carrera = seleccionarCarrerasTodo()
            html+="<div class='alert alert-success'>Carreras</div>"
            for anio in range(a1, a2 + (1)):
                k = 0
                html+="<div align='center' class='alert alert-secondary'>La carrera de "
                for car in carrera:
                    if k < 2:
                        if k == 0:
                            html+=str(car[1])+" tiene "+str(carre[anio][car[0]-1])+" nuevos matriculados y como tambien la carrera de"
                        else:
                            html+=str(car[1])+" tiene "+str(carre[anio][car[0]-1])+" nuevos matriculados"
                    k = k + 1
                html+=" en el Año "+str(anio)+"</div>"
        if siarea == 1 and sicarrera == 0:
            html+="<div class='alert alert-warning'>La área que tienen mas matriculados son los siguientes</div>"
            areas = seleccionarAreas()
            for anio in range(a1, a2 + (1)):
                k = 0
                html+="<div align='center' class='alert alert-secondary'>El área de "
                for are in areas:
                    if k < 2:
                        if k == 0:
                            html+=str(are[1])+" tiene "+str(area[anio][are[0]-1])+" nuevos matriculados y como tambien el área de "
                        else:
                            html+=str(are[1])+" tiene "+str(area[anio][are[0]-1])+" nuevos matriculados"
                    k = k + 1
                html+=" en el Año "+str(anio)+"</div>"
        if siarea == 0 and sicarrera == 1:
            carrera = seleccionarCarrerasTodo()
            html+="<div class='alert alert-success'>Las carreras que tienen mas inscritos son</div> "

            for anio in range(a1, a2 + (1)):
                k = 0
                html+="<div align='center' class='alert alert-secondary'>La carrera de "
                for car in carrera:
                    if k < 2:
                        if k == 0:
                            html+=str(car[1])+" tiene "+str(carre[anio][car[0]-1])+" nuevos matriculados y como tambien la carrera de"
                        else:
                            html+=str(car[1])+" tiene "+str(carre[anio][car[0]-1])+" nuevos matriculados"
                    k = k + 1
                html+=" en el Año "+str(anio)+"</div>"
    if accion1 == "total_estudiantes_area":
        si_total = ress[4]
        fecha1 = ress[5]
        fecha2 = ress[6]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        area = {}
        for anio in range(a1, a2 + (1)):
            area[anio]=[0]*n_are
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                area[anoBD][row[12]-1]+=1
        if si_total == "si_total":
            html += "<div align='center' class='alert alert-secondary'>La cantidad de estudiantes que tienen las áreas son lo siguiente</div>"
            areas = seleccionarAreas()
            for are in areas:#recorremos todo los id de areas
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):

                    html += "<div class='col-lg-4'>"
                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                    html += "<div class='panel-heading'>"
                    html += "<b>Area "+str(nombre_area_id(are[0]))+"</b>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "El total de estudiantes que tiene el área es de "+str(area[anio][are[0]-1])+" Estudiantes en el año "+str(anio)
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                html+="<div><br>"
        else:
            html+="<div class = 'alert alert-secondary'>Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas</div>"
    if accion1 == "pasaron_de_curso":
        id_grados = ress[0]
        si_car_n = ress[1]
        id_car   = ress[2]
        si_ar = ress[3]
        id_ar  = ress[4]
        si_total = ress[5]
        fecha1 = ress[6]
        fecha2 = ress[7]
        dat = []
        dat = [int(d) for d in id_grados.split(',') if d.strip()]
        pares = []
        parMin = []
        # Verificar si la cantidad de datos es par
        if len(dat) % 2 == 0:
            # Iterar sobre los pares consecutivos y obtener el mayor de cada par
            for i in range(0, len(dat), 2):
                if dat[i] > dat[i + 1]:
                    pares.append(dat[i])
                else:
                    pares.append(dat[i + 1])
        else:
            max = 0
            for i in range(len(dat)):
                if dat[i] > max:
                    max = dat[i]
            pares.append(max)
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        area = {}
        carre = {}

        for anio in range(a1, a2 + (1)):
            areas = seleccionarAreas()
            area[anio] = {}
            carre[anio] = {}
            for are in areas:
                area[anio][are[0]]=[0]*n_grado
            carreras = seleccionarCarrerasTodo()
            for car in carreras:
                carre[anio][car[0]]=[0]*n_grado
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if not isinstance(row[16], type(None)) and row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                area[anoBD][row[12]][row[14]-1]+=1
                carre[anoBD][row[13]][row[14]-1]+=1
        if si_car_n == "si_car_n":
            html += "<div align='center' class='alert alert-secondary'>Los estudiantes que pasaron de curso son </div>"

            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    for cur in pares:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "Estudiantes que pasaron a "+str(NOmbredeGrado_por_id(cur))+" son "+str(carre[anio][index1][cur-1])+" en el año "+str(anio)
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                html+="<div><br>"
        elif si_ar == "si_ar":
            html += "<div align='center' class='alert alert-secondary'>Los estudiantes que pasaron de curso son </div>"
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    for cur in pares:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "Estudiantes que pasaron a "+str(NOmbredeGrado_por_id(cur))+" son "+str(carre[anio][index1][cur-1])+" en el año "+str(anio)
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                html+="<div><br>"
        else:
            html += "<div align='center' class='alert alert-secondary'>Los estudiantes que pasaron de curso son </div>"
            html += "<div align='center' class='alert alert-secondary'>Áreas </div>"
            areas = seleccionarAreas()
            for ar in areas:#recorremos todo los id de areas
                index = ar[0] - 1#obtenemos el id
                index1 = ar[0]
                html += "<h5 align='center'>Area " + str(nombre_area_id(index1))+"</h5>"
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    for cur in pares:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "Estudiantes que pasaron a "+str(NOmbredeGrado_por_id(cur))+" son "+str(carre[anio][index1][cur-1])+" en el año "+str(anio)
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                html+="<div><br>"
            html += "<div align='center' class='alert alert-secondary'>Carreras </div>"

            carreras = seleccionarCarrerasTodo()
            for car in carreras:#recorremos todo los id de carreras
                index = car[0] - 1#obtenemos el id
                index1 = car[0]
                html+="<h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                html+="<div class='row'>"
                for anio in range(a1, a2 + (1)):
                    for cur in pares:
                        html += "<div class='col-lg-4'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += "</div>"
                        html += "<div class='panel-body'>"
                        html += "Estudiantes que pasaron a "+str(NOmbredeGrado_por_id(cur))+" son "+str(carre[anio][index1][cur-1])+" en el año "+str(anio)
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"
                html+="<div><br>"
    if accion1 == "estudiantes_regulares_en_materia":
        si_mat = ress[0]
        id_mat = ress[1]
        si_car_n = ress[2]
        id_car   = ress[3]
        si_ar = ress[4]
        id_ar  = ress[5]
        si_total = ress[6]
        fecha1 = ress[7]
        fecha2 = ress[8]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        id_materias = eliminar_dobles(id_mat)
        for mat in id_materias:
            index = int(mat)
            vcar[index] = {}
            dat = seleccionar_asignatura_porID(index)
            for anio in range(a1, a2 + 1):
                vcar[index][anio] = {
                    'aprobado': 0,
                    'reprobado': 0,
                    'tipo_asignatura': dat[11],
                    'area':dat[10],
                    'carrera':dat[8]
                }

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
              if row[3]=='activo':
                  vcar[row[8]][anoBD]['aprobado']+=1
              else:
                  vcar[row[8]][anoBD]['reprobado']+=1
        html+="<div class='alert alert-secondary'>Los estudiantes regulares e irregulares son lo siguiente</div>"
        for mat in id_materias:
            index = int(mat)
            for anio in range(a1, a2 + 1):
                if si_car_n == "si_car_n":
                    carreras = eliminar_dobles(id_car)
                    for car in carreras:
                        ind = int(car)
                        if ind == vcar[index][anio]['carrera']:
                            html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" estudiantes regulares y "+str(vcar[index][anio]['reprobado'])+" estudiantes irregulares del año "+str(anio)+"</div>"
                elif si_ar == "si_ar":
                    areas = eliminar_dobles(id_ar)
                    if vcar[index][anio]['tipo_asignatura'] == 2:#estamos en lo correcto es asignatura de todo el area
                        for are in areas:
                            ind = int(are)
                            if ind == vcar[index][anio]['area']:
                                html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" estudiantes regulares y "+str(vcar[index][anio]['reprobado'])+" estudiantes irregulares del año "+str(anio)+"</div>"
                    else:
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" estudiantes regulares y "+str(vcar[index][anio]['reprobado'])+" estudiantes irregulares del año "+str(anio)+"</div>"

                else:
                    if vcar[index][anio]['tipo_asignatura'] == 1:#normal
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" estudiantes regulares y "+str(vcar[index][anio]['reprobado'])+" estudiantes irregulares del año "+str(anio)+"</div>"
                    else:#materia de un area completo
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(vcar[index][anio]['area'])+" tiene "+str(vcar[index][anio]['aprobado'])+" estudiantes regulares y "+str(vcar[index][anio]['reprobado'])+" estudiantes irregulares del año "+str(anio)+"</div>"
    if accion1 == "estudiantes_desercion_en_materia":
        si_mat = ress[0]
        id_mat = ress[1]
        si_car_n = ress[2]
        id_car   = ress[3]
        si_ar = ress[4]
        id_ar  = ress[5]
        si_total = ress[6]
        fecha1 = ress[7]
        fecha2 = ress[8]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        vcar = {}
        vare = {}
        a11 = int(obtener_ano_de_fecha(fecha1))
        a22 = int(obtener_ano_de_fecha(fecha2))
        a1 = int(obtener_ano_de_fecha(fecha1))
        a2 = int(obtener_ano_de_fecha(fecha2))
        id_materias = eliminar_dobles(id_mat)
        for mat in id_materias:
            index = int(mat)
            vcar[index] = {}
            dat = seleccionar_asignatura_porID(index)
            for anio in range(a1, a2 + 1):
                vcar[index][anio] = {
                    'aprobado': 0,
                    'reprobado': 0,
                    'tipo_asignatura': dat[11],
                    'area':dat[10],
                    'carrera':dat[8]
                }

        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
          if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
              anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))
              if row[4]=='si':
                  vcar[row[8]][anoBD]['aprobado']+=1
              else:
                  vcar[row[8]][anoBD]['reprobado']+=1
        html+="<div class='alert alert-secondary'>Los estudiantes que desertaron son lo siguiente</div>"
        for mat in id_materias:
            index = int(mat)
            for anio in range(a1, a2 + 1):
                if si_car_n == "si_car_n":
                    carreras = eliminar_dobles(id_car)
                    for car in carreras:
                        ind = int(car)
                        if ind == vcar[index][anio]['carrera']:
                            html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" desertores y "+str(vcar[index][anio]['reprobado'])+" que siguen del año "+str(anio)+"</div>"
                elif si_ar == "si_ar":
                    areas = eliminar_dobles(id_ar)
                    if vcar[index][anio]['tipo_asignatura'] == 2:#estamos en lo correcto es asignatura de todo el area
                        for are in areas:
                            ind = int(are)
                            if ind == vcar[index][anio]['area']:
                                html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(ind)+" tiene "+str(vcar[index][anio]['aprobado'])+" desertores y "+str(vcar[index][anio]['reprobado'])+" que siguen del año "+str(anio)+"</div>"
                    else:
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" desertores y "+str(vcar[index][anio]['reprobado'])+" que siguen del año "+str(anio)+"</div>"

                else:
                    if vcar[index][anio]['tipo_asignatura'] == 1:#normal
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" de la carrera de "+nombre_carrera_retor(vcar[index][anio]['carrera'])+" tiene "+str(vcar[index][anio]['aprobado'])+" desertores y "+str(vcar[index][anio]['reprobado'])+" que siguen del año "+str(anio)+"</div>"
                    else:#materia de un area completo
                        html+="<div class='alert alert-secondary'>La asignatura de "+nombre_asignatura(index)+" del area de "+nombre_area_id(vcar[index][anio]['area'])+" tiene "+str(vcar[index][anio]['aprobado'])+" desertores y "+str(vcar[index][anio]['reprobado'])+" que siguen del año "+str(anio)+"</div>"

    html += "</container>"

    return html

def eliminar_dobles(cadena):
    lista = cadena.split(",")
    # Convertir la lista en un conjunto para eliminar duplicados
    conjunto = set(lista)
    # Convertir el conjunto de nuevo en una lista
    lista_sin_duplicados = list(conjunto)
    lista_sin_vacios = [elemento for elemento in lista_sin_duplicados if elemento != '']
    return lista_sin_vacios

def separar_guiones(cadena):
    segmentos = [segmento for segmento in cadena.split('|') if segmento != '']
    return segmentos

def menCOncluyeron(a,b):
    if a == b:
        return "<h6>la relación es pareja</h6>"
    elif a > b:
        return "<h6>hay menos estudiantes que concluyen sus estudios con relación a 1er año</h6>"
    elif a < b:
        return "<h6>existe mas estudiantes que concluyen sus estudios con relación a 1er año</h6>"

def generar_reporte():
    # Llamar al script de reporte.py
    subprocess.call(["python", "reporte.py"])

    # Abrir el archivo PDF resultante en el navegador
    webbrowser.open("reporte.pdf")



def verificar_grado(si_car, si_curso, carrera, grado, si):
    men = ""
    if si_car != "no" and si == "no":
        men += " de la carrera " + carrera
        si = "si"
    else:
        men += " de la carrera " + carrera
        si = "si"

    if si_curso != "no" and si == "no":
        men += " del curso " + grado
        si = "si"
    elif si_curso != "no" and si == "si":
        men += ", del curso " + grado
        si = "si"

    return men
ab = ["Tecnologia", "Salud", "Social"]

def verificar_area(si, area, direccion_area, telefono_area, nombre_carrera, direccion_carrera, si_ar, c_area):
    par = c_area.split("|")
    me = ""
    for i in range(len(par)-1):
        if si == "no":
            me += ab[int(par[i])-1]
            si = "si"
        elif si == "si":
            me += ", " + ab[int(par[i])-1]
    return me

def verificar2(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, dep, provi, si_des, si_apla, si_ar, si_apro, c_area, si):
    men = ""

    if si_activo != "no" and si == "no":
        men += " activos "
        si = "si"

    if si_desactivo != "no" and si == "no":
        men += " desactivos "
        si = "si"
    elif si_desactivo != "no" and si == "si":
        men += ", desactivos"

    if si_m != "no" and si == "no":
        men += " varones "
        si = "si"
    elif si_m != "no" and si == "si":
        men += ", varones"

    if si_f != "no" and si == "no":
        men += " mujeres "
        si = "si"
    elif si_f != "no" and si == "no":
        men += " , mujeres"

    if si_dep != "no" and si == "no":
        men += " del departamento " + dep + " "
        si = "si"
    elif si_dep != "no" and si == "si":
        men += " , departamento de " + dep

    if si_prov != "no" and si == "no":
        men += " de la provincia de " + provi + " "
        si = "si"
    elif si_prov != "no" and si == "si":
        men += " , provincia de " + provi

    if si_des != "no" and si == "no":
        men += " desertores "
        si = "si"
    elif si_des != "no" and si == "si":
        men += ", desertores"
        si = "si"

    if si_apla != "no" and si == "no":
        men += " reprobados "
        si = "si"
    elif si_apla != "no" and si == "si":
        men += ", reprobados"
        si = "si"

    if si_apro != "no" and si == "no":
        men += " aprobados "
        si = "si"
    elif si_apro != "no" and si == "si":
        men += ", aprobados"
        si = "si"

    si1 = "no"
    if si_ar != "no" and si == "si":
        par = c_area.split("|")
        for i in range(len(par)-1):
            if si1 == "no" and si == "si":
                men += " del area " + ab[int(par[i])-1]
                si1 = "si"
            elif si1 == "si":
                men += ", del area " + ab[int(par[i])-1]
        si = "si"

    return men

def verificarUNSXX(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, si_nom, si_apell, dep, provi, nom, ap, am, si):
    men = ""

    if si_activo != "no" and si == "no":
        men += " activos "
        si = "si"

    if si_desactivo != "no" and si == "no":
        men += " desactivos "
        si = "si"
    elif si_desactivo != "no" and si == "si":
        men += ", desactivos"

    if si_m != "no" and si == "no":
        men += " varones "
        si = "si"
    elif si_m != "no" and si == "si":
        men += ", varones"

    if si_f != "no" and si == "no":
        men += " mujeres "
        si = "si"
    elif si_f != "no" and si == "no":
        men += " , mujeres"

    if si_dep != "no" and si == "no":
        men += " del departamento " + dep + " "
        si = "si"
    elif si_dep != "no" and si == "si":
        men += " , departamento de " + dep

    if si_prov != "no" and si == "no":
        men += " de la provincia de " + provi + " "
        si = "si"
    elif si_prov != "no" and si == "si":
        men += " , provincia de " + provi

    hay = "no"
    if si_nom != "no" and si == "no":
        men += " con el nombre de " + nom
        si = "si"
        hay = "si"
    elif si_nom != "no" and si == "si":
        men += " , con el nombre de " + nom
        hay = "si"

    if si_apell != "no" and si == "no" and hay == "si":
        if ap != "":
            men += " " + ap
        if am != "":
            men += " " + am
        si = "si"
    elif si_apell != "no" and si == "si" and hay == "si":
        if ap != "":
            men += " " + ap
        if am != "":
            men += " " + am

    men += " en la Universidad"
    return men

def verificar(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, si_nom, si_apell, carrera, dep, provi, nom, ap, am, si, si_apla, si_apro, si_des, si_curso, grado):
    men = ""

    if si_activo != "no" and si == "no":
        men += " activos "
        si = "si"
    if si_desactivo != "no" and si == "no":
        men += " desactivos "
        si = "si"
    elif si_desactivo != "no" and si == "si":
        men += ", desactivos"
    if si_m != "no" and si == "no":
        men += " varones "
        si = "si"
    elif si_m != "no" and si == "si":
        men += ", varones"
    if si_f != "no" and si == "no":
        men += " mujeres "
        si = "si"
    elif si_f != "no" and si == "si":
        men += " , mujeres"
    if si_dep != "no" and si == "no":
        men += " del departamento " + dep + " "
        si = "si"
    elif si_dep != "no" and si == "si":
        men += " , departamento de " + dep
    if si_prov != "no" and si == "no":
        men += " de la provincia de " + provi + " "
        si = "si"
    elif si_prov != "no" and si == "si":
        men += " , provincia de " + provi
    hay = "no"
    if si_nom != "no" and si == "no":
        men += " con el nombre de " + nom + ""
        si = "si"
        hay = "si"
    elif si_nom != "no" and si == "si":
        men += " , con el nombre de " + nom + ""
        hay = "si"
    if si_apell != "no" and si == "no" and hay == "si":
        if ap != "":
            men += " " + ap
        if am != "":
            men += " " + am
        si = "si"
    elif si_apell != "no" and si == "si" and hay == "si":
        if ap != "":
            men += " " + ap
        if am != "":
            men += " " + am
    if si_des != "no" and si == "no":
        men += " desertores "
        si = "si"
    elif si_des != "no" and si == "si":
        men += ", desertores"
        si = "si"
    if si_apla != "no" and si == "no":
        men += " reprobados "
        si = "si"
    elif si_apla != "no" and si == "si":
        men += ", reprobados"
        si = "si"
    if si_apro != "no" and si == "no":
        men += " aprobados "
        si = "si"
    elif si_apro != "no" and si == "si":
        men += ", aprobados"
        si = "si"
    if si_curso != "no" and si == "no":
        men += " del curso " + grado
        si = "si"
    elif si_curso != "no" and si == "si":
        men += ", del curso " + grado
        si = "si"
    men += " de la carrera de " + carrera
    return men
