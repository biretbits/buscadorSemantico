from flask import jsonify


def  retornar_valores(datos,accion1):
    # Retornar los resultados obtenidos de la consulta
    # Convertir los resultados a una lista de diccionarios
    #if accion >= 0 and accion  < 1:
        #datos = [{'carrera': row[0], 'to': row[1], 'indice':accion} for row in resultados]
    #if accion >= 1 and accion  < 2 or accion == 3:
        #datos = [{'carrera': row[0], 'nombre': row[1],'ap': row[2],'am': row[3],'ci': row[4],'departamento': row[6], 'indice':accion} for row in resultados]
    #if accion >= 2 and accion  < 3 or accion == 4:
        #datos = [{'carrera': row[0], 'nombre': row[1],'ap': row[2],'am': row[3],'ci': row[4],'departamento': row[6], 'indice':accion} for row in resultados]
    if accion1 == "ver_carreras":
        data = [{'carrera': row[1], 'direccion': row[2], 'indice':accion1} for row in datos]
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

    return jsonify(data)
