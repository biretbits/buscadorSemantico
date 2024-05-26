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
            numero_de_filas = len(datos)
            data = [{'nombre': row[0],'ap': row[1],'am': row[2],'ci': row[3],'pais': row[4],'dep': row[5],'provi': row[6],'ciudad': row[7],'regi': row[8],'sexo': row[9],'carrera': row[10],'total':numero_de_filas,'msg': "","indice":accion1} for row in datos]
    if accion1 == "ver_por_nombre_estudiante":
        numero_de_filas = len(datos)
        data = [{'nombre': row[0],'ap': row[1],'am': row[2],'ci': row[3],'pais': row[4],'dep': row[5],'provi': row[6],'ciudad': row[7],'regi': row[8],'sexo': row[9],'carrera': row[10],'total':numero_de_filas,'msg': "","indice":accion1} for row in datos]
    if accion1 == "datos_especificos_estudiante":
        numero_de_filas = len(datos)
        data = [{'nombre': row[0],'ap': row[1],'am': row[2],'ci': row[3],'pais': row[4],'dep': row[5],'provi': row[6],'ciudad': row[7],'regi': row[8],'sexo': row[9],'carrera': row[10],'total':numero_de_filas,'msg': "","indice":accion1} for row in datos]
    if accion1 == "estudiantes_de_unsxx":
        numero_de_filas = len(datos)
        data = [{'nombre': row[0],'ap': row[1],'am': row[2],'ci': row[3],'pais': row[4],'dep': row[5],'provi': row[6],'ciudad': row[7],'regi': row[8],'sexo': row[9], 'total':numero_de_filas,'msg': "","indice":accion1} for row in datos]

    return jsonify(data)
