import spacy
import unicodedata
import pymysql
import re
from sentence_transformers import SentenceTransformer, util
import numpy as np
from unidecode import unidecode


# Cargar el modelo de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v1')
#modelo = SentenceTransformer('paraphrase-MiniLM-L6-v2')
nlp = spacy.load("es_core_news_sm")

def obtener_embedding_de_textos():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT * FROM claves"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)

    if cursor.rowcount > 0:
        res = cursor.fetchall()
        for asi in res:
            texto_embedding = modelo.encode(unidecode(asi[1].lower()))
            embedding_bytes = texto_embedding.tobytes()
            sql_update = "UPDATE claves SET embedding = %s where cod_clave = %s"
            cursor.execute(sql_update, (embedding_bytes, asi[0]))
    conn.commit()
    print("Finalizo")

obtener_embedding_de_textos()
