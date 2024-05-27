

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido,obtener_area,palabra_desercion
from comprobar import palabra_aplazaron
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.metrics import jaccard_distance

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Definir la lista de pares
pares = [
["cuales cual carrera carreras unsxx direccion datos datos detalle universidad nacional siglo xx lugar informacion encuentra",["ver_carreras"]],
#6
["cuales cual total estudiante estudiantes unxx universidad nacional siglo xx cantidad numero todos",["total_de_estudiantes"]],
["quiero desahilitados desahilitado habilitado habilitados cuales cual total informacion estudiante estudiantes carrera unxx universidad nacional siglo xx cantidad numero mostrar visualizar detalle sexo activo activos desactivos desactivo departamento pais provincia ciudad region mujeres varones femenino masculino",
["total_de_estudiantes_carrera"]],
["datos datos estudiante estudiantes quiero los del informacion carrera buscar busqueda",["datos_especificos_estudiante"]],
["todos total del los estudiantes estudiante unsxx de universidad nacional siglo xx cantidad numero mostrar visualizar detalle sexo activo activos desactivos desactivo departamento pais provincia provincias ciudad region mujeres varones masculino femenino",
["estudiantes_de_unsxx"]],
["todas total mostrar detalle detalles informacion visualizar carreras carrera area tecnologia salud social unsxx",["seleccionar_carreras_area"]
],
["todas total mostrar detalle detalles informacion visualizar estudiante estudiantes carreras carrera area tecnologia salud social unsxx cuantos todos aplazaron aplazados reprobados reprobaron activos habilitados mujeres varones ciudad departamento",["estudiante_por_area"]]]


consultas_sql = {
"ver_carreras":"select *from carrera",
"ver_por_nombre_estudiante":" select e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera from carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera where e.nombre_es like '%{}%' ",
"ver_carreras_nombre":"select *from carrera where nombre_carrera like '%{}%';",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante",
"total_de_estudiantes_carrera":"SELECT e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera FROM carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera  where  ",
"datos_especificos_estudiante":"SELECT e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera FROM carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera  where  ",
"estudiantes_de_unsxx":"select * from estudiante as e where ",
"seleccionar_carreras_area":"select *from area as a inner join carrera as c on a.cod_area = c.cod_area where ",
"estudiante_por_area":" select distinct e.cod_es,e.nombre_es,ap_es,am_es,e.titulo_bachiller,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,ca.ano,ca.calificacion,ca.estado_asignatura,ca.desercion from estudiante as e inner join cursa_asignatura as ca on e.cod_es = ca.cod_es ",
}
#e.estado = 'desactivo' or e.cod_area = 3 and e.sexo = 'femenino' or  e.sexo = 'masculino';"
consultas_aux= {"activo_es" :" e.estado = 'activo'",
"desactivo_es":" e.estado = 'desactivo'",
"sexo_es_f" :" e.sexo = 'femenino'",
"sexo_es_m":"  e.sexo = 'masculino'",
"departamento_es":" e.departamento = '{}'",
"provincia_es":" e.provincia = '{}'",
"nombre_es":"  e.nombre_es like '%{}%' ",
"apellido_p_es":"  e.ap_es like '%{}%' ",
"apellido_m_es":"  e.am_es like '%{}%' ",
"nombre_carrera":"c.nombre_carrera like '%{}%'",

"nombre_es_especifico":" e.nombre_es = '{}' ",
"apellido_p_es_especifico":" e.ap_es = '{}' ",
"apellido_m_es_especifico":" e.am_es = '{}' ",

"activo_es_unsxx" :" e.estado = 'activo' ",
"desactivo_es_unsxx":" e.estado = 'desactivo' ",
"sexo_es_f_unsxx" :" e.sexo = 'femenino' ",
"sexo_es_m_unsxx":" e.sexo = 'masculino' ",
"departamento_es_unsxx":" e.departamento = '{}' ",
"provincia_es_unsxx":" e.provincia = '{}'",
"nombre_carrera":" c.nombre_carrera like '%{}%' ",
"cod_area":" c.cod_area = {}",
"cod_area_cursa":" ca.cod_area = {}",
"desercion":" ca.desercion = '{}'",
"aplazaron":" ca.estado_asignatura = '{}'"
}


#"nombre_es":" and e.nombre_es like '%{}%' ",
#"apellido_p_es":" and e.ap_es like '%{}%' ",
#"apellido_m_es":" and e.am_es like '%{}%' ",

# Función para preprocesar y tokenizar el texto




def preprocess_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())

    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatized_tokens

# Función para calcular la similitud palabra por palabra
def calculate_similarity_word_by_word(user_tokens, query_tokens):
    common_words = set(user_tokens) & set(query_tokens)
    return len(common_words)

def buscar(texto):
    max_similarity = -1
    response_index = -1
    consulta = ""
    response = "argumentar_poco_mas"
    # Tokenizar el texto del usuario
    user_tokens = preprocess_text(texto)

    # Recorremos los pares de consultas
    for i, (input_phrase, responses) in enumerate(pares):
        query_tokens = preprocess_text(input_phrase)
        similarity = calculate_similarity_word_by_word(user_tokens, query_tokens)

        # Si la similitud es mayor, actualiza la respuesta y el índice
        if similarity > max_similarity:
            max_similarity = similarity
            response = responses[0]
    print(response)
    nombre_posicion_sql = ""
    if response:
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
                    si = "no"
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
                            sql_aux = consultas_aux["nombre_es"]
                            response += sql_aux.format(nomb)
                            si = "si"
                        elif vec[i] == "si_nom" and si == "si":
                            sql_aux = consultas_aux["nombre_es"]
                            response += " and "+sql_aux.format(nomb)
                            si = "si"
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
                        elif vec[i] == "si_apell" and si == "si":
                            if len(ap) == 1:#numero de apellidos maryor a 1
                                sql_aux = consultas_aux["apellido_p_es"]
                                response += " or "+sql_aux.format(ap[0])
                            elif len(ap)>1:
                                sql_aux = consultas_aux["apellido_p_es"]
                                response += " or "+sql_aux.format(ap[0])
                                sql_aux = consultas_aux["apellido_m_es"]
                                response += " or "+sql_aux.format(ap[1])
                            si = "si"
                        #print(vec[i])
                        vec[i] = "no"
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
        #realizamos consultas de if para saber en cual llega y poder el and o no
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
                    response+= sql_aux.format('si')
                elif vec[i] == "si_des" and si=="si":
                    sql_aux = " and "+consultas_aux["desercion"]
                    si = "si"
                    response+= sql_aux.format('si')
                if vec[i] == "si_apla" and si == "no":
                    sql_aux = consultas_aux["aplazaron"]
                    si = "si"
                    response+= sql_aux.format('activo')
                elif vec[i] == "si_apla" and si=="si":
                    sql_aux = " and "+consultas_aux["aplazaron"]
                    si = "si"
                    response+= sql_aux.format('activo')

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
        return vec1
    else:
        vec1=[]
        vec1.append("argumentar_poco_mas")
        return vect1
