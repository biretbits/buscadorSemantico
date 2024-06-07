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
def  retornar_valores(datos,ress):
    accion1 = ress[-2]
    print("la accion es : ",accion1)
    print(ress,"   trae los siguientes datos ")
    html = ""
    html += "<div class='container justify-content-center align-items-center' style='min-height: 100vh;'>"
    if accion1 == "ver_carreras":
        if ress[0] != 'no':
            html += "Las carreras de la universidad son las siguientes: "
            html += "<h2>Tabla de carreras de la UNSXX</h2>"
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
            k = 1
            for row in datos:
                if row[1] == "":
                    html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas."
                else:
                    html += "<tr>"
                    html += "<td>" + str(k) + "</td>"
                    html += "<td>" + row[1] + "</td>"
                    html += "<td>" + row[2] + "</td>"
                    html += "</tr>"
                    contar += 1
                    k = k + 1
            html += "</tbody>"
            html += "</table>"
            html += "Se tiene " + str(contar) + " carreras activas"
        elif ress[3] != 'no':
            for row in datos:
                html += "La carrera de " + row[1] + " se encuentra en " + row[2]

    if accion1 == "ver_carreras_nombre":
        for row in datos:
            if row[1] == "":
                html += "Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas."
            else:
                html += "La carrera de " + row[1] + " se encuentra en la dirección " + row[2] + " "

    if accion1 == "total_de_estudiantes":
        for row in datos:
            html += "La universidad tiene un total de " + str(row[0]) + " Estudiantes"

    if accion1 == "total_de_estudiantes_carrera":
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

    if accion1 == "estudiantes_de_unsxx":
        total = len(datos)
        me = ""
        if me == "argumentar_poco_mas":
            html += "<div class='alert alert-secondary' role='alert'>Le pido que argumente un poco mas</div>"
        else:
            si_activo = ress[0]
            si_desactivo = ress[1]
            si_m = ress[2]
            si_f = ress[3]
            si_dep = ress[5]
            si_prov = ress[4]
            si_nom = "no"
            si_apell = "no"
            k = 0
            for row in datos:
                dep = row[7]
                provi = row[8]
                nom = row[1]
                ap = row[2]
                am = row[3]
                k = k +1
                if k == 1:
                    break

            si = "no"
            mensaje = "Los estudiantes"
            retu = verificarUNSXX(si_activo, si_desactivo, si_m, si_f, si_dep, si_prov, si_nom, si_apell, dep, provi, nom, ap, am, si)

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
            html += "</tr>"
            html += "</thead>"
            html += "<tbody>"
            contar = 0
            k = 1
            for row in datos:
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
                html += "</tr>"
                contar += 1
                k = k + 1
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
        # Crear el gráfico de torta
        html += "<div class='row'>"
        html += "<h2>Total</h2>"
        html += "<center><canvas id='grafica' width='250' height='250'></canvas></center>"
        html += "</div>"
        #crear para areas
        html += "<div class='row'>"
        html += "<h4 align='center'>Areas</h4>"
        print("areas son ",len(areasU), areasU[1])
        for i in range(len(areasU)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-3'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"
            html += areasU[i]
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><canvas id='graficaa"+str(i)+"' width='250' height='250'></canvas></center>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
        html += "</div>"


        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='row'>"
            html += "<h4 align = 'center'>Carrera</h4>"
            html += "<h5 align = 'center'>"+ac[i]+"</h5>"
            html += "<div class='col-lg-3'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"

            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><canvas id='grafica"+str(i)+"' width='250' height='250'></canvas></center>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
            html += "<div class='row'>"
            k = 0
            for anio in range(a1, a2 + 1):#recorremos las fechas
                html += "<h5 align='center'>Año "+str(anio)+"</h5>"
                for j in range(5):#recorremos todos los cursos aprobados por año

                    html += "<div class='col-lg-3'>"
                    html += "<div class='panel panel-default text-center'>"
                    html += "<div class='panel-heading'>"
                    html += curso[j]
                    html += "</div>"
                    html += "<div class='panel-body'>"
                    html += "<center><canvas id='graficaCurso"+str(i)+str(k)+str(j)+"' width='250' height='250'></canvas></center>"
                    html += "</div>"
                    html += "</div>"
                    html += "</div>"
                k = k + 1
            html += "</div>"

        # Datos para el gráfico
        html += "<script>"
        html += "var data = {"
        html += "'labels': ['Aprobado', 'Reprobado'],"
        html += "'datasets': [{"
        html += "'data': [" + str(capro) + ", " + str(caplaz) + "], "  # Valores para cada sección de la torta
        html += "'backgroundColor': ['#FF6384', '#36A2EB'] "  # Colores para cada sección
        html += "}]"
        html += "};"
        html += "var options = {"
        html += "'responsive': true,"
        html += "'maintainAspectRatio': false"
        html += "};"
        html+="var ctx = document.getElementById('grafica').getContext('2d');"
        html+="var myPieChart = new Chart(ctx, {"
        html+=" type: 'pie',"
        html+=" data: data,"
        html+=" options: options"
        html+="});"
        html += "</script>"
        h = 1
        for i in range(17):#creamos un grafico para cada canvas
            html += "<script>"
            html += "var data = {"
            html += "'labels': ['Aprobado', 'Reprobado'],"
            html += "'datasets': [{"

            html += "'data': [" + str(vapro[i]) + ", " + str(vaplaz[i]) + "], "  # Valores para cada sección de la torta
            html += "'backgroundColor': ['lime', 'orange'] "  # Colores para cada sección
            html += "}]"
            html += "};"
            html += "var options = {"
            html += "'responsive': true,"
            html += "'maintainAspectRatio': false"
            html += "};"

            html+="var ctx = document.getElementById('grafica"+str(i)+"').getContext('2d');"
            html+="var myPieChart = new Chart(ctx, {"
            html+=" type: 'pie',"
            html+=" data: data,"
            html+=" options: options"
            html+="});"
            html += "</script>"
            k = 0
            html += "<script>"
            for anio in range(a11, a22 + 1):#recorremos las fechas

                for j in range(5):#recorremos todos los cursos aprobados por año
                    html += "var data = {"
                    html += "'labels': ['Aprobado', 'Reprobado'],"
                    html += "'datasets': [{"

                    if h == 1:
                        html += "'data': [" + str(c_infor[anio][j]) + ", " + str(c_inforr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 2:
                        html += "'data': [" + str(c_civil[anio][j]) + ", " + str(c_civilr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 3:
                        html += "'data': [" + str(c_minas[anio][j]) + ", " + str(c_minasr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 4:
                        html += "'data': [" + str(c_elec[anio][j]) + ", " + str(c_elecr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 5:
                        html += "'data': [" + str(c_mec[anio][j]) + ", " + str(c_mecr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 6:
                        html += "'data': [" + str(c_agro[anio][j]) + ", " + str(c_agror[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 7:
                        html += "'data': [" + str(c_lit[anio][j]) + ", " + str(c_litr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 8:
                        html += "'data': [" + str(c_der[anio][j]) + ", " + str(c_derr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 9:
                        html += "'data': [" + str(c_cie[anio][j]) + ", " + str(c_cier[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 10:
                        html += "'data': [" + str(c_cont[anio][j]) + ", " + str(c_contr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 11:
                        html += "'data': [" + str(c_odon[anio][j]) + ", " + str(c_odonr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 12:
                        html += "'data': [" + str(c_lab[anio][j]) + ", " + str(c_labr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 13:
                        html += "'data': [" + str(c_enf[anio][j]) + ", " + str(c_enfr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 14:
                        html += "'data': [" + str(c_med[anio][j]) + ", " + str(c_medr[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 15:
                        html += "'data': [" + str(c_bio[anio][j]) + ", " + str(c_bior[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 16:
                        html += "'data': [" + str(c_cso[anio][j]) + ", " + str(c_csor[anio][j]) + "], "  # Valores para cada sección de la torta
                    if h == 17:
                        html += "'data': [" + str(c_quim[anio][j]) + ", " + str(c_quimr[anio][j]) + "], "  # es de la carrera de bioquimica

                    html += "'backgroundColor': ['blue', 'red'] "  # Colores para cada sección
                    html += "}]"
                    html += "};"
                    html += "var options = {"
                    html += "'responsive': true,"
                    html += "'maintainAspectRatio': false"
                    html += "};"

                    html+="var ctx = document.getElementById('graficaCurso"+str(i)+str(k)+str(j)+"').getContext('2d');"
                    html+="var myPieChart = new Chart(ctx, {"
                    html+=" type: 'pie',"
                    html+=" data: data,"
                    html+=" options: options"
                    html+="});"
                k = k + 1
            h = h + 1
            html += "</script>"
        #para las areass
        for i in range(len(areasU)):#creamos un grafico para cada canvas
            html += "<script>"
            html += "var data = {"
            html += "'labels': ['Aprobado', 'Reprobado'],"
            html += "'datasets': [{"

            html += "'data': [" + str(vareasApro[i]) + ", " + str(vareasApla[i]) + "], "  # Valores para cada sección de la torta
            html += "'backgroundColor': ['#FF6384', '#36A2EB'] "  # Colores para cada sección
            html += "}]"
            html += "};"
            html += "var options = {"
            html += "'responsive': true,"
            html += "'maintainAspectRatio': false"
            html += "};"

            html+="var ctx = document.getElementById('graficaa"+str(i)+"').getContext('2d');"
            html+="var myPieChart = new Chart(ctx, {"
            html+=" type: 'pie',"
            html+=" data: data,"
            html+=" options: options"
            html+="});"
            html += "</script>"
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
                if row[3] == 'desactivo':#contar los de primer año
                    if row[12] == 1:
                        vareasT[row[12]][row[8]][0]+=1
                    elif row[12] == 2:
                        vareasS[row[12]][row[8]][0]+=1
                    elif row[12] == 3:
                        vareasSo[row[12]][row[8]][0]+=1
                elif row[3] == 'activo':#contar los de 5to añp
                    if row[12] == 1:
                        vareasTr[row[12]][row[8]][0]+=1
                    elif row[12] == 2:
                        vareasSr[row[12]][row[8]][0]+=1
                    elif row[12] == 3:
                        vareasSor[row[12]][row[8]][0]+=1

                anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))

                if row[3] == 'desactivo':#contamos solo de primer año
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

                elif row[3] == 'activo':#contamos solo de 5to año y aprobados
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
            print(are," no se que me retornara")
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
            if row[15]>=fecha1 and row[15] <= fecha2:
                if row[11] == 'masculino':#contar los de primer año
                    vareas[row[12]]+=1
                elif row[11] == 'femenino':#contar los de 5to añp
                    vareasr[row[12]]+=1

                anoBD = int(obtener_ano_de_fecha(row[15].strftime("%Y-%m-%d")))

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
        mensaje += "detallamos en los siguientes cuadros por area y carreras"
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


    html += "</container>"

    return html

def menCOncluyeron(a,b):
    if a == b:
        return "<h6>la relación es pareja</h6>"
    elif a > b:
        return "<h6>hay menos estudiantes que concluyen sus estudios con relación a 1er año</h6>"
    elif a < b:
        return "<h6>existe mas estudiantes que concluyen sus estudios con relación a 1er año</h6>"




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
