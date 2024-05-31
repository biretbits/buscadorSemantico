

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter
import spacy
from spacy.matcher import Matcher

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

patterns = {
#patrones para obtener carrera y tambien poder obtener carrear por su nombre
"ver_carreras": [
    {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
    {"LEMMA": {"IN": ["carrera"]}},
    {"LEMMA": {"IN": ["cual","cuales"]}, "OP": "?"},
    {"LEMMA": {"IN": ["unsxx"]}, "OP": "?"},
    {"LEMMA": {"IN": ["ingenieria"]}, "OP": "?"},
    {"LEMMA": {"IN": ["datos","informacion","detalle"]}, "OP": "?"},
],
#patrones para obtener el total de estudiantes en la unsxx
"total_de_estudiantes": [
    {"LEMMA": {"IN": ["", "ver", "visualizar"]}, "OP": "?"},
    {"LEMMA": {"IN": ["total", "cantidad", "cuantos","numero"]}},
    {"LEMMA": {"IN": ["estudiante", "alumno"]}},
    {"LEMMA": {"IN": ["universidad", "unsxx"]}, "OP": "?"}
],
    "SHOW_FAILED_STUDENTS": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["estudiante", "alumno"]}},
        {"LEMMA": {"IN": ["aplazar", "reprobar",""]}},
        {"LEMMA": {"IN": ["carrera", "grado"]}, "OP": "?"},
        {"LOWER": {"IN": ["mecánica", "ingeniería mecánica"]}, "OP": "?"}
    ],

}





consultas_sql = {"ver_carreras":"select *from carrera",
"ver_carreras_nombre":"select *from carrera where nombre_carrera like '%{}%';",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante;"
}




def buscar(texto):
    text = texto.lower()
    # Añadir patrones al matcher con sus etiquetas correspondientes
    for intent, pattern in patterns.items():
        matcher.add(intent, [pattern])
    # Procesar el texto
    doc = nlp(text)
    # Enviar los tokens SpaCy al matcher
    matches = matcher(doc)

    # Determinar la intención del usuario
    intencion = None
    for match_id, start, end in matches:
        match_id_str = nlp.vocab.strings[match_id]
        matched_span = doc[start:end]
        intencion = match_id_str  # Guardar la intención correspondiente
        #print(f"Coincidencia: {matched_span.texto}, Intención: {intencion}")
    response = ""
    nombre_posicion_sql = ""
    if intencion:
        if intencion == "ver_carreras":
            carreras_encontradas = obtener_carreras_nombre(text);
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

        if intencion == "total_de_estudiantes":
            nombre_posicion_sql = "total_de_estudiantes"
            sql = consultas_sql[nombre_posicion_sql]
            response = sql

        return response,nombre_posicion_sql
    else:
        return ("Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.")





import numpy as np
from dotenv import dotenv_values
from sentence_transformers import SentenceTransformer

import pymysql
config = dotenv_values(".env")

conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')


# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Cargar el modelo Sentence-Transformers

model = SentenceTransformer('bert-base-nli-mean-tokens')

# Función para obtener el embedding de un texto
def get_embedding(text):
    cursor.execute("SELECT embedding FROM embeddings WHERE texto = %s", (text))
    result = cursor.fetchone()
    if result:
        return np.frombuffer(result[0], dtype=np.float32)
    else:
        embedding = model.encode([text])[0]
        cursor.execute("INSERT INTO embeddings (texto, embedding) VALUES (%s, %s)", (text, embedding.tobytes()))
        conn.commit()
        return embedding

# Funciones para calcular la similitud
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def similarity(text1, text2):
    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)
    return cosine_similarity(embedding1, embedding2)

def similarity_list(text, text_list):
    embedding1 = get_embedding(text)
    similarities = []
    for text2 in text_list:
        embedding2 = get_embedding(text2)
        similarities.append(cosine_similarity(embedding1, embedding2))
    return similarities

def most_similar(text, text_list):
    similarities = similarity_list(text, text_list)
    return text_list[similarities.index(max(similarities))]

def most_similar_with_similarity(text, text_list):
    similarities = similarity_list(text, text_list)
    return text_list[similarities.index(max(similarities))], max(similarities)

def most_similar_with_similarity_threshold(text, text_list, threshold):
    similarities = similarity_list(text, text_list)
    max_similarity = max(similarities)
    if max_similarity < threshold:
        return None, max_similarity
    return text_list[similarities.index(max_similarity)], max_similarity

# BÚSQUEDAS INTELIGENTES CON SENTENCE-TRANSFORMERS Y MYSQL
text_list = ['estudiantes de informatica Obtener, todos los estudiantes , buscar a los estudiantes de informatica',\
             'obtner las carreras de informatica o otras','todos los alumnos de la carrera de informatica quiero obtner'
             ]

text = 'buscar los estudiantes de informatica'

print(f'El texto "{text}" es similar a: "{most_similar(text, text_list)}"')







































import numpy as np
from dotenv import dotenv_values
from sentence_transformers import SentenceTransformer
import pymysql

config = dotenv_values(".env")

# Conexión a la base de datos
conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Cargar el modelo Sentence-Transformers
modelo = SentenceTransformer('bert-base-nli-mean-tokens')

# Función para obtener el embedding de un texto
def obtener_embedding(texto):
    cursor.execute("SELECT embedding FROM embeddings WHERE texto = %s", (texto,))
    resultado = cursor.fetchone()
    if resultado:
        return np.frombuffer(resultado[0], dtype=np.float32)
    else:
        embedding = modelo.encode([texto])[0]
        cursor.execute("INSERT INTO embeddings (texto, embedding) VALUES (%s, %s)", (texto, embedding.tobytes()))
        conn.commit()
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

# Lista de textos con sus consultas SQL asociadas
lista_textos = [
    ["todas las carreras de la universidad nacional siglo xx", "ver_carreras"],
    ["estudiantes aplazados reprobados de la materia de filosofía", "total_de_estudiantes"],
    ["cuantos estudiantes existen en la carrera de mecanica automotriz", "total_de_estudiantes_carrera"],
]

# Consultas SQL asociadas a los textos
consultas_sql = {
    "ver_carreras": "SELECT * FROM carrera",
    "total_de_estudiantes": "SELECT e.nombre_es, e.ap_es, e.am_es, e.ci, e.pais_es, e.departamento, e.provincia, e.ciudad, e.region, e.sexo, c.nombre_carrera FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE e.nombre_es LIKE '%{}%'",
    "total_de_estudiantes_carrera": "SELECT * FROM carrera WHERE cod_carrera = {}",
}

# Función para obtener la consulta SQL correspondiente a un texto dado
def obtener_consulta_sql(texto, lista_textos, consultas_sql):
    texto_mas_sim = texto_mas_similar(texto, lista_textos)
    consulta_sql = consultas_sql.get(texto_mas_sim[1])  # Obtener la consulta SQL asociada al texto más similar
    if consulta_sql:
        return consulta_sql.format(texto)  # Formatear la consulta SQL si necesita algún parámetro
    else:
        return "Consulta no encontrada"  # Manejar el caso donde no se encuentra la consulta SQL

# Texto de ejemplo
texto = 'quieres mostrarme las carreras de la unsxx'

# Obtener y mostrar la consulta SQL correspondiente al texto
consulta = obtener_consulta_sql(texto, lista_textos, consultas_sql)
print(f'La consulta SQL para "{texto}" es: "{consulta}"')
