

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido,obtener_area,palabra_desercion
from comprobar import palabra_aplazaron,palabra_aprobados,palabra_curso,obtener_que_curso_quiere
from comprobar import palabra_nota,fechas
from sql import seleccionar_estudiante
import numpy as np
from dotenv import dotenv_values
from sentence_transformers import SentenceTransformer

# Definir la lista de pares
pares = [
["informacion de todas las carreras",["ver_carreras"]],
["informacion del estudiante de la carrera",["datos_especificos_estudiante"]],
["informacion de los estudiantes de la carrera",["total_de_estudiantes_carrera"]],
["informacion de estudiantes",
["estudiantes_de_unsxx"]],
#["total de estudiantes en las tres areas tecnologia salud social",["total_estudiantes_area"]]
]
consultas_sql = {
"ver_carreras":"select *from carrera",
"ver_por_nombre_estudiante":" select e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera from carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera where e.nombre_es like '%{}%' ",
"ver_carreras_nombre":"select *from carrera where cod_carrera = {};",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante",
"total_de_estudiantes_carrera":"select *from estudiante as e inner join estudiante_perdio as ep on e.cod_es = ep.cod_es",
"datos_especificos_estudiante":"SELECT e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera,e.cod_es FROM carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera  where  ",
"estudiantes_de_unsxx":"select * from estudiante as e where ",
"seleccionar_carreras_area":"select *from area as a inner join carrera as c on a.cod_area = c.cod_area where ",
"estudiante_por_area":"select *from estudiante as e inner join estudiante_perdio as ep on e.cod_es = ep.cod_es",
"seleccionar_asignatura_estudiante":"select *from cursa_asignatura",
"seleccionar_asignatura_estudiante_calificacion":"select *from cursa_asignatura",
"total_de_estudiantes_estadisticas":"select * from estudiante_perdio",
}
#e.estado = 'desactivo' or e.cod_area = 3 and e.sexo = 'femenino' or  e.sexo = 'masculino';"
consultas_aux= {"activo_es" :" e.estado = 'activo'",
"desactivo_es":" e.estado = 'desactivo'",
"sexo_es_f" :" e.sexo = 'femenino'",
"sexo_es_m":"  e.sexo = 'masculino'",
"departamento_es":" e.departamento = '{}'",
"provincia_es":" e.provincia = '{}'",
"nombre_es":"  e.nombre_es = '{}' ",
"apellido_p_es":"  e.ap_es = '{}' ",
"apellido_m_es":"  e.am_es = '{}' ",
"nombre_carrera":" e.cod_carrera = {}",

"nombre_es_especifico":" e.nombre_es = '{}' ",
"apellido_p_es_especifico":" e.ap_es = '{}' ",
"apellido_m_es_especifico":" e.am_es = '{}' ",

"activo_es_unsxx" :" e.estado = 'activo' ",
"desactivo_es_unsxx":" e.estado = 'desactivo' ",
"sexo_es_f_unsxx" :" e.sexo = 'femenino' ",
"sexo_es_m_unsxx":" e.sexo = 'masculino' ",
"departamento_es_unsxx":" e.departamento = '{}' ",
"provincia_es_unsxx":" e.provincia = '{}'",
"nombre_carrera":" e.cod_carrera = {} ",
"cod_area":" c.cod_area = {}",
"cod_area_cursa":" e.cod_area = {}",
"desercion":" abandono = '{}'",
"aplazaron":" estado_ano = '{}'",
"curso_estudiante":" ep.cod_grado = {}",
"id_carrera":" cod_carrera = {}",
"id_estudiante": "cod_es = {}",
"id_grado": "cod_grado = {}",
"fechai": " fecha >= '{}'",
"fechaf": " fecha <= '{}'",
}


config = dotenv_values(".env")

# Cargar el modelo Sentence-Transformers
modelo = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')

# Función para obtener el embedding de un texto
def obtener_embedding(texto):
    embedding = modelo.encode([texto])[0]
    return embedding

