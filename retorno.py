from flask import jsonify
from sql import nombre_carrera_retor,grado_Estudiante,obtener_nombre,nombre_materia,obtener_datos_de_curso
from sql import seleccionarAreas,seleccionar_carrera,seleccionarAsignaturaAreas,seleccionarAsignatura
from sql import nombre_asignatura,nombre_carrera,consulta_Titulado,seleccionarcarrera_id,nombre_area_id
from sql import modalidad_titulacion_id,seleccionarAsignatura_por_id,contar_total_estudiante_curso
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
        id_car = ress[1]#id de carreras
        si_ar = ress[2]
        id_ar = ress[3]
        si_total = ress[4]
        if si_car_n == "si_car_n":
            s_dupli = eliminar_dobles(id_car)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Carrera de "+str(nombre_carrera_retor(index1))+"<h5>"
                contar = 0
                for row in datos:
                    if row[13] == index1:
                        contar+=1
                html += "Se encontro un total de " + str(contar) + " Estudiantes"
        if si_ar == "si_ar":
            s_dupli = eliminar_dobles(id_ar)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area "+str(nombre_area_id(index1))+"<h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    contar = 0
                    for car in carreras:
                        for row in datos:
                            if row[13] == car[0]:
                                contar+=1
                    html += "Se encontro un total de " + str(contar) + " Estudiantes"
                else:
                    html+="<h6>No se encontro información</h6>"
        if si_total == "si_total":
            contar = 0
            for row in datos:
                contar+=1
            html += "La universidad tiene un total de " + str(contar) + " Estudiantes"


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
        fecha1 = ress[0]
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareasApro = [0] * 3
        vareasApla = [0] * 3
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
        print(a1,a2,"  sirbe para ")
        for anio in range(a1, a2 + (1)):
            print(anio, "  el ano es " )
            c_infor[anio] = [0,0,0,0,0]
            c_inforr[anio] = [0,0,0,0,0]
            c_civil[anio] = [0,0,0,0,0]
            c_civilr[anio] = [0,0,0,0,0]
            c_minas[anio] = [0,0,0,0,0]
            c_minasr[anio] = [0,0,0,0,0]
            c_elec[anio] = [0,0,0,0,0]
            c_elecr[anio] = [0,0,0,0,0]
            c_mec[anio] = [0,0,0,0,0]
            c_mecr[anio] = [0,0,0,0,0]
            c_agro[anio] = [0,0,0,0,0]
            c_agror[anio] = [0,0,0,0,0]
            c_lit[anio] = [0,0,0,0,0]
            c_litr[anio] = [0,0,0,0,0]
            c_der[anio] = [0,0,0,0,0]
            c_derr[anio] = [0,0,0,0,0]
            c_cie[anio] = [0,0,0,0,0]
            c_cier[anio] = [0,0,0,0,0]
            c_cont[anio] = [0,0,0,0,0]
            c_contr[anio] = [0,0,0,0,0]
            c_odon[anio] = [0,0,0,0,0]
            c_odonr[anio] = [0,0,0,0,0]
            c_lab[anio] = [0,0,0,0,0]
            c_labr[anio] = [0,0,0,0,0]
            c_enf[anio] = [0,0,0,0,0]
            c_enfr[anio] = [0,0,0,0,0]
            c_med[anio] = [0,0,0,0,0]
            c_medr[anio] = [0,0,0,0,0]
            c_bio[anio] = [0,0,0,0,0]
            c_bior[anio] = [0,0,0,0,0]
            c_cso[anio] = [0,0,0,0,0]
            c_csor[anio] = [0,0,0,0,0]
            c_quim[anio] = [0,0,0,0,0]
            c_quimr[anio] = [0,0,0,0,0]
        #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
        curso ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if row[1] == "aprobado":
                capro += 1
                vapro[row[5]-1] += 1
                vareasApro[row[7]-1] += 1
            elif row[1] == "reprobado":
                caplaz += 1
                vaplaz[row[5]-1] += 1
                vareasApla[row[7]-1] += 1

            if row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango

                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))

                if row[1] == "aprobado":
                    if row[5] == 1:
                        c_infor[anoBD][row[3]-1]+=1
                    if row[5] == 2:
                        c_civil[anoBD][row[3]-1]+=1
                    if row[5] == 3:
                        c_minas[anoBD][row[3]-1]+=1
                    if row[5] == 4:
                        c_elec[anoBD][row[3]-1]+=1
                    if row[5] == 5:
                        c_mec[anoBD][row[3]-1]+=1
                    if row[5] == 6:
                        c_agro[anoBD][row[3]-1]+=1
                    if row[5] == 7:
                        c_lit[anoBD][row[3]-1]+=1
                    if row[5] == 8:
                        c_der[anoBD][row[3]-1]+=1
                    if row[5] == 9:
                        c_cie[anoBD][row[3]-1]+=1
                    if row[5] == 10:
                        c_cont[anoBD][row[3]-1]+=1
                    if row[5] == 11:
                        c_odon[anoBD][row[3]-1]+=1
                    if row[5] == 12:
                        c_lab[anoBD][row[3]-1]+=1
                    if row[5] == 13:
                        c_enf[anoBD][row[3]-1]+=1
                    if row[5] == 14:
                        c_med[anoBD][row[3]-1]+=1
                    if row[5] == 15:
                        c_bio[anoBD][row[3]-1]+=1
                    if row[5] == 16:
                        c_cso[anoBD][row[3]-1]+=1
                    if row[5] == 17:
                        c_quim[anoBD][row[3]-1]+=1

                elif row[1] == "reprobado":
                    if row[5] == 1:
                        c_inforr[anoBD][row[3]-1]+=1
                    if row[5] == 2:
                        c_civilr[anoBD][row[3]-1]+=1
                    if row[5] == 3:
                        c_minasr[anoBD][row[3]-1]+=1
                    if row[5] == 4:
                        c_elecr[anoBD][row[3]-1]+=1
                    if row[5] == 5:
                        c_mecr[anoBD][row[3]-1]+=1
                    if row[5] == 6:
                        c_agror[anoBD][row[3]-1]+=1
                    if row[5] == 7:
                        c_litr[anoBD][row[3]-1]+=1
                    if row[5] == 8:
                        c_derr[anoBD][row[3]-1]+=1
                    if row[5] == 9:
                        c_cier[anoBD][row[3]-1]+=1
                    if row[5] == 10:
                        c_contr[anoBD][row[3]-1]+=1
                    if row[5] == 11:
                        c_odonr[anoBD][row[3]-1]+=1
                    if row[5] == 12:
                        c_labr[anoBD][row[3]-1]+=1
                    if row[5] == 13:
                        c_enfr[anoBD][row[3]-1]+=1
                    if row[5] == 14:
                        c_medr[anoBD][row[3]-1]+=1
                    if row[5] == 15:
                        c_bior[anoBD][row[3]-1]+=1
                    if row[5] == 16:
                        c_csor[anoBD][row[3]-1]+=1
                    if row[5] == 17:
                        c_quimr[anoBD][row[3]-1]+=1

        print(c_infor)
        mensaje = "La cantidad de Estudiantes reprobados y aprobados "
        mensaje += " es lo siguiente por área y carreras"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"

        html += "<div class='row'>"
        html += "<h4 align='center'>Areas</h4>"
        for i in range(len(areasU)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"
            html += areasU[i]
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
            html+="<td>"+str(vareasApro[i])+"</td>"
            html+="<td>"+str(vareasApla[i])+"</td>"
            html+="</tr>"
            html+="</tbody>"
            html +="</table>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"

        h = 1
        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='row'>"
            html += "<h4 align = 'center'>Carrera</h4>"
            html += "<h5 align = 'center'>"+str(ac[i])+"</h5>"
            html += "<div class='col-lg-12' style = 'background-color:khaki;border: 1px solid black;'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"

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
            html+="<td>"+str(vapro[i])+"</td>"
            html+="<td>"+str(vaplaz[i])+"</td>"
            html+="</tr>"
            html+="</tbody>"
            html +="</table>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "<div class='row'>"
            k = 0
            for anio in range(a1, a2 + 1):#recorremos las fechas
                html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                for j in range(5):#recorremos todos los cursos aprobados por año

                    html += "<div class='col-lg-3'style = 'background-color:khaki;border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += curso[j]
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
                    if h == 1:
                        html += "<td>" + str(c_infor[anio][j]) + "</td><td> " + str(c_inforr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 2:
                        html += "<td>" + str(c_civil[anio][j]) + "</td><td> " + str(c_civilr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 3:
                        html += "<td>" + str(c_minas[anio][j]) + "</td><td> " + str(c_minasr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 4:
                        html += "<td>" + str(c_elec[anio][j]) + "</td><td> " + str(c_elecr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 5:
                        html += "<td>" + str(c_mec[anio][j]) + "</td><td> " + str(c_mecr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 6:
                        html += "<td>" + str(c_agro[anio][j]) + "</td><td> " + str(c_agror[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 7:
                        html += "<td>" + str(c_lit[anio][j]) + "</td><td> " + str(c_litr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 8:
                        html += "<td>" + str(c_der[anio][j]) + "</td><td> " + str(c_derr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 9:
                        html += "<td>" + str(c_cie[anio][j]) + "</td><td> " + str(c_cier[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 10:
                        html += "<td>" + str(c_cont[anio][j]) + "</td><td> " + str(c_contr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 11:
                        html += "<td>" + str(c_odon[anio][j]) + "</td><td> " + str(c_odonr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 12:
                        html += "<td>" + str(c_lab[anio][j]) + "</td><td> " + str(c_labr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 13:
                        html += "<td>" + str(c_enf[anio][j]) + "</td><td> " + str(c_enfr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 14:
                        html += "<td>" + str(c_med[anio][j]) + "</td><td> " + str(c_medr[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 15:
                        html += "<td>" + str(c_bio[anio][j]) + "</td><td> " + str(c_bior[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 16:
                        html += "<td>" + str(c_cso[anio][j]) + "</td><td> " + str(c_csor[anio][j]) + "</td>"  # Valores para cada sección de la torta
                    if h == 17:
                        html += "<td>" + str(c_quim[anio][j]) + "</td><td> " + str(c_quimr[anio][j]) + "</td>"  # es de la carrera de bioquimica

                    html+="</tr>"
                    html+="</tbody>"
                    html +="</table>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                k = k + 1
            h = h + 1
            html += "</div>"

        # Datos para el gráfico

    if accion1 == "seleccionar_estudiantes_desertores":
        fecha1 = ress[0]
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareasApro = [0] * 3
        vareasApla = [0] * 3
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
            print(anio, "  el ano es " )
            c_infor[anio] = [0,0,0,0,0]
            c_inforr[anio] = [0,0,0,0,0]
            c_civil[anio] = [0,0,0,0,0]
            c_civilr[anio] = [0,0,0,0,0]
            c_minas[anio] = [0,0,0,0,0]
            c_minasr[anio] = [0,0,0,0,0]
            c_elec[anio] = [0,0,0,0,0]
            c_elecr[anio] = [0,0,0,0,0]
            c_mec[anio] = [0,0,0,0,0]
            c_mecr[anio] = [0,0,0,0,0]
            c_agro[anio] = [0,0,0,0,0]
            c_agror[anio] = [0,0,0,0,0]
            c_lit[anio] = [0,0,0,0,0]
            c_litr[anio] = [0,0,0,0,0]
            c_der[anio] = [0,0,0,0,0]
            c_derr[anio] = [0,0,0,0,0]
            c_cie[anio] = [0,0,0,0,0]
            c_cier[anio] = [0,0,0,0,0]
            c_cont[anio] = [0,0,0,0,0]
            c_contr[anio] = [0,0,0,0,0]
            c_odon[anio] = [0,0,0,0,0]
            c_odonr[anio] = [0,0,0,0,0]
            c_lab[anio] = [0,0,0,0,0]
            c_labr[anio] = [0,0,0,0,0]
            c_enf[anio] = [0,0,0,0,0]
            c_enfr[anio] = [0,0,0,0,0]
            c_med[anio] = [0,0,0,0,0]
            c_medr[anio] = [0,0,0,0,0]
            c_bio[anio] = [0,0,0,0,0]
            c_bior[anio] = [0,0,0,0,0]
            c_cso[anio] = [0,0,0,0,0]
            c_csor[anio] = [0,0,0,0,0]
            c_quim[anio] = [0,0,0,0,0]
            c_quimr[anio] = [0,0,0,0,0]
        #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
        curso ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango
                if row[2] == "no":#no abandonaron
                    capro += 1
                    vapro[row[5]-1] += 1
                    vareasApro[row[7]-1] += 1
                elif row[2] == "si":#si abandonaron
                    caplaz += 1
                    vaplaz[row[5]-1] += 1
                    vareasApla[row[7]-1] += 1

                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))

                if row[2] == "no":
                    if row[5] == 1:
                        c_infor[anoBD][row[3]-1]+=1
                    if row[5] == 2:
                        c_civil[anoBD][row[3]-1]+=1
                    if row[5] == 3:
                        c_minas[anoBD][row[3]-1]+=1
                    if row[5] == 4:
                        c_elec[anoBD][row[3]-1]+=1
                    if row[5] == 5:
                        c_mec[anoBD][row[3]-1]+=1
                    if row[5] == 6:
                        c_agro[anoBD][row[3]-1]+=1
                    if row[5] == 7:
                        c_lit[anoBD][row[3]-1]+=1
                    if row[5] == 8:
                        c_der[anoBD][row[3]-1]+=1
                    if row[5] == 9:
                        c_cie[anoBD][row[3]-1]+=1
                    if row[5] == 10:
                        c_cont[anoBD][row[3]-1]+=1
                    if row[5] == 11:
                        c_odon[anoBD][row[3]-1]+=1
                    if row[5] == 12:
                        c_lab[anoBD][row[3]-1]+=1
                    if row[5] == 13:
                        c_enf[anoBD][row[3]-1]+=1
                    if row[5] == 14:
                        c_med[anoBD][row[3]-1]+=1
                    if row[5] == 15:
                        c_bio[anoBD][row[3]-1]+=1
                    if row[5] == 16:
                        c_cso[anoBD][row[3]-1]+=1
                    if row[5] == 17:
                        c_quim[anoBD][row[3]-1]+=1

                elif row[2] == "si":
                    if row[5] == 1:
                        c_inforr[anoBD][row[3]-1]+=1
                    if row[5] == 2:
                        c_civilr[anoBD][row[3]-1]+=1
                    if row[5] == 3:
                        c_minasr[anoBD][row[3]-1]+=1
                    if row[5] == 4:
                        c_elecr[anoBD][row[3]-1]+=1
                    if row[5] == 5:
                        c_mecr[anoBD][row[3]-1]+=1
                    if row[5] == 6:
                        c_agror[anoBD][row[3]-1]+=1
                    if row[5] == 7:
                        c_litr[anoBD][row[3]-1]+=1
                    if row[5] == 8:
                        c_derr[anoBD][row[3]-1]+=1
                    if row[5] == 9:
                        c_cier[anoBD][row[3]-1]+=1
                    if row[5] == 10:
                        c_contr[anoBD][row[3]-1]+=1
                    if row[5] == 11:
                        c_odonr[anoBD][row[3]-1]+=1
                    if row[5] == 12:
                        c_labr[anoBD][row[3]-1]+=1
                    if row[5] == 13:
                        c_enfr[anoBD][row[3]-1]+=1
                    if row[5] == 14:
                        c_medr[anoBD][row[3]-1]+=1
                    if row[5] == 15:
                        c_bior[anoBD][row[3]-1]+=1
                    if row[5] == 16:
                        c_csor[anoBD][row[3]-1]+=1
                    if row[5] == 17:
                        c_quimr[anoBD][row[3]-1]+=1

        mensaje = "La cantidad de estudiantes que desertaron "
        mensaje += "es lo siguiente por área y carreras"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        # Crear el gráfico de torta
        html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
        html += "<h5 align='center'>Total</h5>"
        html += "<div class='col-lg-12'>"
        html += "<div class='panel panel-default text-center bg-light' style = 'border: 1px solid black;'>"
        html += "<div class='panel-heading'>"
        html += "</div>"
        html += "<div class='panel-body'>"
        html += "<center><h6>Estudiantes que siguen son: "+str(capro)+"</h6></center>"
        html += "<center><h6>Estudiantes que abandonaron son: "+str(caplaz)+"</h6></center>"
        html += "</div>"
        html += "</div>"
        html += "</div>"
        html += "</div>"
        html += "<br>"
        #crear para areas
        html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
        html += "<h4 align='center'>Areas</h4>"
        print("areas son ",len(areasU), areasU[1])
        for i in range(len(areasU)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-4'>"
            html += "<div class='panel panel-default text-center bg-info' style = 'border: 1px solid black;'>"
            html += "<div class='panel-heading'>"
            html += areasU[i]
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><h6>Estudiantes que siguen son: "+str(vareasApro[i])+"</h6></center>"
            html += "<center><h6>Estudiantes que abandonaron son: "+str(vareasApla[i])+"</h6></center>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"
        html += "<br>"
        h = 1

        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='row bg-warning'>"
            html += "<h5 align = 'center'>Carrera</h5>"
            html += "<h6 align = 'center'>"+ac[i]+"</h6>"
            html += "<div class='col-lg-12 p-4' style = 'background-color:RGBA(255, 250, 0, 0.5)'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><h6>Estudiantes que siguen son: "+str(vapro[i])+"</h6></center>"
            html += "<center><h6>Estudiantes que abandonaron son: "+str(vaplaz[i])+"</h6></center>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "<div class='row'>"
            k = 0
            for anio in range(a1, a2 + 1):#recorremos las fechas
                html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                for j in range(5):#recorremos todos los cursos aprobados por año

                    html += "<div class='col-lg-3' style = 'background-color:RGBA(0, 255, 250, 0.3);border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += "<b>"+curso[j]+"</b>"
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    if h == 1:
                        html += "<h6>Estudiantes que siguen son: " + str(c_infor[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_inforr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 2:
                        html += "<h6>Estudiantes que siguen son: " + str(c_civil[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_civilr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 3:
                        html += "<h6>Estudiantes que siguen son: " + str(c_minas[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_minasr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 4:
                        html += "<h6>Estudiantes que siguen son: " + str(c_elec[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_elecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 5:
                        html += "<h6>Estudiantes que siguen son: " + str(c_mec[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_mecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 6:
                        html += "<h6>Estudiantes que siguen son: " + str(c_agro[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_agror[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 7:
                        html += "<h6>Estudiantes que siguen son: " + str(c_lit[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_litr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 8:
                        html += "<h6>Estudiantes que siguen son: " + str(c_der[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_derr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 9:
                        html += "<h6>Estudiantes que siguen son: " + str(c_cie[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_cier[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 10:
                        html += "<h6>Estudiantes que siguen son: " + str(c_cont[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_contr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 11:
                        html += "<h6>Estudiantes que siguen son: " + str(c_odon[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_odonr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 12:
                        html += "<h6>Estudiantes que siguen son: " + str(c_lab[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_labr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 13:
                        html += "<h6>Estudiantes que siguen son: " + str(c_enf[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_enfr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 14:
                        html += "<h6>Estudiantes que siguen son: " + str(c_med[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_medr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 15:
                        html += "<h6>Estudiantes que siguen son: " + str(c_bio[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_bior[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 16:
                        html += "<h6>Estudiantes que siguen son: " + str(c_cso[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_csor[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    if h == 17:
                        html += "<h6>Estudiantes que siguen son: " + str(c_quim[anio][j]) + "</h6>"
                        html +="<h6>Estudiantes que abandonaron son: " + str(c_quimr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                k = k + 1
            h = h + 1
            html += "</div>"
            html += "<br>"
    if accion1 == "diferencia_entre_primero_quinto":
        fecha1 = ress[0]
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareasApro = [0] * 3
        vareasApla = [0] * 3
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
            c_infor[anio] = [0,0,0,0,0]
            c_inforr[anio] = [0,0,0,0,0]
            c_civil[anio] = [0,0,0,0,0]
            c_civilr[anio] = [0,0,0,0,0]
            c_minas[anio] = [0,0,0,0,0]
            c_minasr[anio] = [0,0,0,0,0]
            c_elec[anio] = [0,0,0,0,0]
            c_elecr[anio] = [0,0,0,0,0]
            c_mec[anio] = [0,0,0,0,0]
            c_mecr[anio] = [0,0,0,0,0]
            c_agro[anio] = [0,0,0,0,0]
            c_agror[anio] = [0,0,0,0,0]
            c_lit[anio] = [0,0,0,0,0]
            c_litr[anio] = [0,0,0,0,0]
            c_der[anio] = [0,0,0,0,0]
            c_derr[anio] = [0,0,0,0,0]
            c_cie[anio] = [0,0,0,0,0]
            c_cier[anio] = [0,0,0,0,0]
            c_cont[anio] = [0,0,0,0,0]
            c_contr[anio] = [0,0,0,0,0]
            c_odon[anio] = [0,0,0,0,0]
            c_odonr[anio] = [0,0,0,0,0]
            c_lab[anio] = [0,0,0,0,0]
            c_labr[anio] = [0,0,0,0,0]
            c_enf[anio] = [0,0,0,0,0]
            c_enfr[anio] = [0,0,0,0,0]
            c_med[anio] = [0,0,0,0,0]
            c_medr[anio] = [0,0,0,0,0]
            c_bio[anio] = [0,0,0,0,0]
            c_bior[anio] = [0,0,0,0,0]
            c_cso[anio] = [0,0,0,0,0]
            c_csor[anio] = [0,0,0,0,0]
            c_quim[anio] = [0,0,0,0,0]
            c_quimr[anio] = [0,0,0,0,0]
        #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
        curso ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:
            if row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango
                if row[3] == 1:#contar los de primer año
                    capro += 1
                    vapro[row[5]-1] += 1
                    vareasApro[row[7]-1] += 1
                elif row[3] == 5:#contar los de 5to añp
                    caplaz += 1
                    vaplaz[row[5]-1] += 1
                    vareasApla[row[7]-1] += 1
                anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))

                if row[3] == 1:#contamos solo de primer año
                    if row[5] == 1:
                        c_infor[anoBD][0]+=1
                    if row[5] == 2:
                        c_civil[anoBD][0]+=1
                    if row[5] == 3:
                        c_minas[anoBD][0]+=1
                    if row[5] == 4:
                        c_elec[anoBD][0]+=1
                    if row[5] == 5:
                        c_mec[anoBD][0]+=1
                    if row[5] == 6:
                        c_agro[anoBD][0]+=1
                    if row[5] == 7:
                        c_lit[anoBD][0]+=1
                    if row[5] == 8:
                        c_der[anoBD][0]+=1
                    if row[5] == 9:
                        c_cie[anoBD][0]+=1
                    if row[5] == 10:
                        c_cont[anoBD][0]+=1
                    if row[5] == 11:
                        c_odon[anoBD][0]+=1
                    if row[5] == 12:
                        c_lab[anoBD][0]+=1
                    if row[5] == 13:
                        c_enf[anoBD][0]+=1
                    if row[5] == 14:
                        c_med[anoBD][0]+=1
                    if row[5] == 15:
                        c_bio[anoBD][0]+=1
                    if row[5] == 16:
                        c_cso[anoBD][0]+=1
                    if row[5] == 17:
                        c_quim[anoBD][0]+=1

                elif row[3] == 5 and row[1] == "aprobado":#contamos solo de 5to año y aprobados
                    if row[5] == 1:
                        c_inforr[anoBD][0]+=1
                    if row[5] == 2:
                        c_civilr[anoBD][0]+=1
                    if row[5] == 3:
                        c_minasr[anoBD][0]+=1
                    if row[5] == 4:
                        c_elecr[anoBD][0]+=1
                    if row[5] == 5:
                        c_mecr[anoBD][0]+=1
                    if row[5] == 6:
                        c_agror[anoBD][0]+=1
                    if row[5] == 7:
                        c_litr[anoBD][0]+=1
                    if row[5] == 8:
                        c_derr[anoBD][0]+=1
                    if row[5] == 9:
                        c_cier[anoBD][0]+=1
                    if row[5] == 10:
                        c_contr[anoBD][0]+=1
                    if row[5] == 11:
                        c_odonr[anoBD][0]+=1
                    if row[5] == 12:
                        c_labr[anoBD][0]+=1
                    if row[5] == 13:
                        c_enfr[anoBD][0]+=1
                    if row[5] == 14:
                        c_medr[anoBD][0]+=1
                    if row[5] == 15:
                        c_bior[anoBD][0]+=1
                    if row[5] == 16:
                        c_csor[anoBD][0]+=1
                    if row[5] == 17:
                        c_quimr[anoBD][0]+=1

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
        html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
        html += "<h4 align='center'>Areas</h4>"
        print("areas son ",len(areasU), areasU[1])
        for i in range(len(areasU)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-4'>"
            html += "<div class='panel panel-default text-center bg-info' style = 'border: 1px solid black;'>"
            html += "<div class='panel-heading'>"
            html += areasU[i]
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><h6>Los estudiantes de 1er año son "+str(vareasApro[i])+"</h6></center>"
            html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vareasApla[i])+"</h6></center>"
            html += menCOncluyeron(vareasApro[i],vareasApla[i])
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"
        html += "<br>"
        h = 1

        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='row bg-warning'>"
            html += "<h5 align = 'center'>Carrera</h5>"
            html += "<h6 align = 'center'>"+ac[i]+"</h6>"
            html += "<div class='col-lg-12 p-4' style = 'background-color:RGBA(255, 250, 0, 0.5)'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><h6>Los estudiantes de 1er año son "+str(vapro[i])+"</h6></center>"
            html += "<center><h6>y estudiantes de 5to año que conluyeron sus estudios son "+str(vaplaz[i])+"</h6></center>"
            html += menCOncluyeron(vapro[i],vaplaz[i])
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "<div class='row'>"
            k = 0
            for anio in range(a1, a2 + 1):#recorremos las fechas
                html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                for j in range(1):#recorremos todos los cursos aprobados por año
                    html += "<div class='col-lg-12' style = 'background-color:RGBA(0, 255, 250, 0.3);border: 1px solid black;'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"

                    html += "</div>"
                    html += "<div class='panel-body'>"
                    if h == 1:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_infor[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_inforr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_infor[anio][j],c_inforr[anio][j])
                    if h == 2:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_civil[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_civilr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_civil[anio][j],c_civilr[anio][j])
                    if h == 3:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_minas[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_minasr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_minas[anio][j],c_minasr[anio][j])
                    if h == 4:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_elec[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_elecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_elec[anio][j],c_elecr[anio][j])
                    if h == 5:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_mec[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_mecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_mec[anio][j],c_mecr[anio][j])
                    if h == 6:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_agro[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_agror[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_agro[anio][j],c_agror[anio][j])
                    if h == 7:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_lit[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_litr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_lit[anio][j],c_litr[anio][j])
                    if h == 8:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_der[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_derr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_der[anio][j],c_derr[anio][j])
                    if h == 9:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_cie[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_cier[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_cie[anio][j],c_cier[anio][j])
                    if h == 10:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_cont[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_contr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_cont[anio][j],c_contr[anio][j])
                    if h == 11:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_odon[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_odonr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_odon[anio][j],c_odonr[anio][j])
                    if h == 12:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_lab[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_labr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_lab[anio][j],c_labr[anio][j])
                    if h == 13:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_enf[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_enfr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_enf[anio][j],c_enfr[anio][j])
                    if h == 14:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_med[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_medr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_med[anio][j],c_medr[anio][j])
                    if h == 15:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_bio[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_bior[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_bio[anio][j],c_bior[anio][j])
                    if h == 16:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_cso[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_csor[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_cso[anio][j],c_csor[anio][j])
                    if h == 17:
                        html += "<h6>Los estudiantes de 1er año son " + str(c_quim[anio][j]) + "</h6>"
                        html +="<h6>y estudiantes de 5to año que conluyeron sus estudios son " + str(c_quimr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
                        html += menCOncluyeron(c_quim[anio][j],c_quimr[anio][j])
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                k = k + 1
            h = h + 1
            html += "</div>"
            html += "<br>"
    if accion1 == 'asignaturas_desercion':
        fecha1 = ress[0]
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareasT = {}
        vareasTr = {}
        vareasS = {}
        vareasSr = {}
        vareasSo = {}
        vareasSor = {}
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
        for ar in range(3):
            are = seleccionarAsignaturaAreas((ar+1),1)
            vareasT[ar+1] = {}
            vareasTr[ar+1]={}
            vareasS[ar+1]={}
            vareasSr[ar+1]={}
            vareasSo[ar+1]={}
            vareasSor[ar+1]={}
            if are != "no":
                for arr in are:
                    if arr[10] == 1:
                        vareasT[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]
                        vareasTr[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]
                    elif arr[10] == 2:
                        vareasS[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]
                        vareasSr[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]
                    elif arr[10] == 3:
                        vareasSo[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]
                        vareasSor[ar+1][arr[0]]=[0,arr[8],arr[0],arr[10]]

        for car in range(17):
            asig = seleccionarAsignatura((car+1),1)##enviamos el id de la carrera y el plan de estudio
            if asig != "no":
                for anio in range(a1, a2 + (1)):
                    c_infor[anio] = {}
                    c_civil[anio] = {}
                    c_minas[anio] = {}
                    c_elec[anio] = {}
                    c_mec[anio] = {}
                    c_agro[anio] = {}
                    c_lit[anio] = {}
                    c_der[anio] = {}
                    c_cie[anio] = {}
                    c_cont[anio] = {}
                    c_odon[anio] = {}
                    c_lab[anio] = {}
                    c_enf[anio] = {}
                    c_med[anio] = {}
                    c_bio[anio] = {}
                    c_cso[anio] = {}
                    c_quim[anio] = {}
                    c_inforr[anio] = {}
                    c_civilr[anio] = {}
                    c_minasr[anio] = {}
                    c_elecr[anio] = {}
                    c_mecr[anio] = {}
                    c_agror[anio] = {}
                    c_litr[anio] = {}
                    c_derr[anio] = {}
                    c_cier[anio] = {}
                    c_contr[anio] = {}
                    c_odonr[anio] = {}
                    c_labr[anio] = {}
                    c_enfr[anio] = {}
                    c_medr[anio] = {}
                    c_bior[anio] = {}
                    c_csor[anio] = {}
                    c_quimr[anio] = {}
                    for arr in asig:
                        if arr[8] == 1:#carrera 1 informatica
                        #año id de asignatura  = contar id grado id asignatura
                            c_infor[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_inforr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 2:
                            c_civil[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_civilr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 3:
                            c_minas[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_minasr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 4:
                            c_elec[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_elecr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 5:
                            c_mec[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_mecr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 6:
                            c_agro[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_agror[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 7:
                            c_lit[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_litr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 8:
                            c_der[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_derr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 9:
                            c_cie[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_cier[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 10:
                            c_cont[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_contr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 11:
                            c_odon[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_odonr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 12:
                            c_lab[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_labr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 13:
                            c_enf[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_enfr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 14:
                            c_med[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_medr[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 15:
                            c_bio[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_bior[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 16:
                            c_cso[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_csor[anio][arr[0]] = [0,arr[9],arr[0]]
                        elif arr[8] == 17:
                            c_quim[anio][arr[0]] = [0,arr[9],arr[0]]
                            c_quimr[anio][arr[0]] = [0,arr[9],arr[0]]

       #carrerarr_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
        cursoss ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[14]>=fecha1 and row[14] <= fecha2:
                if row[4] == 'si':#contar los de primer año
                    if row[12] == 1:
                        vareasT[row[12]][row[8]][0]+=1
                    elif row[12] == 2:
                        vareasS[row[12]][row[8]][0]+=1
                    elif row[12] == 3:
                        vareasSo[row[12]][row[8]][0]+=1
                elif row[4] == 'no':#contar los de 5to añp
                    if row[12] == 1:
                        vareasTr[row[12]][row[8]][0]+=1
                    elif row[12] == 2:
                        vareasSr[row[12]][row[8]][0]+=1
                    elif row[12] == 3:
                        vareasSor[row[12]][row[8]][0]+=1

                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))

                if row[4] == 'si':#si esta en el campo de desercion estonces ingresa
                    if row[10] == 1:
                        c_infor[anoBD][row[8]][0]+=1
                    elif row[10] == 2:
                        c_civil[anoBD][row[8]][0]+=1
                    elif row[10] == 3:
                        c_minas[anoBD][row[8]][0]+=1
                    elif row[10] == 4:
                        c_elec[anoBD][row[8]][0]+=1
                    elif row[10] == 5:
                        c_mec[anoBD][row[8]][0]+=1
                    elif row[10] == 6:
                        c_agro[anoBD][row[8]][0]+=1
                    elif row[10] == 7:
                        c_lit[anoBD][row[8]][0]+=1
                    elif row[10] == 8:
                        c_der[anoBD][row[8]][0]+=1
                    elif row[10] == 9:
                        c_cie[anoBD][row[8]][0]+=1
                    elif row[10] == 10:
                        c_cont[anoBD][row[8]][0]+=1
                    elif row[10] == 11:
                        c_odon[anoBD][row[8]][0]+=1
                    elif row[10] == 12:
                        c_lab[anoBD][row[8]][0]+=1
                    elif row[10] == 13:
                        c_enf[anoBD][row[8]][0]+=1
                    elif row[10] == 14:
                        c_med[anoBD][row[8]][0]+=1
                    elif row[10] == 15:
                        c_bio[anoBD][row[8]][0]+=1
                    elif row[10] == 16:
                        c_cso[anoBD][row[8]][0]+=1
                    elif row[10] == 17:
                        c_quim[anoBD][row[8]][0]+=1

                elif row[4] == 'no':#contamos solo de 5to año y aprobados
                    if row[10] == 1:
                        c_inforr[anoBD][row[8]][0]+=1
                    elif row[10] == 2:
                        c_civilr[anoBD][row[8]][0]+=1
                    elif row[10] == 3:
                        c_minasr[anoBD][row[8]][0]+=1
                    elif row[10] == 4:
                        c_elecr[anoBD][row[8]][0]+=1
                    elif row[10] == 5:
                        c_mecr[anoBD][row[8]][0]+=1
                    elif row[10] == 6:
                        c_agror[anoBD][row[8]][0]+=1
                    elif row[10] == 7:
                        c_litr[anoBD][row[8]][0]+=1
                    elif row[10] == 8:
                        c_derr[anoBD][row[8]][0]+=1
                    elif row[10] == 9:
                        c_cier[anoBD][row[8]][0]+=1
                    elif row[10] == 10:
                        c_contr[anoBD][row[8]][0]+=1
                    elif row[10] == 11:
                        c_odonr[anoBD][row[8]][0]+=1
                    elif row[10] == 12:
                        c_labr[anoBD][row[8]][0]+=1
                    elif row[10] == 13:
                        c_enfr[anoBD][row[8]][0]+=1
                    elif row[10] == 14:
                        c_medr[anoBD][row[8]][0]+=1
                    elif row[10] == 15:
                        c_bior[anoBD][row[8]][0]+=1
                    elif row[10] == 16:
                        c_csor[anoBD][row[8]][0]+=1
                    elif row[10] == 17:
                        c_quimr[anoBD][row[8]][0]+=1

        mensaje = "Las asignaturas que tienen mas estudiantes desertores"
        mensaje += " por áreas y carreras, detallamos en los siguientes cuadros"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        # Crear el gráfico de torta

        #crear para areas
        html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
        html += "<h4 align='center'>Areas</h4>"
        k1 = 1
        for i in range(3):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera

            are = seleccionarAsignaturaAreas((i+1),1)#seleccionamos las asingturas con el cod de area

            if are != "no":
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center bg-info' style = 'border: 1px solid black;'>"
                html += "<div class='panel-heading'>"
                html += areasU[i]
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
                for asi in are:
                    if vareasT[i+1][asi[0]][3] == (i+1):
                        if vareasT[i+1][asi[0]][0] > 0:
                            html += "<tr><td>"+str(nombre_asignatura(vareasT[i+1][asi[0]][2]))+"</td>"
                            html += "<td>"+str((vareasT[i+1][asi[0]][0]))+"</td>"
                            html += "<td>"+str(nombre_carrera_retor(vareasT[i+1][asi[0]][1]))+"</td></tr>"
                            #html += "<td>"+str(nombre_carrera(vareasT[i+1][asi[0]].get(1)))+"</td></tr>"
                    elif vareasS[i+1][asi[0]][3] == (i+1):
                        if vareasS[i+1][asi[0]][0] > 0:
                            html += "<tr><td>"+str(nombre_asignatura(vareasS[i+1][asi[0]][2]))+"</td>"
                            html += "<td>"+str((vareasS[i+1][asi[0]][0]))+"</td>"
                            html += "<td>"+str(nombre_carrera_retor(vareasT[i+1][asi[0]][1]))+"</td></tr>"
                            #html += "<td>"+str(nombre_carrera(vareasS[i+1][asi[0]][1]))+"</td></tr>"
                    elif vareasSo[i+1][asi[0]][3] == (i+1):
                        if vareasSo[i+1][asi[0]][0] > 0:
                            html += "<tr><td>"+str(nombre_asignatura(vareasSo[i+1][asi[0]][2]))+"</td>"
                            html += "<td>"+str((vareasSo[i+1][asi[0]][0]))+"</td>"
                            html += "<td>"+str(nombre_carrera_retor(vareasT[i+1][asi[0]][1]))+"</td></tr>"

                            #html += "<td>"+str(nombre_carrera(vareasSo[i+1][asi[0]][1]))+"</td></tr>"
                   #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                html += "<tbody>"
                html += "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
            else:
                html += "<div class='col-lg-4' style = 'background-color:khaki;border: 1px solid black;'>"
                html += "<div class='panel panel-default text-center'>"
                html += "<div class='panel-heading'>"
                html+="<h6>No se encontro información</h6>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
        html += "</div>"
        html += "<br>"
        h = 1
        colorr ={0:'beige',1:'Gainsboro',2:'Khaki',3:'Lavender',4:'LightYellow'}
        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            asig = seleccionarAsignatura((i+1),1)#seleccionamos las asiganturas con el cod id
            html+="<h5 align='center'>Carrera "+nombre_carrera_retor(i+1)+"</h5>"
            if asig != "no":
                html += "<div class='row'>"#abrimos una fila
                for anio in range(a1, a2 + 1):#recorremos las fechas
                    html += "<h6 align='center'>Año "+str(anio)+"</h6>"
                    for g in range(5):#recorremos los cursos
                        html += "<div class='col-lg-3' style = 'background-color:"+str(colorr[g])+";border: 1px solid black;'>"
                        html += "<div class='panel panel-default text-center'>"
                        html += "<div class='panel-heading'>"
                        html += cursoss[g]#imprimimos el curso
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

                            if h == 1: #si carrera es igual a 1 ingresa
                                if (g+1) == c_infor[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_infor[anio][asi[0]][0] > 0:
                                        #print(c_infor[anio][asi[0]][0]," = ",c_infor[anio][asi[0]][1])
                                        html += "<tr><td>"+str(nombre_asignatura(c_infor[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_infor[anio][asi[0]][0]))+"</td></tr>"
                            if h == 2:
                                if (g+1) == c_civil[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_civil[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_civil[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_civil[anio][asi[0]][0]))+"</td></tr>"
                            if h == 3:
                                if (g+1) == c_minas[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_minas[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_minas[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_minas[anio][asi[0]][0]))+"</td></tr>"
                            if h == 4:
                                if (g+1) == c_elec[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_elec[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_elec[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_elec[anio][asi[0]][0]))+"</td></tr>"
                            if h == 5:
                                if (g+1) == c_mec[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_mec[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_mec[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_mec[anio][asi[0]][0]))+"</td></tr>"
                            if h == 6:
                                if (g+1) == c_agro[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_agro[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_agro[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_agro[anio][asi[0]][0]))+"</td></tr>"
                            if h == 7:
                                if (g+1) == c_lit[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_lit[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_lit[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_lit[anio][asi[0]][0]))+"</td></tr>"
                            if h == 8:
                                if (g+1) == c_der[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_der[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_der[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_der[anio][asi[0]][0]))+"</td></tr>"
                            if h == 9:
                                if (g+1) == c_cie[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_cie[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_cie[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_cie[anio][asi[0]][0]))+"</td></tr>"
                            if h == 10:
                                if (g+1) == c_cont[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_cont[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_cont[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_cont[anio][asi[0]][0]))+"</td></tr>"
                            if h == 11:
                                if (g+1) == c_odon[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_odon[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_odon[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_odon[anio][asi[0]][0]))+"</td></tr>"
                            if h == 12:
                                if (g+1) == c_lab[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_lab[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_lab[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_lab[anio][asi[0]][0]))+"</td></tr>"
                            if h == 13:
                                if (g+1) == c_enf[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_enf[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_enf[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_enf[anio][asi[0]][0]))+"</td></tr>"
                            if h == 14:
                                if (g+1) == c_med[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_med[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_med[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_med[anio][asi[0]][0]))+"</td></tr>"
                            if h == 15:
                                if (g+1) == c_bio[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_bio[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_bio[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_bio[anio][asi[0]][0]))+"</td></tr>"
                            if h == 16:
                                if (g+1) == c_cso[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_cso[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_cso[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_cso[anio][asi[0]][0]))+"</td></tr>"

                            if h == 17:
                                if (g+1) == c_quim[anio][asi[0]][1]:#si el curso es igual a primero
                                    if c_quim[anio][asi[0]][0] > 0:
                                        html += "<tr><td>"+str(nombre_asignatura(c_quim[anio][asi[0]][2]))+"</td>"
                                        html += "<td>"+str((c_quim[anio][asi[0]][0]))+"</td></tr>"
                                  #html += menCOncluyeron(vareasApro[i],vareasApla[i])
                        html += "<tbody>"
                        html += "</table>"
                        html += "</div>"
                        html += "</div>"
                        html += "</div>"

                h = h + 1
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
        fecha1 = ress[0]
        fecha2 = ress[1]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareas = {}
        vareasr = {}
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
            ##enviamos el id de la carrera y el plan de estudio
        for j in range(3):
            vareas[j+1] = 0
            vareasr[j+1] = 0
        for anio in range(a1, a2 + (1)):
            c_infor[anio] = 0
            c_civil[anio] = 0
            c_minas[anio] = 0
            c_elec[anio] = 0
            c_mec[anio] = 0
            c_agro[anio] = 0
            c_lit[anio] = 0
            c_der[anio] = 0
            c_cie[anio] = 0
            c_cont[anio] = 0
            c_odon[anio] = 0
            c_lab[anio] = 0
            c_enf[anio] = 0
            c_med[anio] = 0
            c_bio[anio] = 0
            c_cso[anio] = 0
            c_quim[anio] = 0
            c_inforr[anio] = 0
            c_civilr[anio] = 0
            c_minasr[anio] = 0
            c_elecr[anio] = 0
            c_mecr[anio] = 0
            c_agror[anio] = 0
            c_litr[anio] = 0
            c_derr[anio] = 0
            c_cier[anio] = 0
            c_contr[anio] = 0
            c_odonr[anio] = 0
            c_labr[anio] = 0
            c_enfr[anio] = 0
            c_medr[anio] = 0
            c_bior[anio] = 0
            c_csor[anio] = 0
            c_quimr[anio] = 0

       #carrerarr_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
        cursoss ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[16]>=fecha1 and row[16] <= fecha2:
                if row[11] == 'masculino':#contar los de primer año
                    vareas[row[12]]+=1
                elif row[11] == 'femenino':#contar los de 5to añp
                    vareasr[row[12]]+=1

                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))

                if row[11] == 'masculino':#contamos solo de primer año
                    if row[13] == 1:
                        c_infor[anoBD]+=1
                    elif row[13] == 2:
                        c_civil[anoBD]+=1
                    elif row[13] == 3:
                        c_minas[anoBD]+=1
                    elif row[13] == 4:
                        c_elec[anoBD]+=1
                    elif row[13] == 5:
                        c_mec[anoBD]+=1
                    elif row[13] == 6:
                        c_agro[anoBD]+=1
                    elif row[13] == 7:
                        c_lit[anoBD]+=1
                    elif row[13] == 8:
                        c_der[anoBD]+=1
                    elif row[13] == 9:
                        c_cie[anoBD]+=1
                    elif row[13] == 10:
                        c_cont[anoBD]+=1
                    elif row[13] == 11:
                        c_odon[anoBD]+=1
                    elif row[13] == 12:
                        c_lab[anoBD]+=1
                    elif row[13] == 13:
                        c_enf[anoBD]+=1
                    elif row[13] == 14:
                        c_med[anoBD]+=1
                    elif row[13] == 15:
                        c_bio[anoBD]+=1
                    elif row[13] == 16:
                        c_cso[anoBD]+=1
                    elif row[13] == 17:
                        c_quim[anoBD]+=1

                elif row[11] == 'femenino':#contamos solo de 5to año y aprobados
                    if row[13] == 1:
                        c_inforr[anoBD]+=1
                    elif row[13] == 2:
                        c_civilr[anoBD]+=1
                    elif row[13] == 3:
                        c_minasr[anoBD]+=1
                    elif row[13] == 4:
                        c_elecr[anoBD]+=1
                    elif row[13] == 5:
                        c_mecr[anoBD]+=1
                    elif row[13] == 6:
                        c_agror[anoBD]+=1
                    elif row[13] == 7:
                        c_litr[anoBD]+=1
                    elif row[13] == 8:
                        c_derr[anoBD]+=1
                    elif row[13] == 9:
                        c_cier[anoBD]+=1
                    elif row[13] == 10:
                        c_contr[anoBD]+=1
                    elif row[13] == 11:
                        c_odonr[anoBD]+=1
                    elif row[13] == 12:
                        c_labr[anoBD]+=1
                    elif row[13] == 13:
                        c_enfr[anoBD]+=1
                    elif row[13] == 14:
                        c_medr[anoBD]+=1
                    elif row[13] == 15:
                        c_bior[anoBD]+=1
                    elif row[13] == 16:
                        c_csor[anoBD]+=1
                    elif row[13] == 17:
                        c_quimr[anoBD]+=1

        mensaje = "La cantidad de estudiantes clasificado por varones y mujeres"
        mensaje += " detallamos en los siguientes cuadros por area y carreras"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        # Crear el gráfico de torta

        #crear para areas
        html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
        html += "<h4 align='center'>Areas</h4>"
        k1 = 1
        for i in range(3):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-4'>"
            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
            html += "<div class='panel-heading'>"
            html += areasU[i]
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
            html += "<tr><td>"+str(vareas[i+1])+"</td>"
            html += "<td>"+str(vareasr[i+1])+"</td></tr>"
            html += "<tbody>"
            html += "</table>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"
        html += "<br>"
        h = 1
        colorr ={0:'beige',1:'Gainsboro',2:'Khaki',3:'Lavender',4:'LightYellow'}
        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html+="<h5 align='center'>Carrera "+nombre_carrera_retor(i+1)+"</h5>"#nombre de la carrera
            html+="<div class='row'>"
            for anio in range(a1, a2 + (1)):#recoremos los anos que pueden sere desde una año inicio a un año fin
                html += "<div class='col-lg-3' style = 'background-color:khaki;border: 1px solid black;'>"
                html += "<div class='panel panel-default text-center'>"
                html += "<div class='panel-heading'>"
                html += str(anio)
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
                if h == 1: #si carrera es igual a 1 ingresa
                    html += "<tr><td>"+str(c_infor[anio])+"</td>"
                    html += "<td>"+str(c_inforr[anio])+"</td></tr>"
                if h == 2:
                    html += "<tr><td>"+str(c_civil[anio])+"</td>"
                    html += "<td>"+str(c_civilr[anio])+"</td></tr>"
                if h == 3:
                    html += "<tr><td>"+str(c_minas[anio])+"</td>"
                    html += "<td>"+str(c_minasr[anio])+"</td></tr>"
                if h == 4:
                    html += "<tr><td>"+str(c_elec[anio])+"</td>"
                    html += "<td>"+str(c_elecr[anio])+"</td></tr>"
                if h == 5:
                    html += "<tr><td>"+str(c_mec[anio])+"</td>"
                    html += "<td>"+str(c_mecr[anio])+"</td></tr>"
                if h == 6:
                    html += "<tr><td>"+str(c_agro[anio])+"</td>"
                    html += "<td>"+str(c_agror[anio])+"</td></tr>"
                if h == 7:
                    html += "<tr><td>"+str(c_lit[anio])+"</td>"
                    html += "<td>"+str(c_litr[anio])+"</td></tr>"
                if h == 8:
                    html += "<tr><td>"+str(c_der[anio])+"</td>"
                    html += "<td>"+str(c_derr[anio])+"</td></tr>"
                if h == 9:
                    html += "<tr><td>"+str(c_cie[anio])+"</td>"
                    html += "<td>"+str(c_cier[anio])+"</td></tr>"
                if h == 10:
                    html += "<tr><td>"+str(c_cont[anio])+"</td>"
                    html += "<td>"+str(c_contr[anio])+"</td></tr>"
                if h == 11:
                    html += "<tr><td>"+str(c_odon[anio])+"</td>"
                    html += "<td>"+str(c_odonr[anio])+"</td></tr>"
                if h == 12:
                    html += "<tr><td>"+str(c_lab[anio])+"</td>"
                    html += "<td>"+str(c_labr[anio])+"</td></tr>"
                if h == 13:
                    html += "<tr><td>"+str(c_enf[anio])+"</td>"
                    html += "<td>"+str(c_enfr[anio])+"</td></tr>"
                if h == 14:
                    html += "<tr><td>"+str(c_med[anio])+"</td>"
                    html += "<td>"+str(c_medr[anio])+"</td></tr>"
                if h == 15:
                    html += "<tr><td>"+str(c_bio[anio])+"</td>"
                    html += "<td>"+str(c_bior[anio])+"</td></tr>"
                if h == 16:
                    html += "<tr><td>"+str(c_cso[anio])+"</td>"
                    html += "<td>"+str(c_csor[anio])+"</td></tr>"
                if h == 17:
                    html += "<tr><td>"+str(c_quim[anio])+"</td>"
                    html += "<td>"+str(c_quimr[anio])+"</td></tr>"
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
        for anio in range(a1, a2 + (1)):
            vanio[anio]=0
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[4]>=fecha1 and row[4] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[4].strftime("%Y-%m-%d")))
                vanio[anoBD] +=1
        mensaje = "La cantidad de estudiantes que realizaron transferencias a otras universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)

        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            # Crear el gráfico de torta

            #crear para areas
        html += "<div class='row'style = 'border: 1px solid white;background-color:black'>"
        html += "<h6 align='center'style='color:white'>TRANSFERENCIAS POR AÑO</h6>"
        k1 = 1
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-3'>"
            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
            html += "<div class='panel-heading'>"
            html += str(anio)
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "El total de transferencias del año "+str(anio)+" es de"+str(vanio[anio])+" transferencias"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"
        html += "<br><br>"
    if accion1 == "concepto_transferencia":
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
        for anio in range(a1, a2 + (1)):
            vanio[anio]=0
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[4]>=fecha1 and row[4] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[4].strftime("%Y-%m-%d")))
                vanio[anoBD] +=1
        mensaje = "Los estudiante transferidos de otras Universidades desde el año "+str(a1)+" al año "+str(a2)+" son "+str(total)

        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        # Crear el gráfico de torta

        #crear para areas
        html += "<div class='row'style = 'border: 1px solid white;background-color:black'>"
        html += "<h6 align='center'style='color:white'>TRANSFERENCIAS POR AÑO</h6>"
        k1 = 1
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-3'>"
            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
            html += "<div class='panel-heading'>"
            html += str(anio)
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "Transferidos el "+str(anio)+" es de "+str(vanio[anio])+" Estudiantes"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"
        html += "<br><br>"
    if accion1 == "mayor_inscritos":
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

        mensaje = "La información sobre en que areas y carreras existe mas inscritos lo detallamos en los siguientes cuadros"
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


        #crear para areas
        html += "<div class='row'style = 'border: 1px solid white;background-color:black'>"
        html += "<h6 align='center'style='color:white'>Areas</h6>"
        k1 = 1
        areas ={0:"Técnologia",1:"Salud",2:"Sociales"}
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 align='center'style='color:white'>"+str(anio)+"</h6>"
            for ar in range(3):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
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
        html += "<h6 align='center'style='color:white'>Carreras</h6>"

        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 align='center'style='color:white'>"+str(anio)+"</h6>"
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
    if accion1 == "modalidad_titulacion":
        carrera_hay = ress[0]
        mensaje = ""
        if carrera_hay == "si_car":
            mensaje+="<h6>Las modalidades de titulación de la carrera o carreras son</h6>"
        else:
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
        html+="<div class='row'>"
        for i in range(17):
            html += "<div class='col-lg-4'>"
            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
            html += "<div class='panel-heading'>"
            html += nombre_carrera_retor(i+1)
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
            for row in datos:
                html+="<tr>"

                if (i+1) == row[3] and row[2] != 2 and row[3] == 1:
                    print(row[3]," esto es m ",(i+1))
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3] and row[3] == 2:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3] and row[3] == 3:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3] and row[3] == 4:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3]and row[3] == 5:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3]and row[3] == 6:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3]and row[3] == 7:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) ==row[3]and row[3] == 8:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                if (i+1) ==row[3]and row[3] == 9:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 10:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 11:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                if (i+1) == row[3]and row[3] == 12:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 13:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 14:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 15:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 16:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                elif (i+1) == row[3]and row[3] == 17:
                    html+="<td>"+str(k)+"</td>"
                    k=k+1
                    html+="<td>"+row[1]+"</td>"
                html+="</tr>"
            html+="</tbody>"
            html+= "</table>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html+="</div>"
    if accion1 == "total_estudiante_desercion":
        total = len(datos)
        fecha1 = ress[0]#obtenemos las fechas que llegan
        fecha2 = ress[1]
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
            vareas[anio]=[0,0,0]
            vareasno[anio]=[0,0,0]
        for anio in range(a1, a2 + (1)):
            carreras[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            carrerasno[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[8]>=fecha1 and row[8] <= fecha2:
                if row[2] == "si":
                    anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                    vareas[anoBD][row[7]-1]+=1#en cada año y area sumamos mas 1
                    carreras[anoBD][row[5]-1]+=1
                elif row[2] == "no":
                    anoBD = int(obtener_ano_de_fecha(row[8].strftime("%Y-%m-%d")))
                    carrerasno[anoBD][row[5]-1]+=1
                    vareasno[anoBD][row[5]-1]+=1
        mensaje = "La información sobre desercion estudiantil en areas y carreras es lo siguiente"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        #crear para areas

        html += "<h6 align='center'style='color:black'>Areas</h6>"
        k1 = 1
        html += "<div class='row'>"
        areas ={0:"Técnologia",1:"Salud",2:"Sociales"}
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
            for ar in range(3):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += areas[ar]
                html += "</div>"
                html += "<div class='panel-body'>"
                html += "La deserción estudiantil es de "+str(vareas[anio][ar])+" Estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"

        html += "</div>"
        html += "<h6 align='center'style='color:black'>Carreras</h6>"
        for i in range(17):
            k = 1
            html+="<div class='row'>"
            html += "<h6 align='center'style='color:black'>"+nombre_carrera_retor(i+1)+"</h6>"
            for anio in range(a1, a2 + (1)):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += str(anio)
                html += "</div>"
                html += "<div class='panel-body'>"
                html += "La deserción estudiantil es de "+str(carreras[anio][i])+" Estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"
            html+="</div>"
    if accion1 == "titulados_relacion":
        total = len(datos)
        fecha1 = ress[0]#obtenemos las fechas que llegan
        fecha2 = ress[1]
        consultaTitulado = ress[2]
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
            vareas[anio]=[0,0,0]
            vareasTitu[anio]=[0,0,0]
        for anio in range(a1, a2 + (1)):
            carreras[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            carrerasTitu[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[16]>=fecha1 and row[16] <= fecha2:
                if row[14] ==1:
                    anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))
                    carreras[anoBD][row[13]-1]+=1
                    vareas[anoBD][row[12]-1]+=1

        for row in titulados_re:
            if row[9]>=fecha1 and row[9] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[9].strftime("%Y-%m-%d")))
                carrerasTitu[anoBD][row[7]-1]+=1
                vareasTitu[anoBD][row[8]-1]+=1

        mensaje = "En los siguientes cuadros detallamos los titulados con relacion a los primeros niveles"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        #crear para areas

        html += "<h6 align='center'style='color:black'>Areas</h6>"
        k1 = 1
        html += "<div class='row'>"
        areas ={0:"Técnologia",1:"Salud",2:"Sociales"}
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
            for ar in range(3):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += areas[ar]
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
                html+="<td>"+str(vareas[anio][ar])+"</td>"
                html+="<td>"+str(vareasTitu[anio][ar])+"</td>"
                html+="</tr>"
                html+="</tbody>"
                html+= "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"

        html += "</div>"
        html += "<h6 align='center'style='color:black'>Carreras</h6>"
        for i in range(17):
            k = 1
            html+="<div class='row'>"
            html += "<h6 align='center'style='color:black'>"+nombre_carrera_retor(i+1)+"</h6>"
            for anio in range(a1, a2 + (1)):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += str(anio)
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
                html+="<td>"+str(carreras[anio][i])+"</td>"
                html+="<td>"+str(carrerasTitu[anio][i])+"</td>"
                html+="</tr>"
                html+="</tbody>"
                html+= "</table>"
                html += "</div>"
                html += "</div>"
                html += "</div>"
            html+="</div>"
    if accion1 == "clasificacion_departamento":
        total = len(datos)
        fecha1 = ress[0]#obtenemos las fechas que llegan
        fecha2 = ress[1]
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
        for anio in range(a1, a2 + (1)):
            occidente[anio]=[0,0,0]
        for anio in range(a1, a2 + (1)):
            depar[anio] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        for row in datos:#recorremos los datos obtenidos de la base de datos
            if row[16]>=fecha1 and row[16] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[16].strftime("%Y-%m-%d")))

                if row[7].lower().strip() == 'oruro':
                    depar[anoBD][0]+=1
                elif row[7].lower().strip() == 'potosi':
                    depar[anoBD][1]+=1
                elif row[7].lower().strip() == 'la paz':
                    depar[anoBD][2]+=1
                elif row[7].lower().strip() == 'cochabamba':
                    depar[anoBD][3]+=1
                elif row[7].lower().strip() == 'santa cruz':
                    depar[anoBD][4]+=1
                elif row[7].lower().strip() == 'beni':
                    depar[anoBD][5]+=1
                elif row[7].lower().strip() == 'tarija':
                    depar[anoBD][6]+=1
                elif row[7].lower().strip() == 'chuquisaca':
                    depar[anoBD][7]+=1
                elif row[7].lower().strip() == 'pando':
                    depar[anoBD][8]+=1

                if row[10].lower().strip() == "occidente":
                    occidente[anoBD][0]+=1
                elif row[10].lower().strip() == "central":
                    occidente[anoBD][1]+=1
                elif row[10].lower().strip() == "oriente":
                    occidente[anoBD][2]+=1

        mensaje = "Detallaremos en los siguientes cuadros sobre estudiantes a que departamento y region pertencen"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
            #crear para areas

        html += "<h6 align='center'style='color:black'>Región</h6>"
        k1 = 1
        html += "<div class='row'>"
        for anio in range(a1, a2 + (1)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<h6 align='center'style='color:black'>"+str(anio)+"</h6>"
            for ar in range(3):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += region[ar]
                html += "</div>"
                html += "<div class='panel-body'>"
                html+="Se encontro "+str(occidente[anio][ar])+" estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"

        html += "</div><br>"
        html += "<h6 align='center'style='color:black'>Departamento</h6>"
        for i in range(9):
            k = 1
            html+="<div class='row'>"
            html += "<h6 align='center'style='color:black'>"+departamento[i]+"</h6>"
            for anio in range(a1, a2 + (1)):
                html += "<div class='col-lg-4'>"
                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                html += "<div class='panel-heading'>"
                html += str(anio)
                html += "</div>"
                html += "<div class='panel-body'>"
                html+="Se encontro "+str(depar[anio][i])+" estudiantes"
                html += "</div>"
                html += "</div>"
                html += "</div>"
            html+="</div>"
    if accion1 == "plan_de_estudio":
        si_are = ress[0]
        curs ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        if si_are != "no":#si es diferente de no existe una area o areas
            areas_id = ress[1]#obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(areas_id)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
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
                            for k in range(5):
                                html += "<div class='col-lg-6'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += (curs[k])
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
                                    if (k+1) == asigg[9]:#si el curso de asignatura es igual a k entonces
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
        si_car = ress[1]#como no existe alguna area entonces buscaos carreras
        if si_car != "no":#si carrera es diferente de no entonces existe carrera
            car_id = ress[2]#obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(car_id)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+" plan de estudio</h6><br>"#impirmimos el nombre de la carrera
                asig=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                mt = modalidad_titulacion_id(index1)#seleccinamos la modalidad de titulacion
                if asig != "no":
                    html+="<div class='row'>"
                    for k in range(5):
                        html += "<div class='col-lg-6'>"
                        html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                        html += "<div class='panel-heading'>"
                        html += (curs[k])
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
                            if (k+1) == asigg[9]:#si el curso de asignatura es igual a k entonces
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
                else:
                    html+="<h6 align='center'>No se encontro resultados<h6>"

        else:#no hay ni carrera ni area pero si existe plan de estudio
            areasR = [1,2,3]
            for i in areasR:#recorremos todo los id de areas
                index = (i) - 1#obtenemos el id
                index1 = (i)
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
                            for k in range(5):
                                html += "<div class='col-lg-6'>"
                                html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                html += "<div class='panel-heading'>"
                                html += (curs[k])
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
                                    if (k+1) == asigg[9]:#si el curso de asignatura es igual a k entonces
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
        fecha1 = ress[-3]
        fecha2 = ress[-4]
        if fecha1>fecha2:
            aux = fecha1
            fecha1 = fecha2
            fecha2 = aux
        fecha11 = fecha1
        fecha22 = fecha2
        print(fecha1," ee    ",fecha2)
        vapro = [0] * 17
        vaplaz = [0] * 17
        vareasT = {}
        vareasTr = {}
        vareasS = {}
        vareasSr = {}
        vareasSo = {}
        vareasSor = {}
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
        for car in range(17):
            asig = seleccionarAsignatura((car+1),1)##enviamos el id de la carrera y el plan de estudio
            if asig != "no":
                for anio in range(a1, a2 + (1)):
                    c_infor[anio] = {}
                    c_civil[anio] = {}
                    c_minas[anio] = {}
                    c_elec[anio] = {}
                    c_mec[anio] = {}
                    c_agro[anio] = {}
                    c_lit[anio] = {}
                    c_der[anio] = {}
                    c_cie[anio] = {}
                    c_cont[anio] = {}
                    c_odon[anio] = {}
                    c_lab[anio] = {}
                    c_enf[anio] = {}
                    c_med[anio] = {}
                    c_bio[anio] = {}
                    c_cso[anio] = {}
                    c_quim[anio] = {}
                    c_inforr[anio] = {}
                    c_civilr[anio] = {}
                    c_minasr[anio] = {}
                    c_elecr[anio] = {}
                    c_mecr[anio] = {}
                    c_agror[anio] = {}
                    c_litr[anio] = {}
                    c_derr[anio] = {}
                    c_cier[anio] = {}
                    c_contr[anio] = {}
                    c_odonr[anio] = {}
                    c_labr[anio] = {}
                    c_enfr[anio] = {}
                    c_medr[anio] = {}
                    c_bior[anio] = {}
                    c_csor[anio] = {}
                    c_quimr[anio] = {}
                    for arr in asig:
                        if arr[8] == 1:#carrera 1 informatica
                        #año id de asignatura  = contar id grado id asignatura
                            c_infor[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_inforr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 2:
                            c_civil[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_civilr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 3:
                            c_minas[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_minasr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 4:
                            c_elec[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_elecr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 5:
                            c_mec[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_mecr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 6:
                            c_agro[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_agror[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 7:
                            c_lit[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_litr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 8:
                            c_der[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_derr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 9:
                            c_cie[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_cier[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 10:
                            c_cont[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_contr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 11:
                            c_odon[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_odonr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 12:
                            c_lab[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_labr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 13:
                            c_enf[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_enfr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 14:
                            c_med[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_medr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 15:
                            c_bio[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_bior[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 16:
                            c_cso[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_csor[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                        elif arr[8] == 17:
                            c_quim[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
                            c_quimr[anio][arr[0]] = [0,arr[9],arr[0],arr[10]]
        guardar = []
        guardar1 = []
        if isinstance(fecha1, str):
            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        if isinstance(fecha2, str):
            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        print(fecha1," ee121dddd    ",fecha2)
        for row in datos:#recorremos los datos obtenidos de la base de datos

            if not isinstance(row[14], type(None)) and row[14]>=fecha1 and row[14] <= fecha2:
                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))

                if row[10] == 1:
                    c_infor[anoBD][row[8]][0]+=1
                elif row[10] == 2:
                    c_civil[anoBD][row[8]][0]+=1
                elif row[10] == 3:
                    c_minas[anoBD][row[8]][0]+=1
                elif row[10] == 4:
                    c_elec[anoBD][row[8]][0]+=1
                elif row[10] == 5:
                    c_mec[anoBD][row[8]][0]+=1
                elif row[10] == 6:
                    c_agro[anoBD][row[8]][0]+=1
                elif row[10] == 7:
                    c_lit[anoBD][row[8]][0]+=1
                elif row[10] == 8:
                    c_der[anoBD][row[8]][0]+=1
                elif row[10] == 9:
                    c_cie[anoBD][row[8]][0]+=1
                elif row[10] == 10:
                    c_cont[anoBD][row[8]][0]+=1
                elif row[10] == 11:
                    c_odon[anoBD][row[8]][0]+=1
                elif row[10] == 12:
                    c_lab[anoBD][row[8]][0]+=1
                elif row[10] == 13:
                    c_enf[anoBD][row[8]][0]+=1
                elif row[10] == 14:
                    c_med[anoBD][row[8]][0]+=1
                elif row[10] == 15:
                    c_bio[anoBD][row[8]][0]+=1
                elif row[10] == 16:
                    c_cso[anoBD][row[8]][0]+=1
                elif row[10] == 17:
                    c_quim[anoBD][row[8]][0]+=1
        si_are = ress[0]
        curs ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
        if si_are != "no":#si es diferente de no existe una area o areas
            areas_id = ress[1]#obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(areas_id)#si hay doble veces repetido el id lo eliminamos a 1
            for i in s_dupli:#recorremos todo los id de areas
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(areasU[index])+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html += "<h5 align='center'>Carrera " + str(car[1])+"</h5>"
                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            html+="<div class='row'>"
                            for anio in range(a1, a2 + (1)):
                                html += "<h6 align='center'>" + str(anio)+"</h6>"

                                for g in range(5):
                                    html += "<div class='col-lg-4'>"
                                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                    html += "<div class='panel-heading'>"
                                    cur = g+1
                                    print(cur," = ",car[0])
                                    fech1 = str(anio)+"-01-01"
                                    fech2 = str(anio)+"-12-30"
                                    html += curs[g]+" tiene "+str((contar_total_estudiante_curso(cur,car[0],fech1,fech2)))+" estudiantes"
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
                                        if car[0] == 1:#si carrera es igual a 1 es informatica
                                            if (g+1) == c_infor[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_infor[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_infor[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 2:
                                            if (g+1) == c_civil[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_civil[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_civil[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 3:
                                            if (g+1) == c_minas[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_minas[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_minas[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 4:
                                            if (g+1) == c_elec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_elec[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_elec[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 5:
                                            if (g+1) == c_mec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_mec[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_mec[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 6:
                                            if (g+1) == c_agro[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_agro[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_agro[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 7:
                                            if (g+1) == c_lit[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_lit[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_lit[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 8:
                                            if (g+1) == c_der[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_der[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_der[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 9:
                                            if (g+1) == c_cie[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cie[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cie[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 10:
                                            if (g+1) == c_cont[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cont[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cont[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 11:
                                            if (g+1) == c_odon[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_odon[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_odon[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 12:
                                            if (g+1) == c_lab[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_lab[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_lab[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 13:
                                            if (g+1) == c_enf[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_enf[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_enf[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 14:
                                            if (g+1) == c_med[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_med[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_med[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 15:
                                            if (g+1) == c_bio[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_bio[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_bio[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 16:
                                            if (g+1) == c_cso[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cso[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cso[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 17:
                                            if (g+1) == c_quim[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_quim[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_quim[anio][mat[0]][0])+"</td></tr>"

                                    html+="</tbody>"
                                    html+= "</table>"
                                    html += "</div>"
                                    html += "</div>"
                                    html += "</div>"
                            html+="</div>"
                        else:
                            html+="<h6 align='center'>No se encontro información</h6>"
                else:
                    html+="<h6 align='center'>No se encontro información</h6>"
        si_car = ress[1]
        if si_car != "no":
            car_id = ress[2]#obtenemos los id de areas quue llegan
            s_dupli = eliminar_dobles(car_id)#si hay doble veces repetido el id lo eliminamos a 1
            print(s_dupli," esta bien o no ")
            for i in s_dupli:#recorremos todo los id de carreras
                index = int(i) - 1#obtenemos el id
                index1 = int(i)
                html+="<br><h6 align='center'>Carrera "+nombre_carrera_retor(index1)+"</h6><br>"#impirmimos el nombre de la carrera
                materias=seleccionarAsignatura_por_id(index1)#seleccionamos las asignaturas
                if materias != "no":
                    html+="<div class='row'>"
                    for anio in range(a1, a2 + (1)):
                        html += "<h6 align='center'>" + str(anio)+"</h6>"
                        for g in range(5):
                            html += "<div class='col-lg-4'>"
                            html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                            html += "<div class='panel-heading'>"
                            cur = g+1
                            fech1 = str(anio)+"-01-01"
                            fech2 = str(anio)+"-12-30"
                            html += curs[g]+" tiene "+str((contar_total_estudiante_curso(cur,index1,fech1,fech2)))+" estudiantes"
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
                                if index1 == 1:#si carrera es igual a 1 es informatica
                                    if (g+1) == c_infor[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_infor[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_infor[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 2:
                                    if (g+1) == c_civil[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_civil[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_civil[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 3:
                                    if (g+1) == c_minas[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_minas[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_minas[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 4:
                                    if (g+1) == c_elec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_elec[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_elec[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 5:
                                    if (g+1) == c_mec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_mec[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_mec[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 6:
                                    if (g+1) == c_agro[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_agro[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_agro[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 7:
                                    if (g+1) == c_lit[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_lit[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_lit[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 8:
                                    if (g+1) == c_der[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_der[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_der[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 9:
                                    if (g+1) == c_cie[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_cie[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_cie[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 10:
                                    if (g+1) == c_cont[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_cont[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_cont[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 11:
                                    if (g+1) == c_odon[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_odon[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_odon[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 12:
                                    if (g+1) == c_lab[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_lab[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_lab[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 13:
                                    if (g+1) == c_enf[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_enf[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_enf[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 14:
                                    if (g+1) == c_med[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_med[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_med[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 15:
                                    if (g+1) == c_bio[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_bio[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_bio[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 16:
                                    if (g+1) == c_cso[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_cso[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_cso[anio][mat[0]][0])+"</td></tr>"
                                elif index1 == 17:
                                    if (g+1) == c_quim[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                        html+="<tr><td>"+nombre_asignatura(c_quim[anio][mat[0]][2])+"</td>"
                                        html+="<td>"+str(c_quim[anio][mat[0]][0])+"</td></tr>"

                            html+="</tbody>"
                            html+= "</table>"
                            html += "</div>"
                            html += "</div>"
                            html += "</div>"
                    html+="</div>"
                else:
                    html+="<h6 align='center'>No se encontro información</h6>"
        else:#si es diferente de no existe una area o areas
            areas =[1,2,3]
            for i in areas:#recorremos todo los id de areas
                index = int(i)-1#obtenemos el id
                index1 = int(i)
                html += "<h5 align='center'>Area " + str(areasU[index])+"</h5>"
                carreras = seleccionarcarrera_id(index1)#buscamos con el id todas las carreras relacionadas con el area
                if carreras != "no":#si es diferente de no entonces ingresamos
                    for car in carreras:#recorremos todas las carreras encontradas
                        html += "<h5 align='center'>Carrera " + str(car[1])+"</h5>"
                        materias = seleccionarAsignatura_por_id(car[0])#seleccionar asiganturas carrera
                        if materias != "no":
                            html+="<div class='row'>"
                            for anio in range(a1, a2 + (1)):
                                html += "<h6 align='center'>" + str(anio)+"</h6>"

                                for g in range(5):
                                    html += "<div class='col-lg-4'>"
                                    html += "<div class='panel panel-default text-center' style = 'border: 1px solid black;background-color:khaki'>"
                                    html += "<div class='panel-heading'>"
                                    cur = g+1
                                    print(cur," = ",car[0])
                                    fech1 = str(anio)+"-01-01"
                                    fech2 = str(anio)+"-12-30"
                                    html += curs[g]+" tiene "+str((contar_total_estudiante_curso(cur,car[0],fech1,fech2)))+" estudiantes"
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
                                        if car[0] == 1:#si carrera es igual a 1 es informatica
                                            if (g+1) == c_infor[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_infor[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_infor[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 2:
                                            if (g+1) == c_civil[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_civil[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_civil[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 3:
                                            if (g+1) == c_minas[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_minas[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_minas[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 4:
                                            if (g+1) == c_elec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_elec[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_elec[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 5:
                                            if (g+1) == c_mec[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_mec[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_mec[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 6:
                                            if (g+1) == c_agro[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_agro[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_agro[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 7:
                                            if (g+1) == c_lit[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_lit[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_lit[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 8:
                                            if (g+1) == c_der[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_der[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_der[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 9:
                                            if (g+1) == c_cie[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cie[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cie[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 10:
                                            if (g+1) == c_cont[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cont[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cont[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 11:
                                            if (g+1) == c_odon[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_odon[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_odon[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 12:
                                            if (g+1) == c_lab[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_lab[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_lab[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 13:
                                            if (g+1) == c_enf[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_enf[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_enf[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 14:
                                            if (g+1) == c_med[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_med[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_med[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 15:
                                            if (g+1) == c_bio[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_bio[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_bio[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 16:
                                            if (g+1) == c_cso[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_cso[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_cso[anio][mat[0]][0])+"</td></tr>"
                                        elif car[0] == 17:
                                            if (g+1) == c_quim[anio][mat[0]][1]:#si el grado actual es igula a 1, 2 o etc ingresa
                                                html+="<tr><td>"+nombre_asignatura(c_quim[anio][mat[0]][2])+"</td>"
                                                html+="<td>"+str(c_quim[anio][mat[0]][0])+"</td></tr>"

                                    html+="</tbody>"
                                    html+= "</table>"
                                    html += "</div>"
                                    html += "</div>"
                                    html += "</div>"
                            html+="</div>"
                        else:
                            html+="<h6 align='center'>No se encontro información</h6>"
                else:
                    html+="<h6 align='center'>No se encontro información</h6>"
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
