

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido
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
["provincia provincias cuales cual carrera unsxx direccion datos datos detalle universidad nacional siglo xx lugar informacion encuentra",["ver_carreras"]],
#6
["cuales cual total estudiante estudiantes unxx universidad nacional siglo xx cantidad numero todos",["total_de_estudiantes"]],
["desahilitados desahilitado habilitado habilitados cuales cual total estudiante estudiantes carrera unxx universidad nacional siglo xx cantidad numero mostrar visualizar detalle sexo activo activos desactivos desactivo departamento pais provincia ciudad region",
["total_de_estudiantes_carrera"]],

]

consultas_sql = {
"ver_carreras":"select *from carrera",
"ver_por_nombre_estudiante":" select e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera from carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera where e.nombre_es like '%{}%' ",
"ver_carreras_nombre":"select *from carrera where nombre_carrera like '%{}%';",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante;",
"total_de_estudiantes_carrera":"SELECT e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera FROM carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera  where c.nombre_carrera like '%{}%' "

}

consultas_aux= {"activo_es" :" and e.estado = 'activo'",
"desactivo_es":" and e.estado = 'desactivo'",
"sexo_es_f" :" and e.sexo = 'femenino'",
"sexo_es_m":" and e.sexo = 'masculino'",
"departamento_es":" and e.departamento = '{}'",
"provincia_es":" and e.provincia = '{}'",
"nombre_es":" and e.nombre_es like '%{}%' ",
"apellido_p_es":" or e.ap_es like '%{}%' ",
"apellido_m_es":" or e.am_es like '%{}%' ",
"nombre_carrera":" and c.nombre_carrera like '%{}%' ",}
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

    nombre_posicion_sql = ""
    if response:
        if response == "ver_carreras":
            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:
                # Obtener la primera carrera encontrada
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "ver_carreras_nombre"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
            else:
                nombre_posicion_sql = "ver_carreras"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql


        if response== "total_de_estudiantes":
            hay = "no"
            response = ""
            nomb = encontrar_nombre(texto)
            if nomb != "no":
                nombre_posicion_sql = "ver_por_nombre_estudiante"
                sql_aux = consultas_sql["ver_por_nombre_estudiante"]
                response += sql_aux.format(nomb)
                hay = "si"
            ap = encontrar_apellido(texto)
            if ap != "no":
                if len(ap) > 1:#numero de apellidos maryor a 1
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += sql_aux.format(ap[0])
                else:
                    sql_aux = consultas_aux["apellido_p_es"]
                    response += sql_aux.format(ap[0])
                    sql_aux = consultas_aux["apellido_m_es"]
                    response += sql_aux.format(ap[1])
                hay = "si"
                nombre_posicion_sql = "ver_por_nombre_estudiante"

            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "ver_por_nombre_estudiante"
                sql_aux = consultas_aux["nombre_carrera"]
                response += sql_aux.format(primera_carrera)
                hay = "si"

            if hay == "no":
                nombre_posicion_sql = "total_de_estudiantes"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql

        if response== "total_de_estudiantes_carrera":
                carreras_encontradas = obtener_carreras_nombre(texto);
                if carreras_encontradas:

                    primera_carrera = carreras_encontradas.pop(0)
                    nombre_posicion_sql = "total_de_estudiantes_carrera"
                    sql = consultas_sql[nombre_posicion_sql]
                    response = sql.format(primera_carrera)
                    if contiene_palabras_activas(texto):
                        response += consultas_aux["activo_es"]
                    elif contiene_palabras_desactivas(texto):
                        response += consultas_aux["desactivo_es"]
                    if contiene_palabras_sexo_varon(texto):
                        response += consultas_aux["sexo_es_m"]
                    if contiene_palabras_sexo_mujer(texto):
                        response += consultas_aux["sexo_es_f"]

                    dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
                    if dep_encontrado != "no":
                        sql_aux = consultas_aux["departamento_es"]
                        response += sql_aux.format(dep_encontrado)

                    pr_encontrado = palabras_provincia(texto)
                    if pr_encontrado != "no":
                        sql_aux = consultas_aux["provincia_es"]
                        response += sql_aux.format(pr_encontrado)

                    nomb = encontrar_nombre(texto)
                    if nomb != "no":
                        sql_aux = consultas_aux["nombre_es"]
                        response += sql_aux.format(nomb)

                    ap = encontrar_apellido(texto)
                    if ap != "no":
                        if len(ap) > 1:#numero de apellidos maryor a 1
                            sql_aux = consultas_aux["apellido_p_es"]
                            response += sql_aux.format(ap[0])
                        else:
                            sql_aux = consultas_aux["apellido_p_es"]
                            response += sql_aux.format(ap[0])
                            sql_aux = consultas_aux["apellido_m_es"]
                            response += sql_aux.format(ap[1])
                else:
                    response = "argumentar_poco_mas"
        return response,nombre_posicion_sql
    else:
        return ("argumentar_poco_mas"),nombre_posicion_sql
