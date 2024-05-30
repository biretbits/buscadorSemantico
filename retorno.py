from flask import jsonify
from sql import nombre_carrera,grado_Estudiante,obtener_nombre,nombre_materia

def  retornar_valores(datos,ress):
    accion1 = ress[-2]
    html = ""
    html += "<div class='container'>"
    if accion1 == "ver_carreras":
        # Crear una lista de diccionarios a partir de datos
        data = [{'carrera': row[1], 'direccion': row[2]} for row in datos]
        # Crear una lista de diccionarios a partir de ress
        data += [{'si_car_n': fila[3], 'si_car': fila[4],'indice':accion1} for fila in ress[:len(ress)-2]]
    if accion1 == "ver_carreras_nombre":
        data = [{'carrera': row[1], 'direccion': row[2], 'indice':accion1} for row in datos]
    if accion1 == "total_de_estudiantes":
        data = [{'total': row[0], 'indice':accion1} for row in datos]

    if accion1 == "total_de_estudiantes_carrera":
        if datos == "argumentar_poco_mas":
            data = [{'msg': "argumentar_poco_mas","indice":accion1}]
        else:
            # Obtener el número de filas
            numero_de_filas = len(datos)
            print(datos[0][13],"    es el id de una de las carreras lo que me llega")
            # Crear la lista de diccionarios a partir de 'datos'
            nom_car = nombre_carrera(datos[0][13]);
            data = [{'nombre': row[1], 'ap': row[2], 'am': row[3], 'ci': row[5], 'pais': row[6],
                     'dep': row[7], 'provi': row[8], 'ciudad': row[9], 'regi': row[10],
                      'sexo': row[11],'carrera_nom':nombre_carrera(row[13]),'estado_ano':row[16],
                      'abandono':row[17],'grado':grado_Estudiante(row[18])} for row in datos]
            # Crear un diccionario con los nuevos datos
            nuevos_datos = {
                'si_car_n': ress[0],
                'si_activo': ress[1],
                'si_desactivo': ress[2],
                'si_m': ress[3],
                'si_f': ress[4],
                'si_dep': ress[5],
                'si_prov': ress[6],
                'si_nom': ress[7],
                'si_apell': ress[8],
                'si_des': ress[9],
                'si_apla': ress[10],
                'si_apro': ress[11],
                'si_curso':ress[12],
                'car':nom_car,
                'total': numero_de_filas,
                'indice': accion1
            }




            # Agregar los nuevos datos a la lista de diccionarios
            data.append(nuevos_datos)

            # Convertir la lista de diccionarios a JSON y devolverlo usando jsonify

    if accion1 == "datos_especificos_estudiante":
        numero_de_filas = len(datos)
    # Crear la lista de diccionarios a partir de 'datos'
        data = [{'nombre': row[0], 'ap': row[1], 'am': row[2], 'ci': row[3], 'pais': row[4],
                     'dep': row[5], 'provi': row[6], 'ciudad': row[7], 'regi': row[8], 'sexo': row[9],'car': row[10]} for row in datos]
                # Crear un diccionario con los nuevos datos
        nuevos_datos = {
                    'si_car_n': ress[0],
                    'si_nom': ress[1],
                    'si_apell': ress[2],
                    'msg': "",
                    'total': numero_de_filas,
                    'indice': accion1
                }

                # Agregar los nuevos datos a la lista de diccionarios
        data.append(nuevos_datos)
    if accion1 == "estudiantes_de_unsxx":
        numero_de_filas = len(datos)

        # Crear la lista de diccionarios a partir de 'datos'
        data = [{'nombre': row[1], 'ap': row[2], 'am': row[3], 'ci': row[5], 'pais': row[6],
                 'dep': row[7], 'provi': row[8], 'ciudad': row[9], 'regi': row[10], 'sexo': row[11]} for row in datos]

        # Crear un diccionario con los nuevos datos
        nuevos_datos = {
            'si_activo': ress[0],
            'si_desactivo': ress[1],
            'si_m': ress[2],
            'si_f': ress[3],
            'si_prov': ress[4],
            'si_dep': ress[5],
            'msg': "",
            'total': numero_de_filas,
            'indice': accion1
        }
        data.append(nuevos_datos)

    if accion1 == "seleccionar_carreras_area":
        data = [{'area': row[1], 'direccion_area': row[2], 'telefono_area': row[3], 'nombre_carrera': row[5],
              'direccion_carrera': row[6]} for row in datos]
        nuevos_datos = {
        'si_ar':ress[0],
        'c_area':ress[1],
        'indice':accion1
        }
        data.append(nuevos_datos)

        # Agregar los nuevos datos a la lista de diccionarios

    if accion1 == "estudiante_por_area":
        numero_de_filas = len(datos)

        data =[{'cod_es': row[0],'nombre_es': row[1],'ap_es': row[2],'am_es': row[3],
        'titulo_bachiller': row[4],'ci': row[5],'pais_es': row[6],
        'departamento': row[7],'provincia': row[8],'ciudad': row[9],'region': row[10],
        'sexo': row[11],'cod_area': row[12],
        'cod_carrera': row[13],'estado_ano': row[16],'abandono': row[17]}for row in datos]
        nuevos_datos ={
        "si_activo":ress[0],
        "si_desactivo":ress[1],
        "si_m":ress[2],
        "si_f":ress[3],
        "si_prov":ress[4],
        "si_dep":ress[5],
        "si_des":ress[6],
        "si_apla":ress[7],
        "si_apro":ress[8],
        "si_ar":ress[9],
        'c_area':ress[10],
        'total': numero_de_filas,
        'indice':accion1
        }

        data.append(nuevos_datos)

    if accion1 == "seleccionar_asignatura_estudiante":

        data = [{'cod_cursa': row[0],'ano': row[1],'calificacion':row[2],'nombre_es':obtener_nombre(row[5]),
        'cod_docente':row[7],'nombre_asignatura':nombre_materia(row[8]),'nombre_carrera':nombre_carrera(row[10]),
        'grado':grado_Estudiante(row[11])} for row in datos]
        nuevos_datos = {
            "nombre": ress[0],
            "apellid_p": ress[1],
            "si_cali": ress[2],
            "si_car": ress[3],
            "si_nom_apell": ress[4],
            "si_curso": ress[5],
            'indice':accion1
        }
        data.append(nuevos_datos)
    if accion1 == "total_de_estudiantes_estadisticas":


        si_des = ress[0]
        si_apla = ress[1]
        si_apro = ress[2]
        vapro = [0] * 18
        vaplaz = [0] * 18
        vdes = [0] * 18
        vndes = [0] * 18
        capro = 0
        caplaz = 0
        cdes = 0
        cndes = 0
        total = 0
        for row in datos:
            print(row[1])
            if row[2] == "si":
                cdes += 1
                vdes[row[4]] += 1
            elif row[2] == "no":
                cndes += 1
                vndes[row[4]] += 1

            if row[1] == "aprobado":
                capro += 1
                vapro[row[4]] += 1
            elif row[1] == "reprobado":
                caplaz += 1
                vaplaz[row[4]] += 1

            total += 1

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
            html += "<center><canvas id='grafica1' width='250' height='250'></canvas></center>"

            # Datos para el gráfico
            html += "<script>"
            html += "var data = {"
            html += "'labels': ['Aprobado', 'Reprobado'],"
            html += "'datasets': [{"
            html += "'data': [" + str(30) + ", " + str(50) + "], "  # Valores para cada sección de la torta
            html += "'backgroundColor': ['#FF6384', '#36A2EB'] "  # Colores para cada sección
            html += "}]"
            html += "};"

            html += "var options = {"
            html += "'responsive': true,"
            html += "'maintainAspectRatio': false"
            html += "};"

            html+="var ctx = document.getElementById('grafica1').getContext('2d');"

            html+="var myPieChart = new Chart(ctx, {"
            html+=" type: 'pie',"
            html+=" data: data,"
            html+=" options: options"
            html+="});"
            html += "</script>"


        html += "</container>"
    return html

    ac = {
1: "Ingenieria Informatica",
2: "Ingenieria civil",
3: "Ingenieria de minas",
4: "Ingenieria electromecanica",
5: "Ingenieria mecanica automotriz",
6: "Ingenieria agronomia",
7: "Ingenieria evaporiticos del litio",
8: "Derecho",
9: "Ciencias de la Educacion",
10: "contaduria",
11: "Odontologia",
12: "Laboratorio Clinico",
13: "Enfermeria",
14: "Medicina",
15: "Ingenieria bio medica",
16: "comunicacion social",
17: "bioquimica"
}
