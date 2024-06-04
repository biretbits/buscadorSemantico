from flask import jsonify
from sql import nombre_carrera_retor,grado_Estudiante,obtener_nombre,nombre_materia,obtener_datos_de_curso
from sql import seleccionarAreas,seleccionar_carrera,seleccionarAsignaturaAreas,seleccionarAsignatura
from sql import nombre_asignatura
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
            vareasT[ar] = {}
            vareasTr[ar]={}
            varearS[ar]={}
            vareasSr[ar]={}
            vareasSo[ar]={}
            vareasSor[ar]={}
            for as in are:
                if as[10] == 1:
                    vareasT[ar][as[0]]=[0,as[10],as[0]]
                    vareasTr[ar][as[0]]=[0,as[10],as[0]]
                if as[10] == 2:
                    vareasS[ar][as[0]]=[0,as[10],as[0]]
                    vareasSr[ar][as[0]]=[0,as[10],as[0]]
                if as[10] == 3:
                    vareasSo[ar][as[0]]=[0,as[10],as[0]]
                    vareasSor[ar][as[0]]=[0,as[10],as[0]]
        for car in range(17):
            asig = seleccionarAsignatura((car+1),1)##enviamos el id de la carrera y el plan de estudio
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
                for as in asig:
                    if as[8] == 1:#carrera 1 informatica
                    #año id de asignatura  = contar id grado id asignatura
                        c_infor[anio][as[0]] = [0,as[9],as[0]]
                        c_inforr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 2:
                        c_civil[anio][as[0]] = [0,as[9],as[0]]
                        c_civilr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 3
                        c_minas[anio][as[0]] = [0,as[9],as[0]]
                        c_minasr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 4:
                        c_elec[anio][as[0]] = [0,as[9],as[0]]
                        c_elecr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 5:
                        c_mec[anio][as[0]] = [0,as[9],as[0]]
                        c_mecr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 6:
                        c_agro[anio][as[0]] = [0,as[9],as[0]]
                        c_agror[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 7:
                        c_lit[anio][as[0]] = [0,as[9],as[0]]
                        c_litr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 8:
                        c_der[anio][as[0]] = [0,as[9],as[0]]
                        c_derr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 9:
                        c_cie[anio][as[0]] = [0,as[9],as[0]]
                        c_cier[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 10:
                        c_cont[anio][as[0]] = [0,as[9],as[0]]
                        c_contr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 11:
                        c_odon[anio][as[0]] = [0,as[9],as[0]]
                        c_odonr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 12:
                        c_lab[anio][as[0]] = [0,as[9],as[0]]
                        c_labr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 13:
                        c_enf[anio][as[0]] = [0,as[9],as[0]]
                        c_enfr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 14:
                        c_med[anio][as[0]] = [0,as[9],as[0]]
                        c_medr[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 15:
                        c_bio[anio][as[0]] = [0,as[9],as[0]]
                        c_bior[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 16:
                        c_cso[anio][as[0]] = [0,as[9],as[0]]
                        c_csor[anio][as[0]] = [0,as[9],as[0]]
                    if as[8] == 17:
                        c_quim[anio][as[0]] = [0,as[9],as[0]]
                        c_quimr[anio][as[0]] = [0,as[9],as[0]]

       #carreras_a= [carreraa[0] for carreraa in ro]#aqui tengo todas las carreras pero sus id
       curso ={0:'1er año',1:"2do año",2:"3er año",3:'4to año',4:'5to año'}
       guardar = []
       guardar1 = []
       if isinstance(fecha1, str):
           fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
       if isinstance(fecha2, str):
           fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
       for row in datos:
           if row[14]>=fecha1 and row[14] <= fecha2:
               if row[3] == 'activo':#contar los de primer año
                   if as[0] == 1:
                       vareasT[row[10]][as[0]][0]+=1
                   if as[0] == 2:
                       vareasS[row[10]][as[0]][0]+=1
                   if as[0] == 3:
                       vareasSo[row[10]][as[0]][0]+=1
               elif row[3] == 'desactivo':#contar los de 5to añp
                   if as[0] == 1:
                       vareasT[row[10]][as[0]][0]+=1
                   if as[0] == 2:
                       vareasS[row[10]][as[0]][0]+=1
                   if as[0] == 3:
                       vareasSo[row[10]][as[0]][0]+=1
               anoBD = int(obtener_ano_de_fecha(row[14].strftime("%Y-%m-%d")))

               if row[3] == 'activo':#contamos solo de primer año
                   if row[10] == 1:
                       c_infor[anoBD][row[8]][0]+=1
                   if row[10] == 2:
                       c_civil[anoBD][row[8]][0]+=1
                   if row[10] == 3:
                       c_minas[anoBD][row[8]][0]+=1
                   if row[10] == 4:
                       c_elec[anoBD][row[8]][0]+=1
                   if row[10] == 5:
                       c_mec[anoBD][row[8]][0]+=1
                   if row[10] == 6:
                       c_agro[anoBD][row[8]][0]+=1
                   if row[10] == 7:
                       c_lit[anoBD][row[8]][0]+=1
                   if row[10] == 8:
                       c_der[anoBD][row[8]][0]+=1
                   if row[10] == 9:
                       c_cie[anoBD][row[8]][0]+=1
                   if row[10] == 10:
                       c_cont[anoBD][row[8]][0]+=1
                   if row[10] == 11:
                       c_odon[anoBD][row[8]][0]+=1
                   if row[10] == 12:
                       c_lab[anoBD][row[8]][0]+=1
                   if row[10] == 13:
                       c_enf[anoBD][row[8]][0]+=1
                   if row[10] == 14:
                       c_med[anoBD][row[8]][0]+=1
                   if row[10] == 15:
                       c_bio[anoBD][row[8]][0]+=1
                   if row[10] == 16:
                       c_cso[anoBD][row[8]][0]+=1
                   if row[10] == 17:
                       c_quim[anoBD][row[8]][0]+=1

               elif row[3] == 'desactivo':#contamos solo de 5to año y aprobados
                   if row[10] == 1:
                       c_inforr[anoBD][row[8]][0]+=1
                   if row[10] == 2:
                       c_civilr[anoBD][row[8]][0]+=1
                   if row[10] == 3:
                       c_minasr[anoBD][row[8]][0]+=1
                   if row[10] == 4:
                       c_elecr[anoBD][row[8]][0]+=1
                   if row[10] == 5:
                       c_mecr[anoBD][row[8]][0]+=1
                   if row[10] == 6:
                       c_agror[anoBD][row[8]][0]+=1
                   if row[10] == 7:
                       c_litr[anoBD][row[8]][0]+=1
                   if row[10] == 8:
                       c_derr[anoBD][row[8]][0]+=1
                   if row[10] == 9:
                       c_cier[anoBD][row[8]][0]+=1
                   if row[10] == 10:
                       c_contr[anoBD][row[8]][0]+=1
                   if row[10] == 11:
                       c_odonr[anoBD][row[8]][0]+=1
                   if row[10] == 12:
                       c_labr[anoBD][row[8]][0]+=1
                   if row[10] == 13:
                       c_enfr[anoBD][row[8]][0]+=1
                   if row[10] == 14:
                       c_medr[anoBD][row[8]][0]+=1
                   if row[10] == 15:
                       c_bior[anoBD][row[8]][0]+=1
                   if row[10] == 16:
                       c_csor[anoBD][row[8]][0]+=1
                   if row[10] == 17:
                       c_quimr[anoBD][row[8]][0]+=1

       mensaje = "Las asignaturas que tienen mas estudiantes desertores"
       mensaje += " por áreas y carreras, detallamos en los siguientes cuadros"
       html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
       # Crear el gráfico de torta

       #crear para areas
       html += "<div class='row bg-warning'style = 'border: 1px solid black;'>"
       html += "<h4 align='center'>Areas</h4>"
       k1 = 1
       for i in range(len(areasU)):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
           html += "<div class='col-lg-4'>"
           html += "<div class='panel panel-default text-center bg-info' style = 'border: 1px solid black;'>"
           html += "<div class='panel-heading'>"
           html += areasU[i]
           html += "</div>"
           html += "<div class='panel-body'>"
           html += "<table class='table table-striped'>"
           html += "<thead>"
           html += "<tr>"
           html += "<th>Nro</th>"
           html += "<th>Asignatura</th>"
           html += "<th>Deserciones</th>"
           html += "<th>Carrera</th>"
           html += "</tr>"
           html += "</thead>"
           html += "<tbody>"
           are = seleccionarAsignaturaAreas((i+1),1)#seleccionamos las asingturas con el cod de area
           for j in are:
               if vareasT[i][j][0] > 0:
                   html += "<tr><td>"+str(nombre_asignatura(vareasT[i][j][2]))+"</td>"
                   html += "<td>"+str((vareasT[i][j][0]))+"</td>"
                   html += "<td>"+str(nombre_carrera(vareasT[i][j][1]))+"</td></tr>"
               #html += menCOncluyeron(vareasApro[i],vareasApla[i])
           html += "<tbody>"
           html += "</table>"
           html += "</div>"
           html += "</div>"
           html += "</div>"
       html += "</div>"
       html += "<br>"
       h = 1

       for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
           asig = seleccionarAsignatura((i+1),1)#seleccionamos las asiganturas con el cod id
           html += "<div class='row'>"#abrimos una fila
           for anio in range(a1, a2 + 1):#recorremos las fechas
               html += "<h6 align='center'>Año "+str(anio)+"</h6>"
               for g in range(5):#recorremos los cursos
                   html += "<div class='col-lg-12' style = 'background-color:RGBA(0, 255, 250, 0.3);border: 1px solid black;'>"
                   html += "<div class='panel panel-default text-center'>"
                   html += "<div class='panel-heading'>"
                   html += curso[g]#imprimimos el curso
                   html += "</div>"
                   html += "<div class='panel-body'>"
                   html += "<table class='table table-striped'>"
                   html += "<thead>"
                   html += "<tr>"
                   html += "<th>Nro</th>"
                   html += "<th>Asignatura</th>"
                   html += "<th>Deserciones</th>"
                   html += "</tr>"
                   html += "</thead>"
                   html += "<tbody>"
                   for j in asig:#recorremos las asignaturas

                       if h == 1: #si carrera es igual a 1 ingresa
                            if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                                if c_infor[anio][j][0] > 0:
                                    html += "<tr><td>"+str(nombre_asignatura(c_infor[anio][j][1]))+"</td>"
                                    html += "<td>"+str((c_infor[anio][j][0]))+"</td></tr>"
                       if h == 2:
                          if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                              if c_infor[anio][j][0] > 0:
                                  html += "<tr><td>"+str(nombre_asignatura(c_civil[anio][j][1]))+"</td>"
                                  html += "<td>"+str((c_civil[anio][j][0]))+"</td></tr>"
                       if h == 3:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_minas[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_minas[anio][j][0]))+"</td></tr>"
                       if h == 4:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_elec[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_elec[anio][j][0]))+"</td></tr>"
                       if h == 5:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_mec[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_mec[anio][j][0]))+"</td></tr>"
                       if h == 6:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_agro[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_agro[anio][j][0]))+"</td></tr>"
                       if h == 7:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_lit[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_lit[anio][j][0]))+"</td></tr>"
                       if h == 8:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_der[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_der[anio][j][0]))+"</td></tr>"
                       if h == 9:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_cie[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_cie[anio][j][0]))+"</td></tr>"
                       if h == 10:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_cont[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_cont[anio][j][0]))+"</td></tr>"
                       if h == 11:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_odon[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_odon[anio][j][0]))+"</td></tr>"
                       if h == 12:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_lab[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_lab[anio][j][0]))+"</td></tr>"
                       if h == 13:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_enf[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_enf[anio][j][0]))+"</td></tr>"
                       if h == 14:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_med[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_med[anio][j][0]))+"</td></tr>"
                       if h == 15:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_bio[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_bio[anio][j][0]))+"</td></tr>"
                       if h == 16:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_cso[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_cso[anio][j][0]))+"</td></tr>"
                       if h == 17:
                           if (g+1) == c_infor[anio][j][1]:#si el curso es igual a primero
                               if c_infor[anio][j][0] > 0:
                                   html += "<tr><td>"+str(nombre_asignatura(c_quim[anio][j][1]))+"</td>"
                                   html += "<td>"+str((c_quim[anio][j][0]))+"</td></tr>"
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
