import pymysql

def seleccionar_estudiante(id):

    # Consulta SQL para seleccionar un estudiante por su ID
    sql_consulta = "SELECT * FROM estudiante WHERE cod_es = %s"
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta SQL con el ID proporcionado como parámetro
    cursor.execute(sql_consulta, (id))
    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener los datos de la consulta
        estudiante = cursor.fetchone()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        # Si se encuentra el estudiante, obtener sus datos
        nombres = estudiante[1] + "|" + estudiante[2] + "|" + estudiante[3]
        return nombres
    else:
        # Si no hay resultados, devolver un mensaje indicando que no se encontró el estudiante
        return "Lo siento, no se encontró un estudiante con el ID proporcionado."


# Ejemplo de uso
id_estudiante = 5
nombres_estudiante = seleccionar_estudiante(id_estudiante)
print(nombres_estudiante)








    vec = []
    vec1 = []
    response = ""
    carreras_encontradas = obtener_carreras_nombre(texto);
    if carreras_encontradas:#si existe algun nombre de carrera ingresa
        vec.append("si_car")
        nombre_posicion_sql = "total_de_estudiantes_carrera"
        sql = consultas_sql[nombre_posicion_sql]
        print(carreras_encontradas,"  estas son las carreras",texto)
        if  contiene_palabras_activas(texto) != "no":#si contiene la palabra activo ingresa
            vec.append("si_activo")
        else:
            vec.append("no")

        if contiene_palabras_desactivas(texto) != "no":#si contiene la palabra desactivo o al relacionado ingresa
            vec.append("si_desactivo")
        else:
            vec.append("no")

        if contiene_palabras_sexo_varon(texto) != "no":#si contiene la palabra sexo
            vec.append("si_m")
        else:
            vec.append("no")
        if contiene_palabras_sexo_mujer(texto) != "no":#si contiene femenino ingresa
            vec.append("si_f")
        else:
            vec.append("no")

        dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
        if dep_encontrado != "no":
            vec.append("si_dep")
        else:
            vec.append("no")

        pr_encontrado = palabras_provincia(texto)#si contiene algun departamento ingresa
        if pr_encontrado != "no":
            vec.append("si_prov")
        else:
            vec.append("no")
        nomb = encontrar_nombre(texto)#si existe algun nombre ingresa
        if nomb != "no":
            vec.append("si_nom")
        else:
            vec.append("no")
        ap = encontrar_apellido(texto)#si hay algun apellido ingresa
        if ap != "no":
            vec.append("si_apell")
        else:
            vec.append("no")
        desercion = palabra_desercion(texto)#buscamos palabras relacionados con desercion o relacionado
        if desercion != "no":
            vec.append("si_des")
        else:
            vec.append("no")
        aplazar = palabra_aplazaron(texto)#buscamos palabras relacionados con aplazar
        print(aplazar,"  aplazadoss")
        if aplazar != "no":
            vec.append("si_apla")
            aplazar = "reprobado"
        else:
            vec.append("no")

        aprobado = palabra_aprobados(texto)
        if aprobado != "no":
            vec.append("si_apro")
            aprobado = "aprobado"
        else:
            vec.append("no")

        curso = palabra_curso(texto)
        print(curso,"    curso son ")
        id_curso = "no";


        if curso != "no":
            id_curso=obtener_que_curso_quiere(texto)
            if id_curso != "no":
                vec.append("si_curso")
            else:
                vec.append("no")
        else:
            vec.append("no")

        si = "no"
        for i in range(len(vec)):
            vec1.append(vec[i])
        vec1.append(nombre_posicion_sql)
        print(carreras_encontradas)
        print(vec)
        nombres = 'no'
        apellidos = 'no'
        for i in range(len(vec)):

            if vec[i] == "si_car" and si == "no":
                auxi = consultas_aux["nombre_carrera"]
                primera_carrera = carreras_encontradas.pop(0)
                print(primera_carrera)
                response += auxi.format(primera_carrera)
                si = "si"
            elif vec[i] == "si_car" and si == "si":
                auxi = consultas_aux["nombre_carrera"]
                primera_carrera = carreras_encontradas.pop(0)
                response += " and "+auxi.format(primera_carrera)
                si = "si"
            if vec[i] == "si_activo" and si == "no":
                response += consultas_aux["activo_es"]
                si = "si"
            elif vec[i] == "si_activo" and si == "si":
                response += " and "+consultas_aux["activo_es"]
                si = "si"

            if vec[i] == "si_desactivo" and si == "no":
                response += consultas_aux["desactivo_es"]
                si = "si"
            elif vec[i] == "si_desactivo" and si == "si":
                response += " and "+consultas_aux["desactivo_es"]
                si = "si"

            if vec[i] == "si_m" and si == "no":
                response += consultas_aux["sexo_es_m"]
                si = "si"
            elif vec[i] == "si_m" and si == "si":
                response += " and "+consultas_aux["sexo_es_m"]
                si = "si"

            if vec[i] == "si_f" and si == "no":
                response += consultas_aux["sexo_es_f"]
                si = "si"
            elif vec[i] == "si_f" and si == "si":
                response += " and "+consultas_aux["sexo_es_f"]
                si = "si"

            if vec[i] == "si_prov" and si == "no":
                sql_aux = consultas_aux["provincia_es"]
                si = "si"
                response += sql_aux.format(pr_encontrado)
            elif vec[i] == "si_prov" and si == "si":
                sql_aux = " and "+consultas_aux["provincia_es"]
                si = "si"
                response += sql_aux.format(pr_encontrado)
            if vec[i] == "si_dep" and si == "no":
                sql_aux = consultas_aux["departamento_es"]
                si = "si"
                response += sql_aux.format(dep_encontrado)
            elif vec[i] == "si_dep" and si == "si":
                sql_aux = " and "+consultas_aux["departamento_es"]
                si = "si"
                response += sql_aux.format(dep_encontrado)

            if vec[i] == "si_nom" and si == "no":
                sql_aux = "("+consultas_aux["nombre_es"]
                response += sql_aux.format(nomb)
                si = "si"
                nombres = "si"
            elif vec[i] == "si_nom" and si == "si":
                sql_aux = consultas_aux["nombre_es"]
                response += " and ("+sql_aux.format(nomb)
                si = "si"
                nombres = "si"
                #apellidos

            if vec[i] == "si_apell" and si == "no":
                if len(ap) == 1:#numero de apellidos maryor a 1
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += sql_aux.format(ap[0])
                elif len(ap)>1:
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += sql_aux.format(ap[0])
                    sql_aux = consultas_aux["apellido_m_es"]
                    response += sql_aux.format(ap[1])
                si = "si"
                if nombres == "si":
                    response+=") "
                    apellidos = 'si'
            elif vec[i] == "si_apell" and si == "si":
                if len(ap) == 1:#numero de apellidos maryor a 1
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += " and "+sql_aux.format(ap[0])
                elif len(ap)>1:
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += " and "+sql_aux.format(ap[0])
                    sql_aux = consultas_aux["apellido_m_es"]
                    response += " and "+sql_aux.format(ap[1])
                si = "si"
                if nombres == "si":
                    response+=") "
                    apellidos = 'si'
            if apellidos == "no" and vec[i] == "si_apell" and si == "si":#no existe apellidos entonces cerramos en nombre el parentesis
                response+=") "

            if vec[i] == "si_des" and si == "no":
                sql_aux = consultas_aux["desercion"]
                si = "si"
                response+= sql_aux.format(desercion)
            elif vec[i] == "si_des" and si=="si":
                sql_aux = " and "+consultas_aux["desercion"]
                si = "si"
                response+= sql_aux.format(desercion)
            if vec[i] == "si_apro" and  si == "no":
                sql_aux = consultas_aux["aplazaron"]
                si = "si"
                response+= sql_aux.format(aprobado)
            elif vec[i] == "si_apro" and si=="si":
                sql_aux = " and "+consultas_aux["aplazaron"]
                si = "si"
                response+= sql_aux.format(aprobado)

            if vec[i] == "si_apla" and  si == "no":
                sql_aux = consultas_aux["aplazaron"]
                si = "si"
                response+= sql_aux.format(aplazar)
            elif vec[i] == "si_apla" and si=="si":
                sql_aux = " and "+consultas_aux["aplazaron"]
                si = "si"
                response+= sql_aux.format(aplazar)

            if vec[i] == "si_curso" and si == "no":
                sql_aux = consultas_aux["curso_estudiante"]
                si = "si"
                response+= sql_aux.format(id_curso.pop(0))
            elif vec[i] == "si_curso" and si == "si":
                sql_aux = consultas_aux["curso_estudiante"]
                si = "si"
                response+= " and "+sql_aux.format(id_curso.pop(0))
            #print(vec[i])
            vec[i] = "no"
        if si == "no":#si se mantienen en no entonces aumentamos WHERE
            response = response
        else:
            response=" where "+response

        response = sql+" "+response;
    else:
        response = "argumentar_poco_mas"
    vec1.append(response)
