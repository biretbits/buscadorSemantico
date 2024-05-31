from flask import jsonify
from sql import nombre_carrera_retor,grado_Estudiante,obtener_nombre,nombre_materia,obtener_datos_de_curso
from sql import seleccionarAreas
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
areasU = {
0:'Tecnologia',1:"Salud",2:"Sociales"
}
def  retornar_valores(datos,ress):
    accion1 = ress[-2]
    print("la accion es : ",accion1)
    print(ress,"   trae los siguientes datos ")
    html = ""
    html += "<div class='container'>"
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
        si_des = ress[0]
        si_apla = ress[1]
        si_apro = ress[2]
        vapro = [0] * 17
        vaplaz = [0] * 17
        vdes = [0] * 17
        vndes = [0] * 17
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
        for row in datos:
            #comtamos datos
            if row[2] == "si":
                cdes += 1
                vdes[row[5]-1] += 1

            elif row[2] == "no":
                cndes += 1
                vndes[row[5]-1] += 1

            if row[1] == "aprobado":
                capro += 1
                vapro[row[5]-1] += 1
                vareasApro[row[7]-1] += 1
            elif row[1] == "reprobado":
                caplaz += 1
                vaplaz[row[5]-1] += 1
                vareasApla[row[7]-1] += 1

        mensaje = "La cantidad de "
        si = "no"
        if si_des != "no" and si == "no":
            mensaje += " desertores "
            si = "si"
        if si_apla != "no" and si == "no":
            mensaje += " reprobados "
            si = "si"
        elif si_apla != "no" and si == "si":
            mensaje += ", reprobados "
            si = "si"
        if si_apro != "no" and si == "no":
            mensaje += " aprobados "
            si = "si"
        elif si_apro != "no" and si == "si":
            mensaje += ", aprobados "
            si = "si"
        mensaje += " es lo siguiente por área y carreras"
        html += "<div class='alert alert-secondary' role='alert'>" + mensaje + "</div>"
        # Crear el gráfico de torta
        html += "<div class='row'>"
        html += "<h2>Total</h2>"
        html += "<center><canvas id='grafica' width='250' height='250'></canvas></center>"
        html += "</div>"
        #crear para areas
        html += "<div class='row'>"
        html += "<h2>Areas</h2>"
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

        html += "<div class='row'>"
        html += "<h2>Carreras</h2>"
        for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
            html += "<div class='col-lg-3'>"
            html += "<div class='panel panel-default text-center'>"
            html += "<div class='panel-heading'>"
            html += ac[i]
            html += "</div>"
            html += "<div class='panel-body'>"
            html += "<center><canvas id='grafica"+str(i)+"' width='250' height='250'></canvas></center>"
            html += "</div>"
            html += "</div>"
            html += "</div>"
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
        j = 0
        for i in range(17):#creamos un grafico para cada canvas
            html += "<script>"
            html += "var data = {"
            html += "'labels': ['Aprobado', 'Reprobado'],"
            html += "'datasets': [{"

            html += "'data': [" + str(vapro[i]) + ", " + str(vaplaz[i]) + "], "  # Valores para cada sección de la torta
            html += "'backgroundColor': ['#FF6384', '#36A2EB'] "  # Colores para cada sección
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

        html += "</container>"
    return html



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
