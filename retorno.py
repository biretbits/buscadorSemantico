from flask import jsonify


def  retornar_valores(datos,ress):
    accion1 = ress[-2]
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
            # Crear la lista de diccionarios a partir de 'datos'
            data = [{'nombre': row[0], 'ap': row[1], 'am': row[2], 'ci': row[3], 'pais': row[4],
                     'dep': row[5], 'provi': row[6], 'ciudad': row[7], 'regi': row[8], 'sexo': row[9],'car': row[10]} for row in datos]

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


    return jsonify(data)
