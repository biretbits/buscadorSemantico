import pymysql
import spacy
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Cargar el modelo de embeddings
modelo = SentenceTransformer('paraphrase-MiniLM-L6-v2')
nlp = spacy.load("es_core_news_sm")

# Función para obtener embeddings de un texto
def obtener_embedding(texto):
    return modelo.encode(texto.lower())

# Función para conectar a la base de datos y obtener embeddings de asignaturas
def obtener_asignaturas():
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()

    sql_consulta = "SELECT * FROM asignatura"
    cursor.execute(sql_consulta)
    res = cursor.fetchall()

    for asi in res:
        if asi[13] == b'':  # Si el campo embedding está vacío
            texto_embedding = obtener_embedding(asi[2])
            embedding_bytes = texto_embedding.tobytes()

            sql_update = "UPDATE asignatura SET embedding = %s WHERE cod_asig = %s"
            cursor.execute(sql_update, (embedding_bytes, asi[0]))

    sql_consu = "SELECT * FROM asignatura"
    cursor.execute(sql_consu)
    embed = cursor.fetchall()

    conn.commit()
    conn.close()

    return embed

# Función para verificar si el texto contiene alguna asignatura
def contiene_asignatura(texto, asignaturas, modelo):
    nuevo = []
    doc = nlp(texto.lower())  # Convertir a minúsculas y procesar con spaCy

    # Filtrar entidades relevantes (asignaturas) identificadas por spaCy
    asignaturas_mencionadas = [entidad.text for entidad in doc]
    secuencias=[]
    for longitud in range(1, len(asignaturas_mencionadas) + 1):
        for i in range(len(asignaturas_mencionadas) - longitud + 1):
            subsecuencia = ' '.join(asignaturas_mencionadas[i:i + longitud])
            secuencias.append(subsecuencia)
    for asig in secuencias:
        embeddings_texto = obtener_embedding(asig)
        nuevo.append(embeddings_texto)
    asignaturas_encontradas = []
    asi=[]

    umbral = 0.9
    for enc in nuevo:
        max = 0
        for asign in asignaturas:

            embedding_bd = np.frombuffer(asign[13], dtype=np.float32)#obtenemos su embedding de cada consulta
            coseno_similar = util.cos_sim(enc, embedding_bd)#calculamos el coseno de similitud
            coseno_max= coseno_similar.item()
            #coseno_salida.append(coseno_similar.item())
            if coseno_max > max and coseno_max>umbral:#calculamos el maximo item
                max = coseno_max
                id_respuesta = asign[2]#cuardamos la posible respuesta
                asi.append(id_respuesta)
    print(id_respuesta," maximo",max ,asi)

    return asignaturas_encontradas

# Función auxiliar para seleccionar datos de la asignatura por su ID
def seleccionar_asignatura_por_id(id_asignatura):
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')
    cursor = conn.cursor()

    sql_consulta = "SELECT * FROM asignatura WHERE cod_asig = %s"
    cursor.execute(sql_consulta, (id_asignatura,))
    asignatura = cursor.fetchone()

    conn.close()
    return asignatura

# Obtener las asignaturas desde la base de datos
asignaturas = obtener_asignaturas()

# Ejemplo de uso
texto = "El próximo semestre tengo clases de fisica i y de fisica ii y de taller de programacion y tambien de analisis matematico"
asignaturas_encontradas = contiene_asignatura(texto, asignaturas, modelo)

if asignaturas_encontradas:
    for asignatura in asignaturas_encontradas:
        print(f"¿El texto contiene la asignatura '{asignatura[2]}'?")
else:
    print("No se encontraron asignaturas en el texto.")
