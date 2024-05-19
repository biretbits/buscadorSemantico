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

    return jsonify(data)