# Funciones para calcular la similitud
def similitud_coseno(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def similitud(texto1, texto2):
    embedding1 = obtener_embedding(texto1)
    embedding2 = obtener_embedding(texto2)
    return similitud_coseno(embedding1, embedding2)

def lista_similitud(texto, lista_textos):
    embedding1 = obtener_embedding(texto)
    similitudes = []
    for texto2 in lista_textos:
        embedding2 = obtener_embedding(texto2[0])
        similitudes.append(similitud_coseno(embedding1, embedding2))
    return similitudes

def texto_mas_similar(texto, lista_textos):
    similitudes = lista_similitud(texto, lista_textos)
    return lista_textos[similitudes.index(max(similitudes))]

def texto_mas_similar_con_similitud(texto, lista_textos):
    similitudes = lista_similitud(texto, lista_textos)
    return lista_textos[similitudes.index(max(similitudes))], max(similitudes)

def texto_mas_similar_con_umbral_similitud(texto, lista_textos, umbral):
    similitudes = lista_similitud(texto, lista_textos)
    max_similitud = max(similitudes)
    if max_similitud < umbral:
        return None, max_similitud
    return lista_textos[similitudes.index(max_similitud)], max_similitud

def obtener_consulta_sql(texto, lista_textos, consultas_sql):
    texto_mas_sim = texto_mas_similar(texto, lista_textos)
      # Obtener la consulta SQL asociada al texto más similar
    print(texto_mas_sim, "los textos similares son ")
    if texto_mas_sim:
        return texto_mas_sim[1]  # Formatear la consulta SQL si necesita algún parámetro
    else:
        return "argumentar_poco_mas"  # Manejar el caso donde no se encuentra la consulta SQL

def buscar(texto):

    consulta = ""
    response = "argumentar_poco_mas"
    resp = obtener_consulta_sql(texto, pares, consultas_sql)
    print(response,"   esta es la respuesta")
    response = resp[0]
    nombre_posicion_sql = ""
    print(response," preguntamos")
    if response != "argumentar_poco_mas" and response != "":
        print(response," preguntamos 545")
        vec1=[]
        if response == "ver_carreras":
            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:
                vec1.append("si_car_n")
                # Obtener la primera carrera encontrada
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "ver_carreras_nombre"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
            else:
                vec1.append("si_car")
                nombre_posicion_sql = "ver_carreras"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response== "total_de_estudiantes":
            hay = "no"
            response = ""
            vec1=[]
            #puede decir el total de estudiante de la carrera infor
            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:#si existe algun nombre de carrera ingresa
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "total_de_estudiantes_carrera"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
                hay  = 'si'
                vec1.append("total_es_car")
            if hay == 'no':
                nombre_posicion_sql = "total_de_estudiantes"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql
                vec1.append("total_es_unsxx")
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response== "total_de_estudiantes_carrera":
                vec = []
                vec1 = []
                response = "";
                carreras_encontradas = obtener_carreras_nombre(texto);
                if carreras_encontradas:#si existe algun nombre de carrera ingresa
                    vec.append("si_car")
                    nombre_posicion_sql = "total_de_estudiantes_carrera"
                    sql = consultas_sql[nombre_posicion_sql]
                    print(carreras_encontradas,"  estas son las carreras")
                    if contiene_palabras_activas(texto):#si contiene la palabra activo ingresa
                        vec.append("si_activo")
                    else:
                        vec.append("no")

                    if contiene_palabras_desactivas(texto):#si contiene la palabra desactivo o al relacionado ingresa
                        vec.append("si_desactivo")
                    else:
                        vec.append("no")

                    if contiene_palabras_sexo_varon(texto):#si contiene la palabra sexo
                        vec.append("si_m")
                    else:
                        vec.append("no")
                    if contiene_palabras_sexo_mujer(texto):#si contiene femenino ingresa
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
        if response == "datos_especificos_estudiante":
            vec=[]
            vec1=[]
            response = ""
            carreras_encontradas = obtener_carreras_nombre(texto);
            nombre_posicion_sql = "datos_especificos_estudiante"
            sql = consultas_sql[nombre_posicion_sql]
            if carreras_encontradas:#si existe algun nombre de carrera ingresa
                vec.append("si_car")
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
            si = "no"
            print(ap,"  esto son los apellidos")
            for i in range(len(vec)):
                vec1.append(vec[i])
            vec1.append(nombre_posicion_sql)
            for i in range(len(vec)):
                if vec[i] == "si_car" and si == "no":
                    auxi = consultas_aux["nombre_carrera"]
                    primera_carrera = carreras_encontradas.pop(0)
                    response += auxi.format(primera_carrera)
                    si = "si"
                elif vec[i] == "si_car" and si == "si":
                    auxi = consultas_aux["nombre_carrera"]
                    primera_carrera = carreras_encontradas.pop(0)
                    si = "si"
                    response += " and "+auxi.format(primera_carrera)
                if vec[i] == "si_nom" and si == "no":
                    sql_aux = consultas_aux["nombre_es_especifico"]
                    response += sql_aux.format(nomb)
                    si = "si"
                elif vec[i] == "si_nom" and si == "si":
                    sql_aux = consultas_aux["nombre_es_especifico"]
                    response += " and "+sql_aux.format(nomb)
                    si = "si"
                    #apellidos
                if vec[i] == "si_apell" and si == "no":
                    if len(ap) == 1:#numero de apellidos maryor a 1
                        sql_aux = consultas_aux["apellido_p_es_especifico"]
                        response += sql_aux.format(ap[0])
                    elif len(ap)>1:
                        sql_aux = consultas_aux["apellido_p_es_especifico"]
                        response += sql_aux.format(ap[0])
                        sql_aux = consultas_aux["apellido_m_es_especifico"]
                        response += sql_aux.format(ap[1])
                    si = "si"
                elif vec[i] == "si_apell" and si == "si":
                    if len(ap) == 1:#numero de apellidos maryor a 1
                        sql_aux = consultas_aux["apellido_p_es_especifico"]
                        response += " and "+sql_aux.format(ap[0])
                    elif len(ap)>1:
                        sql_aux = consultas_aux["apellido_p_es_especifico"]
                        response += " and "+sql_aux.format(ap[0])
                        sql_aux = consultas_aux["apellido_m_es_especifico"]
                        response += " or "+sql_aux.format(ap[1])
                    si = "si"
            response = sql+" "+response
            vec1.append(response);
        if response == "estudiantes_de_unsxx":
            existe  ="no"
            response = ""
            vec = []
            nombre_posicion_sql = "estudiantes_de_unsxx"
            sql = consultas_sql[nombre_posicion_sql]
        #realizamos consultas de if para saber en  llega y poder el and o no
            if contiene_palabras_activas(texto):#si contiene la palabra activo ingresa
                vec.append("si_activo")
            else:
                vec.append("no")

            if contiene_palabras_desactivas(texto):#si contiene la palabra desactivo o al relacionado ingresa
                vec.append("si_desactivo")
            else:
                vec.append("no")
            if contiene_palabras_sexo_varon(texto):#si contiene la palabra sexo
                vec.append("si_m")
            else:
                vec.append("no")
            if contiene_palabras_sexo_mujer(texto):#si contiene femenino ingresa
                vec.append("si_f")
            else:
                vec.append("no")
            pr_encontrado = palabras_provincia(texto)#si contiene algun departamento ingresa
            if pr_encontrado != "no":
                vec.append("si_prov")
            else:
                vec.append("no")

            dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
            if dep_encontrado != "no":
                vec.append("si_dep")
            else:
                vec.append("no")
            si = "no"
            vec1 = []
            for i in range(len(vec)):
                vec1.append(vec[i])
            vec1.append(nombre_posicion_sql)
            for i in range(len(vec)):
                if vec[i] == "si_activo" and si == "no":
                    response += consultas_aux["activo_es_unsxx"]
                    si = "si"
                elif vec[i] == "si_activo" and si == "si":
                    response += " and "+consultas_aux["activo_es_unsxx"]
                    si = "si"

                if vec[i] == "si_desactivo" and si == "no":
                    response += consultas_aux["desactivo_es_unsxx"]
                    si = "si"
                elif vec[i] == "si_desactivo" and si == "si":
                    response += " and "+consultas_aux["desactivo_es_unsxx"]
                    si = "si"

                if vec[i] == "si_m" and si == "no":
                    response += consultas_aux["sexo_es_m_unsxx"]
                    si = "si"
                elif vec[i] == "si_m" and si == "si":
                    response += " and "+consultas_aux["sexo_es_m_unsxx"]
                    si = "si"

                if vec[i] == "si_f" and si == "no":
                    response += consultas_aux["sexo_es_f_unsxx"]
                    si = "si"
                elif vec[i] == "si_f" and si == "si":
                    response += " and "+consultas_aux["sexo_es_f_unsxx"]
                    si = "si"

                if vec[i] == "si_prov" and si == "no":
                    sql_aux = consultas_aux["provincia_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(pr_encontrado)
                elif vec[i] == "si_prov" and si == "si":
                    sql_aux = " and "+consultas_aux["provincia_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(pr_encontrado)
                if vec[i] == "si_dep" and si == "no":
                    sql_aux = consultas_aux["departamento_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(dep_encontrado)
                elif vec[i] == "si_dep" and si == "si":
                    sql_aux = " and "+consultas_aux["departamento_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(dep_encontrado)
                print(vec[i],  si)
                vec[i] = "no"
                #print(vec[i])
            #print(response,"   eess")
            response = sql + response
            vec1.append(response)
        if response == "seleccionar_carreras_area":#nos permite seleccionar todas las carreras por area
            vec1 = []
            response = ""
            ar = obtener_area(texto)  # Supongamos que esto devuelve una lista de áreas
            if ar:
                vec1.append("si_ar")  # Agrega "si_ar" a vec1 si se encontraron áreas en el texto
            else:
                vec1.append("no")  # Agrega "no" a vec1 si no se encontraron áreas en el texto
            nombre_posicion_sql = "seleccionar_carreras_area"
            sql = consultas_sql[nombre_posicion_sql]  # Obtiene la consulta SQL según el nombre de la posición
            si = "no"
            unir = ""
            for i in range(len(ar)):
                sql_aux = consultas_aux["cod_area"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                if si == "no":
                    response += sql_aux.format(ar[i])  # Agrega la consulta auxiliar al response si es la primera iteración
                    unir+=str(ar[i])+"|"
                    si = "si"
                elif si == "si":
                    unir+=str(ar[i])+"|"
                    response += " or " + sql_aux.format(ar[i])  # Agrega "or" y la consulta auxiliar al response para otras iteracpara otras iteraciones
            vec1.append(unir)
            vec1.append(nombre_posicion_sql)  # Agrega el nombre de la posición SQL a vec1
            response = sql + response  # Combina la consulta principal con las consultas auxiliares
            vec1.append(response)  # Agrega la consulta completa a vec1
        if response == "estudiante_por_area":#obtner estudiantes por area
            existe  ="no"
            response = ""
            vec = []
            nombre_posicion_sql = "estudiante_por_area"#creamos una varible para referenciar a mi array consultas_sql
            sql = consultas_sql[nombre_posicion_sql]#obtenemos la consulta
            #realizamos preguntas del texto ingresado para saber que es lo que busca el usuario
            if contiene_palabras_activas(texto):#si contiene la palabra activo ingresa
                vec.append("si_activo")
            else:
                vec.append("no")

            if contiene_palabras_desactivas(texto):#si contiene la palabra desactivo o al relacionado ingresa
                vec.append("si_desactivo")
            else:
                vec.append("no")
            if contiene_palabras_sexo_varon(texto):#si contiene la palabra sexo
                vec.append("si_m")
            else:
                vec.append("no")
            if contiene_palabras_sexo_mujer(texto):#si contiene femenino ingresa
                vec.append("si_f")
            else:
                vec.append("no")
            pr_encontrado = palabras_provincia(texto)#si contiene algun departamento ingresa
            if pr_encontrado != "no":
                vec.append("si_prov")
            else:
                vec.append("no")

            dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
            if dep_encontrado != "no":
                vec.append("si_dep")
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
            ar = obtener_area(texto)  # Supongamos que esto devuelve una lista de áreas
            if ar:
                vec.append("si_ar")  # Agrega "si_ar" a vec1 si se encontraron áreas en el texto
            else:
                vec.append("no")  # Agrega "no" a vec1 si no se encontraron áreas en el texto
            si = "no"
            vec1 = []
            unir = ""
            for i in range(len(vec)):
                vec1.append(vec[i])

            for i in range(len(vec)):
                if vec[i] == "si_activo" and si == "no":
                    response += consultas_aux["activo_es_unsxx"]
                    si = "si"
                elif vec[i] == "si_activo" and si == "si":
                    response += " and "+consultas_aux["activo_es_unsxx"]
                    si = "si"

                if vec[i] == "si_desactivo" and si == "no":
                    response += consultas_aux["desactivo_es_unsxx"]
                    si = "si"
                elif vec[i] == "si_desactivo" and si == "si":
                    response += " and "+consultas_aux["desactivo_es_unsxx"]
                    si = "si"

                if vec[i] == "si_m" and si == "no":
                    response += consultas_aux["sexo_es_m_unsxx"]
                    si = "si"
                elif vec[i] == "si_m" and si == "si":
                    response += " and "+consultas_aux["sexo_es_m_unsxx"]
                    si = "si"

                if vec[i] == "si_f" and si == "no":
                    response += consultas_aux["sexo_es_f_unsxx"]
                    si = "si"
                elif vec[i] == "si_f" and si == "si":
                    response += " and "+consultas_aux["sexo_es_f_unsxx"]
                    si = "si"

                if vec[i] == "si_prov" and si == "no":
                    sql_aux = consultas_aux["provincia_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(pr_encontrado)
                elif vec[i] == "si_prov" and si == "si":
                    sql_aux = " and "+consultas_aux["provincia_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(pr_encontrado)
                if vec[i] == "si_dep" and si == "no":
                    sql_aux = consultas_aux["departamento_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(dep_encontrado)
                elif vec[i] == "si_dep" and si == "si":
                    sql_aux = " and "+consultas_aux["departamento_es_unsxx"]
                    si = "si"
                    response += sql_aux.format(dep_encontrado)
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

                if vec[i] == "si_ar" and si == "no":
                    sql_aux = consultas_aux["cod_area_cursa"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                    response += sql_aux.format(ar[0])  # Agrega la consulta auxiliar al response si es la primera iteración
                    unir+=str(ar[0])+"|"
                    si = "si"
                elif vec[i] == "si_ar" and si == "si":
                    sql_aux = consultas_aux["cod_area_cursa"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                    unir+=str(ar[0])+"|"
                    response += " and " + sql_aux.format(ar[0])  # Agrega "or" y la consulta auxiliar al response para otras iteracpara otras iteraciones
                    si = "si"
                print(vec[i],  si)
                vec[i] = "no"
                #print(vec[i])
            #print(response,"   eess")
            vec1.append(unir)
            vec1.append(nombre_posicion_sql)
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response

            response = sql + response
            vec1.append(response)

        if response == "seleccionar_asignatura_estudiante":
            vec = []
            vec1 = []
            response = "";
            contar_parametros = 0
            if palabra_nota(texto) != "no":
                vec.append("si_cali")
            else:
                vec.append("no")
            carreras_encontradas = obtener_carreras_nombre(texto);
            nombre_posicion_sql = "seleccionar_asignatura_estudiante"
            sql = consultas_sql[nombre_posicion_sql]

            if carreras_encontradas:#si existe algun nombre de carrera ingresa
                vec.append("si_car")
                print(carreras_encontradas,"  estas son las carreras")
            else:
                vec.append("no")
            nombre = "no"
            apellido = "no"
            nomb = encontrar_nombre(texto)#si existe algun nombre ingresa
            if nomb != "no":
                nombre = "si"
            ap = encontrar_apellido(texto)#si hay algun apellido ingresa
            if ap != "no" and nombre == "si":
                apellido = "si"
            if nombre == "si" or apellido == "si":
                id_estudiante = seleccionar_estudiante1(nomb,ap,carreras_encontradas)#buscamos el id con el nombre y apellido del estudiante
                print(id_estudiante,"   no hay estudiante")
                if id_estudiante == "no":
                    vec.append("no")
                    vec1.append(nomb)
                    vec1.append(ap[0])
                else:
                    vec.append("si_nom_apell")
                    vec1.append("")
                    vec1.append("")
            else:
                vec.append("no")
                vec1.append("")
                vec1.append("")
            curso = palabra_curso(texto)
            id_curso = "no";
            id_curso=obtener_que_curso_quiere(texto)
            if curso != "no" or id_curso != "no" and  len(id_curso) != 0:#existe la palabra curso
                vec.append("si_curso")
            else:
                vec.append("no")
            si = "no"
            print(id_curso)
            for i in range(len(vec)):
                vec1.append(vec[i])
            vec1.append(nombre_posicion_sql)

            for i in range(len(vec)):
                if vec[i] == "si_car" and si == "no":
                    sql_aux = consultas_aux["id_carrera"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                    response += sql_aux.format(carreras_encontradas[0])
                    si = "si"
                elif vec[i] == "si_car" and si == "si":
                    sql_aux = consultas_aux["id_carrera"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                    response += " and "+sql_aux.format(carreras_encontradas[0])
                    si = "si"
                if vec[i] == "si_nom_apell" and si == "no":
                    sql_aux = consultas_aux["id_estudiante"]
                    response+=sql_aux.format(id_estudiante)
                    si = "si"
                elif vec[i] == "si_nom_apell" and si == "si":
                    sql_aux = consultas_aux["id_estudiante"]
                    response+=" and "+sql_aux.format(id_estudiante)
                    si = "si"

                if vec[i] == "si_curso" and si == "no":
                    sql_aux = consultas_aux["id_grado"]
                    si = "si"
                    response+= sql_aux.format(id_curso.pop(0))
                elif vec[i] == "si_curso" and si == "si":
                    sql_aux = consultas_aux["id_grado"]
                    si = "si"
                    response+= " and "+sql_aux.format(id_curso.pop(0))
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            response = sql+response
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response == "total_de_estudiantes_estadisticas":#obtener estadistica de estudiantes aprobados y reprobados
            vec = []
            vec1 = []
            response = "";
            desercion = palabra_desercion(texto)#buscamos palabras relacionados con desercion o relacionado
            if desercion != "no":
                vec.append("si_des")
            else:
                vec.append("no")

            aplazar = palabra_aplazaron(texto)#buscamos palabras relacionados con aplazar

            if aplazar != "no":
                vec.append("si_apla")
            else:
                vec.append("no")

            aprobado = palabra_aprobados(texto)
            if aprobado != "no":
                vec.append("si_apro")
            else:
                vec.append("no")

            fecha = fechas(texto)
            if len(fecha) >= 1:#si existe fechas
                vec.append("si_fecha")
                if len(fecha) == 1:
                    fecha1 = fecha[0]
                    fecha2 = ""
                elif len(fecha)>1:
                    fecha1 = fecha[0]
                    fecha2 = fecha[1]
            else:#no hay fechas
                vec.append("no")
                fecha1 = ""
                fecha2 = ""

            print(fecha)
            nombre_posicion_sql = "total_de_estudiantes_estadisticas"
            sql = consultas_sql[nombre_posicion_sql]
            for i in range(len(vec)):
                vec1.append(vec[i])
            si = "no"
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        return vec1
    else:
        vec1=[]
        vec1.append("argumentar_poco_mas")
        return vect1
textoo = "detalle de los estudiantes activos de la universidad nacional siglo xx"
re = buscar(textoo)

print(re)
#falta
#cuantas mujeres y cuantos hombres hay en informatica



#funcionan
#todos los estudiantes de oruro en la unsxx y esten activos tambien de provincia cercado
#estudiante de la carrera informatica
#estudiante de la carrera informatica que esten activos y sexo masculino
#cuantos estudiantes tiene la carrera de informatica
#todas las carreras de la unxx
#detalle de la unsxx
#me puedes brindar informacion de la carrera informatica
# la informacion del total de estudiantes de la carrera de mecanica automotriz
#datos del estudiante juan lima de la carrera de informatica
#datos del estudiante juan lima jurado de la carrera de informatica
#total de estudiantes del departamento de oruro unsxx y que sean mujeres
#todos los estudiantes del departamento de oruro unsxx
#area de tecnologia cuantos estudiantes tiene
#area de tecnologia cuantos estudiantes tiene y activos
#cuantos estudiantes son del departamento de oruro en  el area tecnologia
#cuantos estudiantes aplazados tenemos en el area tecnologia
#cuantos estudiantes desertados tenemos en el area tecnologia
#total de estudiantes reprobados en el area de tecnologia
#total de estudiantes aprobados en el area de tecnologia
#cuantos estudiantes reprobados hay en la carrera de informatica
#cuales son las materias del estudiante fabian sierra de la carrera de informatica
#cuales son las materias del estudiante fabian sierra de la carrera de informatica del 2do año
#cuantos estudiantes reprobados hay en la carrera de informatica
#estadistica de estudiantes reprobados en la unsxx de fechas del 03/02/2024
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
    if row[2] == "no":#no abandonaron
        capro += 1
        vapro[row[5]-1] += 1
        vareasApro[row[7]-1] += 1
    elif row[2] == "si":#si abandonaron
        caplaz += 1
        vaplaz[row[5]-1] += 1
        vareasApla[row[7]-1] += 1

    if row[8]>=fecha1 and row[8] <= fecha2:#la fecha obtenidad tiene que estar en ese rango

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

print(c_infor)
mensaje = "La cantidad que desertaron "
mensaje += "es lo siguiente por área y carreras"
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
    html += "<center><h5>Los estudiantes que abandonaron son: "+str(capro)+"</h5></center>"
    html += "<center><h5>Los estudiantes que siguen adelante son: "+str(caplaz)+"</h5></center>"
    html += "</div>"
    html += "</div>"
    html += "</div>"
html += "</div>"
h = 1
for i in range(17):#recorremos con un for las 17 carrerasy creamos un canvas para cada carrera
    html += "<div class='row'>"
    html += "<h4 align = 'center'>Carrera</h4>"
    html += "<h5 align = 'center'>"+ac[i]+"</h5>"
    html += "<div class='col-lg-3'>"
    html += "<div class='panel panel-default text-center'>"
    html += "<div class='panel-heading'>"
    html += "</div>"
    html += "<div class='panel-body'>"
    html += "<center><h5>Los estudiantes que abandonaron son: "+str(vapro[i])+"</h5></center>"
    html += "<center><h5>Los estudiantes que siguen adelante son: "+str(v_aplaz[i])+"</h5></center>"
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
            if h == 1:
                html += "<h6>Estudiante que abandonaron son: " + str(c_infor[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_inforr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 2:
                html += "<h6>Estudiante que abandonaron son: " + str(c_civil[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_civilr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 3:
                html += "<h6>Estudiante que abandonaron son: " + str(c_minas[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_minasr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 4:
                html += "<h6>Estudiante que abandonaron son: " + str(c_elec[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_elecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 5:
                html += "<h6>Estudiante que abandonaron son: " + str(c_mec[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_mecr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 6:
                html += "<h6>Estudiante que abandonaron son: " + str(c_agro[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_agror[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 7:
                html += "<h6>Estudiante que abandonaron son: " + str(c_lit[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_litr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 8:
                html += "<h6>Estudiante que abandonaron son: " + str(c_der[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_derr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 9:
                html += "<h6>Estudiante que abandonaron son: " + str(c_cie[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_cier[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 10:
                html += "<h6>Estudiante que abandonaron son: " + str(c_cont[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_contr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 11:
                html += "<h6>Estudiante que abandonaron son: " + str(c_odon[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_odonr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 12:
                html += "<h6>Estudiante que abandonaron son: " + str(c_lab[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_labr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 13:
                html += "<h6>Estudiante que abandonaron son: " + str(c_enf[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_enfr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 14:
                html += "<h6>Estudiante que abandonaron son: " + str(c_med[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_medr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 15:
                html += "<h6>Estudiante que abandonaron son: " + str(c_bio[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_bior[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 16:
                html += "<h6>Estudiante que abandonaron son: " + str(c_cso[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_csor[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            if h == 17:
                html += "<h6>Estudiante que abandonaron son: " + str(c_quim[anio][j]) + "</h6>"
                html +="<h6>Estudiantes que siguen adelante son: " + str(c_quimr[anio][j]) + "</h6>"  # Valores para cada sección de la torta
            html += "</div>"
            html += "</div>"
            html += "</div>"
        k = k + 1
    h = h + 1
    html += "</div>"
